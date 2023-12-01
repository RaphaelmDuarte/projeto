import psycopg2

#configurações

host= '197.170.0.2'
user= 'postgres'
password= 'postgres'
dbname= 'trackseries'
port= '5432'

DATABASE_URL = 'host={0} port={1} user={2} dbname={3} password={4}'.format(host , port, user, dbname, password)

CONECTION = psycopg2.connect(DATABASE_URL)

CRYPTKEY = b'$2b$04$HFrP2BAT3GTea9dCVJqFJO'

EXPIRATION = int(8600000)

TOKEN_KEY = 'Kh&I|MTLjh;<98Q!v-kc|C+nHt&+ZIMRCpJTAtjf>B)[b5kt:ji<+:FLYmefhn'