FROM python:3.13-slim

WORKDIR /code

COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]