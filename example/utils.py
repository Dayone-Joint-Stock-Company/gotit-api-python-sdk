import base64
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization, hashes
from config import Config
import random
import string
import os

def load_private_key_from_string(private_key_str=None, password=None):
    """
    Load and validate RSA private key from string or environment variable
    """
    try:
        # Get private key from parameter or environment variable
        key_str = private_key_str or os.getenv('PRIVATE_KEY_STR')
        
        # Check if private key is empty
        if not key_str or key_str.strip() == "":
            raise ValueError("Private key is empty. Please set the PRIVATE_KEY_STR environment variable.")
            
        # Verify the private key format
        if not key_str.strip().startswith('-----BEGIN RSA PRIVATE KEY-----'):
            raise ValueError("Invalid private key format. Must start with '-----BEGIN RSA PRIVATE KEY-----'")
        if not key_str.strip().endswith('-----END RSA PRIVATE KEY-----'):
            raise ValueError("Invalid private key format. Must end with '-----END RSA PRIVATE KEY-----'")
        
        # Try to load the private key
        private_key = serialization.load_pem_private_key(
            key_str.encode(),  # Convert string to bytes
            password=password.encode() if password else None
        )
        
        # Verify it's an RSA key
        if not isinstance(private_key, rsa.RSAPrivateKey):
            raise ValueError("The provided key is not an RSA private key")
            
        return private_key
        
    except ValueError as ve:
        raise ValueError(f"Private key validation error: {str(ve)}")
    except Exception as e:
        raise ValueError(f"Failed to load private key: {str(e)}")

def sign_data(private_key, message):
    """
    Sign data using RSA private key
    """
    try:
        signature = private_key.sign(
            message.encode(),  # Convert message to bytes
            padding.PKCS1v15(),  # Use PKCS1 v1.5 padding
            hashes.SHA256()  # Use SHA-256 hashing
        )
        return base64.b64encode(signature).decode()  # Convert to Base64 string
    except Exception as e:
        raise ValueError(f"Failed to sign data: {str(e)}")

def generate_random_string(length=10):
    """
    Generate random string of specified length
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) 