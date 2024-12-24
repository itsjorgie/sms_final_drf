from cryptography.fernet import Fernet
from decouple import config

# Load Fernet encryption key from environment
FERNET_SECRET_KEY = config('FERNET_SECRET_KEY')
cipher = Fernet(FERNET_SECRET_KEY)

def encrypt_message(message):
    return cipher.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message.encode()).decode()

def decrypt_sent_message(encrypted_message):
    fernet = Fernet(ENCRYPTION_KEY)
    decrypted_sent_message = fernet.decrypt(encrypted_sent_message.encode()).decode()
    return decrypted_sent_message