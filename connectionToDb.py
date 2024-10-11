import psycopg2
import yaml

class DatabaseConnection:
    def __init__(self, config_file = 'db_info.yaml'):
        self.config_file = config_file
        self.conn = None

    def connection(self):
        try:
            with open(self.config_file, 'r') as f:
                config = yaml.safe_load(f)
            self.conn = psycopg2.connect(
                dbname = config['database']['dbname'],
                user = config['database']['user'],
                password = config['database']['password'],
                host = config['database']['host'],
                port = config['database']['port']
            )
            print("Database connected successfully!")
        except(Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def close(self):
        if self.conn:
            self.conn.close()
            print("Соединение закрыто")

    def execute(self, query, params=None):
        with self.conn.cursos() as cur:
            cur.execute(query, params)
            self.conn.commit()

    def insert(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())

        query = f"INSET INTO {table_name} ({columns}) VALUES ({placeholders})"

        self.execute(query, values)

    def update(self, table_name, data, where):
        set_clause = ', '.join([f"{key} = %s" for key in data])
        values = tuple(data.values())

        query = f"UPDATE {table_name} SET {set_clause} WHERE {where}"
        self.execute(query, values)

    def delete(self, table_name, where):
        query = f"DELETE FROM {table_name} WHERE {where}"
        self.execute(query)

    def fetchall(self, query):
        with self.conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def get_all_data(self, table_name):
        query = f"SELECT * FROM {table_name}"
        return self.fetchall(query)