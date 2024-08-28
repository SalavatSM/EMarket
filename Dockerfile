# Базовый образ Python 3.9
FROM python:3.9-slim

# Устанавливаем переменную окружения для отключения буферизации вывода Python
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости из файла requirements.txt
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Запускаем сервер через Gunicorn при старте контейнера
CMD ["gunicorn", "--bind", ":8000", "test_project.wsgi:application"]
