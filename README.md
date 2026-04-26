# Portfolio Website

A personal portfolio website built with Django.

## Features

- Home, About, Experience, Skills, Projects, Contact pages
- Admin panel for easy content management
- Full authentication system
- Responsive design
- Dark theme

## Setup

1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create `.env` file with your email credentials
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
7. Run server:
   ```bash
   python manage.py runserver
   ```

## Admin Access

URL: `/admin/`