# TODO: Install the backend dependency package into the app folder inside the container.

FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Make sure the database file is accessible
RUN mkdir -p /app/data

# Default command
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]