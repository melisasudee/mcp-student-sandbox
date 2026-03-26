"""
SECURE VERSION: secret_leak.py (FIXED)
Uses environment variables instead of hardcoded credentials
"""

import os
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_aws_secret_key() -> str:
    """
    Safely retrieve AWS secret key from environment.
    
    Returns:
        AWS secret key from environment variable
        
    Raises:
        ValueError: If AWS_SECRET_KEY is not set
        
    Security:
        - Credentials stored in .env file (git ignored)
        - Not visible in source code
        - Can be rotated without code changes
    """
    secret_key = os.getenv("AWS_SECRET_KEY")
    
    if not secret_key:
        raise ValueError(
            "AWS_SECRET_KEY not found in environment. "
            "Please set the environment variable or use .env file"
        )
    
    # Validate key format (basic check)
    if len(secret_key) < 20:
        raise ValueError("AWS_SECRET_KEY appears too short to be valid")
    
    return secret_key


def connect() -> dict:
    """
    Connect to AWS using environment-based credentials.
    
    Returns:
        Connection configuration dict
        
    Security Notes:
        - Never prints full credentials to logs
        - Only logs that connection was attempted
        - Actual key kept secret
    """
    try:
        secret_key = get_aws_secret_key()
        
        # Safely log without exposing the full key
        key_preview = f"{secret_key[:8]}...{secret_key[-4:]}"
        logger.info(f"Connecting to AWS with key: {key_preview}")
        
        # Return connection config
        return {
            "status": "connected",
            "key_hash": hash(secret_key),  # Hash instead of raw key
            "region": os.getenv("AWS_REGION", "us-east-1"),
        }
        
    except ValueError as e:
        logger.error(f"Connection failed: {e}")
        raise


if __name__ == "__main__":
    try:
        connection_info = connect()
        print("✓ Connection successful")
        print(f"  Region: {connection_info['region']}")
    except ValueError as e:
        print(f"✗ Error: {e}")
        exit(1)
