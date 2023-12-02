import psycopg2
import os

#configurações

host= os.getenv('POSTGRES_HOST')
user= os.getenv('POSTGRES_USER')
password= os.getenv('POSTGRES_PASS')
dbname= os.getenv('POSTGRES_DATABASE')
port= os.getenv('POSTGRES_PORT')

DATABASE_URL = 'host={0} port={1} user={2} dbname={3} password={4}'.format(host , port, user, dbname, password)

CONECTION = psycopg2.connect(DATABASE_URL)

CRYPTKEY = b'$2b$04$HFrP2BAT3GTea9dCVJqFJO'

EXPIRATION = int(8600000)

TOKEN_KEY = 'Kh&I|MTLjh;<98Q!v-kc|C+nHt&+ZIMRCpJTAtjf>B)[b5kt:ji<+:FLYmefhn'