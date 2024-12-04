import pytest
from email_service.utils.idempotency import check_idempotency

def test_idempotency_not_sent():
    email_key = "user@example.com-Subject-Body"
    assert not check_idempotency(email_key)

def test_idempotency_already_sent():
    email_key = "user@example.com-Subject-Body"
    check_idempotency(email_key)  # Simulate marking email as sent
    assert check_idempotency(email_key) == True
