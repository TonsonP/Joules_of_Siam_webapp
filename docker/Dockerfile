# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Django development server port
EXPOSE 8000

# For production
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# For development
CMD ["tail", "-f", "/dev/null"]
