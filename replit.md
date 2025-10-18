# Django Movie Management System

## Overview
This is a Django-based movie management web application that allows users to manage movies, directors, actors, and censor information. The project includes user authentication (signup, signin, logout) and full CRUD operations for movie-related data.

## Project Structure
The repository contains two Django projects:
- **Project_Sample/first_project** - A simpler Django project with student/teacher modules (uses SQLite)
- **second_project** - The main movie management system (currently active)

## Current State
The project has been successfully configured to run in the Replit environment with the following setup:
- Django 5.2.7 running on Python 3.11
- Database: SQLite (switched from PostgreSQL for Replit compatibility)
- Server: Development server on port 5000 (0.0.0.0:5000)
- Deployment: Configured with Gunicorn for production autoscale deployment

## Recent Changes (October 18, 2025)
1. Installed Django, Pillow, psycopg2-binary, and Gunicorn
2. Configured Django settings for Replit environment:
   - Set ALLOWED_HOSTS to ['*'] to work with Replit's proxy
   - Added CSRF_TRUSTED_ORIGINS for Replit domains
   - Switched database from PostgreSQL to SQLite
3. Applied all database migrations successfully
4. Created .gitignore file for Python/Django projects
5. Configured workflow to run Django development server on port 5000
6. Configured deployment with Gunicorn for production

## Tech Stack
- **Framework**: Django 5.2.7
- **Language**: Python 3.11
- **Database**: SQLite
- **Frontend**: HTML, CSS, Bootstrap 5
- **Media Handling**: Django File Uploads (Pillow for image processing)
- **Authentication**: Django built-in authentication
- **Deployment**: Gunicorn WSGI server

## Features
- User authentication (signup, signin, logout)
- Movie management (add, edit, delete, list)
- Director management
- Actor management
- Censor board information management
- Responsive Bootstrap 5 UI
- Media upload support for movie thumbnails

## Running the Application
The application is configured to run automatically via the workflow:
- Development: `python manage.py runserver 0.0.0.0:5000` (DEBUG=True)
- Production: Gunicorn WSGI server with autoscale deployment (DEBUG=False)

## Environment Variables

### Development
The application runs in development mode by default with DEBUG=True and uses a default SECRET_KEY.

### Production Deployment
**IMPORTANT**: Before deploying to production, you MUST configure SECRET_KEY in Replit Secrets:

1. Generate a secure secret key by running:
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

2. Add the generated key to Replit Secrets:
   - Open the "Secrets" tab (lock icon in the sidebar)
   - Add a new secret: `SECRET_KEY` = (paste the generated key)

3. The deployment is already configured to run with DEBUG=False

**Note**: The application will intentionally fail to start in production if SECRET_KEY is not set. This is a security feature to prevent accidental production deployment with insecure settings.

## Database Models
- **Movie**: Title, description, release date, rating, thumbnail
- **Director**: Name and bio
- **Actor**: Name and bio
- **CensorInfo**: Rating and certificate details

## Project Architecture
The main project (`second_project`) follows Django's MVT pattern:
- **Models**: Database structure in `movies/models.py`
- **Views**: Business logic in `movies/views.py`
- **Templates**: HTML templates in `template/` directory
- **Static Files**: CSS, images in `static/` directory
- **Media Files**: Uploaded content in `media/` directory
