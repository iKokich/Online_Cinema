import psycopg2

try:
    conn = psycopg2.connect(dbname ='carShop_db',
                            user ='postgres',
                            password = '523678',
                            host = 'localhost',
                            port = '5432')
    print("Database connected...")
except:
    print('Can`t establish connection to database')
