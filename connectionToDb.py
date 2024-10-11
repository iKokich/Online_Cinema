import psycopg2
import yaml

def connect_to_db(config_file='db_info.yaml'):
    """Подключение к базе данных с использованием конфигурации из YAML-файла.

    Args:
        config_file (str, optional): Путь к YAML-файлу с конфигурацией. По умолчанию 'config.yaml'.

    Returns:
        psycopg2.connection.connection: Объект подключения к базе данных.
    """

    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)

        conn = psycopg2.connect(
            dbname=config['database']['dbname'],
            user=config['database']['user'],
            password=config['database']['password'],
            host=config['database']['host'],
            port=config['database']['port']
        )
        print("Database connected successfully!")
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

if __name__ == '__main__':
    conn = connect_to_db()

    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Movies;")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        conn.close()
        print("Соединение с базой данных закрыто.")