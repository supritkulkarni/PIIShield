import hashlib

def hash_pii(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()

def verify_pii(value: str, hashed: str) -> bool:
    return hash_pii(value) == hashed
