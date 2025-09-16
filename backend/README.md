# Backend — Django + DRF

## Docker (recommended)
1. Ensure Docker and docker-compose are installed.
2. From repository root run:
   docker-compose up --build
3. Первый запуск: примените миграции и загрузите фикстуры внутри контейнера:
   docker-compose exec backend python manage.py migrate
   docker-compose exec backend python manage.py loaddata dds_app/fixtures/initial_data.json
4. Создайте суперпользователя (опционально):
   docker-compose exec backend python manage.py createsuperuser
5. API доступно: http://localhost/api/
6. 

## Локальная разработка (без Docker)
1. Создайте виртуальное окружение и активируйте его.
2. Установите зависимости: pip install -r requirements.txt
3. Примените миграции: python manage.py migrate
4. Загрузите фикстуры: python manage.py loaddata dds_app/fixtures/initial_data.json
5. Запустите: python manage.py runserver
