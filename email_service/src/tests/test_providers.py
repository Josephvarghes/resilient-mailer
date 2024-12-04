import pytest
from email_service.src.email_service.providers import MockEmailProvider1,MockEmailProvider2


def test_mock_provider1_success():
    provider = MockEmailProvider1()
    result = provider.send_email('test@example.com', 'Subject', 'Body')
    assert result['status'] == 'success'

def test_mock_provider1_failure():
    provider = MockEmailProvider1()
    provider.random = lambda: 1  # Force failure
    with pytest.raises(Exception, match="Provider 1 failed"):
        provider.send_email('test@example.com', 'Subject', 'Body')

def test_mock_provider2_success():
    provider = MockEmailProvider2()
    result = provider.send_email('test@example.com', 'Subject', 'Body')
    assert result['status'] == 'success'

def test_mock_provider2_failure():
    provider = MockEmailProvider2()
    provider.random = lambda: 1  # Force failure
    with pytest.raises(Exception, match="Provider 2 failed"):
        provider.send_email('test@example.com', 'Subject', 'Body')
