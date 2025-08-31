FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код и базу данных
COPY ./app ./app
COPY check.db ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
