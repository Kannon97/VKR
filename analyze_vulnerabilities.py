import subprocess
import sys

# Функция для запуска Bandit
def run_bandit():
    print("Running Bandit...")
    # Запуск Bandit для сканирования файлов проекта на уязвимости
    subprocess.run([sys.executable, '-m', 'bandit', '-r', 'medical_app.py'])

# Функция для запуска Flake8
def run_flake8():
    print("Running Flake8...")
    # Запуск Flake8 для проверки стиля кода и выявления ошибок
    subprocess.run([sys.executable, '-m', 'flake8', 'medical_app.py'])

# Функция для запуска Safety
def run_safety():
    print("Running Safety...")
    # Запуск Safety для проверки используемых пакетов на наличие известных уязвимостей
    subprocess.run([sys.executable, '-m', 'safety', 'check'])

# Главная функция, которая выполняет все основные операции
def main():
    print("Starting security analysis...\n")
    run_bandit()  # Запуск анализа кода с помощью Bandit
    print("\n")
    run_flake8()  # Запуск проверки стиля кода с помощью Flake8
    print("\n")
    run_safety()  # Запуск проверки зависимостей с помощью Safety
    print("\nSecurity analysis completed.")

if __name__ == '__main__':
    main()