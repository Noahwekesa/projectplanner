# Project Planner

A Django-based Project Management System

## Introduction

This project is a project management system built using the Django web framework. It allows users to create, manage, and track their projects, tasks, and deadlines.

### Features:

- Create and manage projects with detailed descriptions.
- Define tasks for each project with deadlines and assign them to users (if applicable).
- Track the progress of tasks and mark them as completed.
- User management system for team collaboration.

## Installation

- installation to run it locally

### Prerequisites:

- Python (version 3.x recommended)
- pip (Python package installer)
- A database management system (e.g., PostgreSQL, MySQL)

### Steps:

1. Clone Repository

```bash

git clone https://github.com/Noahwekesa/projectplanner.git
```

2. Navigate to the project dir

```bash

cd projectplanner
```

3. Create a virtual environment(recommended)

```bash

python -m venv venv

source venv/bin/activate

```

4. Install dependencies

```bash

pip install -r requirements.txt
```

5. Create a local database and configure database settings in `settings.py`.

6. Apply database migrations:

```bash

python manage.py makemigrations

python manage.py migrate
```

7. Run the development server

```bash

python manage.py runserver
```

8. run tailwind server

```bash
python manage.py tailwind start

```

### Author(s):

[Noah wekesa LinkedIn](www.linkedin.com/in/noah-wekesa-4a375815a)
