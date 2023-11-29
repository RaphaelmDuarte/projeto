from settings import TOKEN_KEY, EXPIRATION
import jwt

tokey = TOKEN_KEY

async def token_generator(name: str, id: int, ):
    payload = {"id": id, "name": name, "exp": EXPIRATION}
    return jwt.encode(payload, tokey, algorithm="HS256")

async def get_userId(token: str):
    userId: int = jwt.decode(token, options={"verify_signature": False})['id']
    return userId