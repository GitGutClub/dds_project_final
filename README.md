# 📌 DDS — Управление движением денежных средств

Веб-приложение для учёта и анализа движения денежных средств (ДДС).  
Стек: **Django + Django REST Framework (backend)**, **React (frontend)**, **PostgreSQL (БД)**, **Nginx (реверс-прокси)**, **Docker Compose** для контейнеризации.

---

## 🚀 Возможности

- ✅ CRUD-операции с движениями (доходы/расходы).  
- ✅ Справочники: Типы, Статусы, Категории, Подкатегории.  
- ✅ Фильтрация по датам, типам, категориям, статусам.  
- ✅ React SPA с интеграцией через REST API.  
- ✅ Django Admin для управления данными.  
- ✅ Автоматическая подстановка текущей даты при создании записи (если не указана).  
- ✅ Nginx обслуживает как API, так и статику фронтенда/бэкенда.  

---

## 📂 Структура проекта

```
.
├── backend/              # Django backend (API + Admin)
│   ├── dds_project/      # Django проект
│   ├── dds_app/          # Основное приложение (модели, сериализаторы, viewsets)
│   ├── staticfiles/      # Скомпилированная статика Django
│   └── Dockerfile
│
├── frontend/             # React frontend (SPA)
│   ├── src/              # Компоненты React
│   ├── build/            # Сборка (генерируется `npm run build`)
│   └── Dockerfile
│
├── nginx/                # Конфиги nginx
│   └── nginx.conf
│
├── docker-compose.yml
└── README.md             # Этот файл 🙂
```

---

## ⚙️ Требования

- [Docker](https://www.docker.com/) ≥ 20.10  
- [Docker Compose](https://docs.docker.com/compose/) ≥ 2.0  

---

## 🔧 Локальный запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/yourusername/dds.git
cd dds
```

### 2. Построить и запустить контейнеры
```bash
docker compose up -d --build
```

> ⚠️ Если контейнеры уже существуют и возникают конфликты по именам:  
> ```bash
> docker rm -f dds_backend dds_frontend dds_nginx
> docker compose up -d --build
> ```

### 3. Проверить, что всё работает
- Django API: [http://localhost/api/](http://localhost/api/)  
- Django Admin: [http://localhost/admin/](http://localhost/admin/)  
- React SPA: [http://localhost/](http://localhost/)  

### 4. Создать суперпользователя Django (для админки)
```bash
docker exec -it dds_backend python manage.py createsuperuser
```

---

## 🛠 Основные команды

### Остановить проект
```bash
docker compose down
```

### Пересобрать проект (с очисткой кэша)
```bash
docker compose build --no-cache
docker compose up -d
```

### Просмотреть логи
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

## 🌍 Архитектура (схема)

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
 │ Django App  │ │ Gunicorn    │ │ PostgreSQL (?) │
 │ (backend)   │ │ (WSGI)      │ │ (БД)           │
 └─────────────┘ └─────────────┘ └────────────────┘
```

---

## 📑 TODO / Улучшения

- Добавить авторизацию (JWT или session).  
- Сделать редактирование записей на фронтенде (сейчас только через админку).  
- Подключить PostgreSQL вместо SQLite.  
- Тесты (pytest + DRF test client).  

---

## 👨‍💻 Автор

Проект разработан для управления личными финансами / корпоративного учёта.  
Можно использовать как основу для собственного финансового планировщика.  
