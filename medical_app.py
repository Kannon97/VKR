import sqlite3
import hashlib

# Функция для установки соединения с базой данных
def connect_db():
    # Создает соединение с базой данных medical_records.db
    conn = sqlite3.connect('medical_records.db')
    return conn

# Функция для создания таблицы patients в базе данных
def create_table(conn):
    conn.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        diagnosis TEXT NOT NULL
    )
    ''')
    conn.commit()

# Функция для добавления нового пациента в таблицу patients
def add_patient(conn, name, diagnosis):
    conn.execute('INSERT INTO patients (name, diagnosis) VALUES (?, ?)', (name, diagnosis))
    conn.commit()

# Функция для получения данных о пациенте по его ID
def get_patient(conn, patient_id):
    cursor = conn.execute('SELECT * FROM patients WHERE id=?', (patient_id,))
    return cursor.fetchone()

# Функция для хэширования паролей
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Главная функция, которая выполняет все основные операции
def main():
    conn = connect_db()  # Устанавливает соединение с базой данных
    create_table(conn)   # Создает таблицу patients
    add_patient(conn, 'John Doe', 'Flu')  # Добавляет пациента в таблицу
    patient = get_patient(conn, 1)  # Получает данные о пациенте с ID 1
    print(f'Patient: {patient}')  # Выводит данные о пациенте
    password = 'password123'
    print(f'Hashed password: {hash_password(password)}')  # Хэширует и выводит пароль

if __name__ == '__main__':
    main()