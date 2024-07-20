# Используем официальный образ Python в качестве базового
FROM python:3.11

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt requirements.txt

# Устанавливаем зависимости из requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект в рабочую директорию
COPY . .

# Открываем порт для доступа к приложению
EXPOSE 8000

# Команда для запуска Django-приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myshop.wsgi:application"]
