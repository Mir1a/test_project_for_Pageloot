# Проект

## Установка и запуск
1. Склонируйте репозиторий:
   ```bash
   git clone git@github.com:Mir1a/test_project_for_Pageloot.git
   cd test_project_for_Pageloot

2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv

3. Активируйте виртуальное окружение

4. Установите зависимости:
   ```bash
   pip install -r requirements.txt

5. Проведите миграции:
   ```bash
   python manage.py migrate

6. Запустите проект:
   ```bash
   python manage.py runserver

7. Проверьте эндпоинты: Откройте http://127.0.0.1:8000/api/swagger/ в вашем браузере.
