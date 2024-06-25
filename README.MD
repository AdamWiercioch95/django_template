# Django Template

## Introduction
This project is a template for a Django application that can be used as a base for new projects. It includes basic configurations and sample files to facilitate a quick start.

## Prerequisites
- Python 3.8 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- Virtual environment (optional, but recommended)

## How to Run the Project?

### 1. Create a New Project Directory
1. Create a new directory for your project and navigate to it:
    ```bash
    mkdir myproject
    cd myproject
    ```

### 2. Set Up the Virtual Environment and Install Django
1. Create a virtual environment and install Django using Poetry:
    ```bash
    poetry init -n
    poetry add django
    ```

### 3. Set Up the Django Project
1. Set up your project using the copied template URL:
    ```bash
    django-admin startproject project_name . --template https://github.com/AdamWiercioch95/django_template/archive/refs/heads/template.zip
    ```
    Replace `project_name` with the desired name for your project.

### 4. Install Dependencies
1. Use Poetry to install the project dependencies:
    ```bash
    poetry install
    ```

### 5. Open the Project
1. Open your project in your preferred code editor.


### 6. Configure Environment Files
1. Navigate to the `env` directory and create a `.env` file based on the `.env-default` file:
    ```bash
    cp env/.env-default env/.env
    ```
2. Edit the `env/.env` file to fit your environment (e.g., database settings, API keys, etc.).

### 7. Adjust Test Configurations
1. Open the `pytest.ini` file and replace `{{ project_name }}` with your project name:
    ```ini
    [pytest]
    DJANGO_SETTINGS_MODULE = {{ project_name }}.settings
    ```
    For example, if your project name is `myproject`, it should be:
    ```ini
    [pytest]
    DJANGO_SETTINGS_MODULE = myproject.settings
    ```

## Additional Information
- To run the Django development server, use:
    ```bash
    poetry run python manage.py runserver
    ```
- To run tests, use:
    ```bash
    poetry run pytest
    ```

## Useful Links
- [Django Documentation](https://docs.djangoproject.com/)
- [Poetry Documentation](https://python-poetry.org/docs/)
