from src.models.form.UserForm import UserForm
from src.models.view.JWTTokenView import JWTTokenView
from src.models.view.UserView import UserView
from src.repository.UserRepository import create_user, get_user
from src.services.TokenService import token_generator

async def userCreate(user: UserForm):
    return await create_user(user)

async def getUser(user: UserForm):
    try:
        internal_user: UserView = await get_user(user)
        tok = await token_generator(internal_user.name, internal_user.id)
        return JWTTokenView(token=tok, userId=internal_user.id)
    except Exception as e:
        print(e)
        raise Exception("Authentication Failed!")