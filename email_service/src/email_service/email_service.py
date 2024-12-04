import random
from email_service.src.email_service.utils.retry_logic import apply_retry_logic
from email_service.src.email_service.utils.idempotency import check_idempotency 
from email_service.src.email_service.providers import MockEmailProvider1,MockEmailProvider2
class EmailService:
    def __init__(self):
        # self.providers = ["provider1", "provider2"]
        self.providers = [MockEmailProvider1(), MockEmailProvider2()]
    
    def send_email(self, to, subject, body):
        email_key = f"{to}-{subject}-{body}"
        
        if check_idempotency(email_key):
            return {"status": "already_sent", "email_key": email_key}
        
        result = apply_retry_logic(self.providers, to, subject, body)
        
        if result['status'] == 'success':
            # Mark email as sent (store email_key for idempotency)
            return result
        return {"status": "failed", "error": result.get('error')}

email_service = EmailService()
