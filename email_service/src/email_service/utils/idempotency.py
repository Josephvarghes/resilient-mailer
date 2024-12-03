sent_emails = set()

def check_idempotency(email_key):
    if email_key in sent_emails:
        return True
    sent_emails.add(email_key)
    return False
