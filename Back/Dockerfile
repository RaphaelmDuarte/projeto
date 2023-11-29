FROM python:3.8-slim
WORKDIR /app
COPY /src /app/
COPY /requirements.txt /app/
RUN apt-get update \
    && apt-get install -y postgresql postgresql-contrib libpq-dev \
    && apt-get install -y build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]