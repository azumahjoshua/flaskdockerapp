# Use Python 3.9 as the base image
FROM python:3.9-slim-buster

WORKDIR /app

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
