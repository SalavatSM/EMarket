# Базовый образ Python 3.9
FROM python:3.9-slim-buster

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем только необходимые файлы проекта
COPY beam_prjct beam_prjct
COPY static static

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=beam_prjct.settings

# Запускаем сервер через Gunicorn при старте контейнера
CMD ["gunicorn", "--bind", ":8000", "beam_prjct.wsgi:application"]

