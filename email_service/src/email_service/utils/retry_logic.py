import time
from email_service.src.email_service import providers

def apply_retry_logic(provider, to, subject, body): #change provider -> providers
    attempts = 0

    while attempts < 5:
        for provider in providers:
            try:
                return providers.send_email(to, subject, body)
            except Exception as e:
                attempts += 1
                print(f"Attempt {attempts}: Error - {str(e)}")
                time.sleep(2 ** attempts)  # Exponential backoff

    return {"status": "failed", "error": "All providers failed after retries"}
