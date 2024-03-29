# Use an official Python runtime as the base image
FROM python:3.9-slim
EXPOSE 8000
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Collect static files
# RUN python manage.py

# Run the Django application
CMD ["python", "./manage.py","runserver","0.0.0.0:8000"]
