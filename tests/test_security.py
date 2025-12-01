from api.security import hash_pii, verify_pii

def test_hash_and_verify():
    original = "john.doe@example.com"
    hashed = hash_pii(original)
    assert verify_pii(original, hashed)