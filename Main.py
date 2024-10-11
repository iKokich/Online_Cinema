from connectionToDb import DatabaseConnection

def main():
    # Инициализация подключения к базе данных
    db = DatabaseConnection(config_file='db_info.yaml')
    db.connect()

    # Пример вставки данных
    data = {'movie_id': 5, 'movie_name': 'Chop-Chop', 'movie_date': 2006, 'movie_genre': 'fantasy'}
    db.insert('Movies', data)

    # Пример получения всех данных
    all_data = db.get_all_data('Movies')
    print(all_data)

    # Закрытие подключения к базе данных
    db.close()

if __name__ == "__main__":
    main()
