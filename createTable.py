import psycopg2

conn = psycopg2.connect(dbname='carShop_db',
                        user='postgres',
                        password='523678',
                        host='localhost',
                        port='5432')
print("Database connected")
cur = conn.cursor()
cur.execute("CREATE TABLE student(id serial PRIMARY KEY, name CHAR(50), roll integer);")
print("Table created")
conn.commit()
conn.close()