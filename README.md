# DDS — Full Package (Django DRF + React SPA)

Содержит два варианта запуска:
1. Docker (docker-compose) — рекомендуемый для ревью/демо
2. Локальный — отдельный запуск backend и frontend

Содержание архива:
- backend/ — Django + DRF + fixtures, настроено на Postgres (docker) и SQLite (локально)
- frontend/ — React SPA (sources), npm scripts, Dockerfile для production
- docker-compose.yml — запускает backend, frontend (nginx), postgres
- READMEs внутри backend и frontend с инструкциями

Сначала прочитайте backend/README.md и frontend/README.md для детальных шагов.
