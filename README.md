# User Authentication Django App

## Overview
This Django project provides user authentication functionality using a custom login decorator. It allows users to log in and access protected views within the application.

## Features
- User registration
- User login/logout
- Custom login decorator to protect views

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations to create the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
1. Register a new user by accessing `/signup` endpoint.
2. Log in with the registered user credentials at `/login`.
3. Access protected views by decorating them with `@login_required` decorator.

## Docker Integration
This project includes Docker support for easy deployment.

### Building the Docker Image
1. Make sure Docker is installed on your system.
2. Build the Docker image using the provided Dockerfile:
    ```bash
    docker build -t user_auth .
    ```

### Running the Docker Container
Run the Docker container with the following command:
```bash
docker run -d -p 8000:8000 user_auth
