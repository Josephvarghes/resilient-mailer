import random

class MockEmailProvider1:
    def send_email(self, to, subject, body):
        if random.random() < 0.7:
            return {"status": "success", "provider": "Provider 1"}
        raise Exception("Provider 1 failed")

class MockEmailProvider2:
    def send_email(self, to, subject, body):
        if random.random() < 0.5:
            return {"status": "success", "provider": "Provider 2"}
        raise Exception("Provider 2 failed")

providers = [MockEmailProvider1(), MockEmailProvider2()]
