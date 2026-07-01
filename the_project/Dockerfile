FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY . .

CMD ["sh", "-c", "uvicorn todo_app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]