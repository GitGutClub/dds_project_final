FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

# Собираем статику для админки
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "dds_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
