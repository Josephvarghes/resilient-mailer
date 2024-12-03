import pytest
from email_service.email_service import email_service
from email_service.utils.idempotency import check_idempotency

@pytest.fixture
def reset_sent_emails():
    # Reset sent emails before each test
    global check_idempotency
    check_idempotency.sent_emails.clear()

def test_send_email_success(reset_sent_emails):
    result = email_service.send_email('test@example.com', 'Test Subject', 'Test Body')
    assert result['status'] == 'success'

def test_idempotency(reset_sent_emails):
    email_key = 'test@example.com-Test Subject-Test Body'
    check_idempotency(email_key)  # Mark as sent
    result = email_service.send_email('test@example.com', 'Test Subject', 'Test Body')
    assert result['status'] == 'already_sent'
