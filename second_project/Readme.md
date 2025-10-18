🎬 Movie Sample Django Project

This project was built as part of  learning portfolio to explore Django’s MVC (Model–View–Template) pattern and full-stack web development.

It demonstrates how to design a complete movie management system — including user authentication, data management, PostgreSQL database integration, and a responsive Bootstrap-based interface.

🚀 Features

🔐 User Signup, Signin & Logout (Authentication)

🎥 Movie management: Add, Edit, Delete, and List Movies

👨‍💼 Manage Directors, Actors, and Censor Board Info

🧾 Dynamic data storage using PostgreSQL

🖼️ Media upload support (e.g., movie posters)

🧱 Django Models, Forms, Views, Templates, and URL routing

💬 Smart Bootstrap 5 menu that adapts to login status

📱 Fully responsive UI for desktop and mobile

🧩 Entity Relationship (ER) Overview


 ┌────────────┐        ┌─────────────┐
 │   Movie    │◄──────►│  Director   │
 └────────────┘        └─────────────┘
       ▲                     ▲
       │                     │
       │                     │
       ▼                     ▼
 ┌────────────┐        ┌─────────────┐
 │   Actor    │        │ CensorInfo  │
 └────────────┘        └─────────────┘

Relationships

Each Movie is associated with one or more Actors

Each Movie has one Director

Each Movie has related CensorInfo (rating, certificate, etc.)

🗃️ Database Configuration (PostgreSQL)

Configured in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_db',
        'USER': 'irshad',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

🧱 Models Example
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='posters/')

🧾 Forms

Uses Django’s ModelForm for clean form-to-model mapping:

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


🌐 Views Overview
View Name	Description
index()	Home page showing all movies
create()	Add a new movie
edit()	Edit an existing movie
delete()	Delete a movie
list()	Show list of movies
director(), actor(), censor_info()	Manage related data
signup(), signin(), signout()	Handle authentication


🎨 Templates

menu.html – Responsive Bootstrap navbar

index.html – Homepage showing all movies

create.html – Movie creation/editing form

list.html – Displays all movies

director.html, actor.html, censor_info.html – CRUD templates

user_signup.html, user_signin.html – Auth pages

base.html – Shared layout


🛠️ Tech Stack
Component	Technology
Framework	Django 5.2.6
Language	Python 3.12
Database	PostgreSQL
Frontend	HTML, CSS, Bootstrap 5
Auth System	Django built-in authentication
Media	Django File Uploads (MEDIA_URL / MEDIA_ROOT)



👨‍💻 Author

Irshad
💼 Django Developer | Python Enthusiast
📧 irshad2934@gmail.com
