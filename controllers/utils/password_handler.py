import hashlib
import os

def hash_password(password):
    # Create a salt
    salt = os.urandom(32)

    # Use the hashlib.pbkdf2_hmac method to create a hash
    key = hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm to use
        # Convert the password to bytes
        password.encode('utf-8'),
        # Provide the salt
        salt, 
        # It is recommended to use at least 100,000 iterations of SHA-256
        100000
    )

    return salt, key

def verify_password(salt, key, password_to_check):
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password_to_check.encode('utf-8'),
        salt, 
        100000
    )

    return key == new_key