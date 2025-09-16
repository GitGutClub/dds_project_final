# DDS — Учёт движения денежных средств

Веб-приложение для ведения и анализа движения денежных средств (ДДС).
Стек: **Django + Django REST Framework (backend)**, **React (frontend)**, **PostgreSQL**, **Nginx**, **Docker Compose**.

---

## Основные функции

* Управление доходами и расходами (CRUD).
* Справочники: Типы, Статусы, Категории, Подкатегории.
* Фильтрация записей по датам, категориям, типам и статусам.
* SPA на React с интеграцией через REST API.
* Django Admin для управления данными.
* Автоматическая подстановка текущей даты при создании записи, если дата не указана.
* Nginx для обслуживания API и статических файлов.

---

## 📂 Структура проекта

```
.
├── backend/              # Django backend (API + Admin)
│   ├── dds_project/      # Django проект
│   ├── dds_app/          # Основное приложение (модели, сериализаторы, viewsets)
│   ├── staticfiles/      # Собранная статика Django
│   └── Dockerfile
│
├── frontend/             # React frontend (SPA)
│   ├── src/              # Компоненты React
│   ├── build/            # Сборка (npm run build)
│   └── Dockerfile
│
├── nginx/                # Конфиги nginx
│   └── nginx.conf
│
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Требования

* [Docker](https://www.docker.com/) ≥ 20.10
* [Docker Compose](https://docs.docker.com/compose/) ≥ 2.0

---

## 🔧 Локальный запуск

### 1. Клонируем репозиторий

```bash
git clone https://github.com/yourusername/dds.git
cd dds
```

### 2. Построить и запустить контейнеры

```bash
docker compose up -d --build
```

> Если контейнеры уже существуют:

```bash
docker rm -f dds_backend dds_frontend dds_nginx
docker compose up -d --build
```

### 3. Проверка работы

* Django API: [http://localhost/api/](http://localhost/api/)
* Django Admin: [http://localhost/admin/](http://localhost/admin/)
* React SPA: [http://localhost/](http://localhost/)

### 4. Создание суперпользователя для админки

```bash
docker exec -it dds_backend python manage.py createsuperuser
```

---

## 🛠 Основные команды

### Остановить проект

```bash
docker compose down
```

### Пересобрать контейнеры (очистка кэша)

```bash
docker compose build --no-cache
docker compose up -d
```

### Просмотр логов

```bash
docker compose logs -f backend
docker compose logs -f frontend
docker compose logs -f nginx
```

### Выполнить миграции вручную

```bash
docker exec -it dds_backend python manage.py migrate
```

---

## 🌍 Архитектура

```text
             ┌──────────────┐
             │   React SPA  │
             │ (frontend)   │
             └───────▲──────┘
                     │ (http://localhost)
              ┌──────┴──────┐
              │   Nginx     │
              └──────┬──────┘
        ┌────────────┼─────────────┐
        │            │             │
   (стат. файлы) (API /admin)  (React build)
        │            │             │
 ┌──────▼──────┐ ┌───▼─────────┐ ┌─▼──────────────┐
 │ Django App  │ │ Gunicorn    │ │ PostgreSQL      │
 │ (backend)   │ │ (WSGI)      │ │ (БД)           │
 └─────────────┘ └─────────────┘ └────────────────┘
```

---

## 📑 Планы / улучшения

* Добавить авторизацию (JWT или session).
* Возможность редактирования записей через фронтенд.
* Перейти на PostgreSQL (если используется SQLite).
* Написать тесты (pytest + DRF test client).

---
