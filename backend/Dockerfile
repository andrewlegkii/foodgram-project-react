# Build stage
FROM python:3.7-slim as build

WORKDIR /build

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# Production stage
FROM python:3.7-slim

WORKDIR /app

COPY --from=build /build .

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]
