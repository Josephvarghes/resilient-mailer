import pytest
from email_service.src.email_service.utils.retry_logic import apply_retry_logic
from email_service.src.email_service.providers import providers

def mock_fail_provider():
    class MockFailProvider:
        def send_email(self, to, subject, body):
            raise Exception("Simulated Failure")
    return MockFailProvider()

def test_retry_logic_success():
    result = apply_retry_logic(providers, 'test@example.com', 'Subject', 'Body')
    assert result['status'] == 'success'
    assert 'provider' in result

def test_retry_logic_failure():
    result = apply_retry_logic([mock_fail_provider()], 'test@example.com', 'Subject', 'Body')
    assert result['status'] == 'failed'
    assert 'error' in result
