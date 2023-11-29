from fastapi import HTTPException
from src.models.form.UserForm import UserForm
from src.models.view.UserView import UserView
from src.settings import CONECTION
import bcrypt

connect = CONECTION

async def create_user(user: UserForm):
    query = "INSERT INTO appuser(name, email, password) VALUES('{}', '{}', '{}') RETURNING id;"
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(user.name, user.email.lower(), user.password)
        cur.execute(sql)
        first = cur.fetchone()
        use = UserView(id=first[0],
                        name=user.name,
                        email=user.email)
        conn.commit()
        return use
    except Exception as e:
        raise HTTPException(status_code=409, detail="Email alrady registered!!!")

async def get_user(user: UserForm):
    query = "SELECT * FROM appuser WHERE email = '{}'"
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(user.email.lower())
        cur.execute(sql)
        first = cur.fetchone()
        if not bcrypt.checkpw(user.password.encode('utf-8'), first[3].encode('utf-8')):
            raise Exception("Authentication failed!")
        internal_user = UserView(id=first[0],
                                name=first[1],
                                email=user.email)
        return internal_user
    except Exception as e:
        print(e)