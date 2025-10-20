import hashlib
import base64
DEFAULTSEED = "blah blah"
def generate_password(seed: str, length: int = 6, defaultseed: str = DEFAULTSEED) -> str:
    """I should have a bit more of a doc string.
    """
    biz = seed.lower() + defaultseed.lower()
    salt = hashlib.sha512(biz.encode()).hexdigest()[:20]
    salted_input = seed.lower() + salt.lower()
    hash_bytes = hashlib.sha512(salted_input.encode()).digest()
    password = base64.b64encode(hash_bytes).decode("utf-8")
    password = "".join(filter(str.isalnum, password))
    return password[:length]
