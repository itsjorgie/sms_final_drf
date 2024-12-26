from cryptography.fernet import Fernet, InvalidToken
from decouple import config

# Load Fernet encryption key from environment
FERNET_SECRET_KEY = config('FERNET_SECRET_KEY')
cipher = Fernet(FERNET_SECRET_KEY)

def encrypt_message(message):
    try:
        return cipher.encrypt(message.encode()).decode()
    except Exception as e:
        raise ValueError(f"Encryption failed: {e}")

def decrypt_message(encrypted_message):
    try:
        return cipher.decrypt(encrypted_message.encode()).decode()
    except InvalidToken:
        raise ValueError("Decryption failed: Invalid encryption key or message.")
    except Exception as e:
        raise ValueError(f"Decryption failed: {e}")
