# Café Reservation Website

A full-stack Django web application for reserving tables at a café.  
Users can book a table by selecting date, time, and number of guests.  
Admin can view, edit, and cancel reservations through the dashboard.

## Features
- Table reservation form (name, email, phone, date, time, guest count)  
- Admin dashboard to view, confirm, or cancel bookings  
- Django admin panel for managing reservations  
- Responsive design using Bootstrap  
- SQLite database for development

## Tech Stack
- Python 3.x
- Django 5.x
- Bootstrap 5
- SQLite3
- HTML/CSS

## How to Run Locally

### 1. Clone the repository
git clone https://github.com/your-username/cafe_reservation.git
cd cafe_reservation

shell
Copy
Edit

### 2. Create & activate virtual environment
python -m venv venv

vbnet
Copy
Edit
Activate:
- On Windows:
venv\Scripts\activate

diff
Copy
Edit
- On Mac/Linux:
source venv/bin/activate

shell
Copy
Edit

### 3. Install dependencies
pip install django

shell
Copy
Edit

### 4. Run migrations
python manage.py makemigrations
python manage.py migrate

shell
Copy
Edit

### 5. Run the development server
python manage.py runserver

markdown
Copy
Edit
Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Admin Panel
- Create a superuser:
python manage.py createsuperuser

less
Copy
Edit
- Visit: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Deployment (Render)

### 1. Create a Render account:
https://render.com/

### 2. Push your project to GitHub (see below)

### 3. In Render dashboard:
- Click New → Web Service
- Connect your GitHub repository
- Select:
  - Runtime: Python
  - Build Command:  
    ```
    pip install -r requirements.txt
    python manage.py migrate
    ```
  - Start Command:
    ```
    gunicorn cafe_reservation.wsgi:application
    ```
- Set environment variable:
SECRET_KEY = your_django_secret_key

shell
Copy
Edit
- Click Create Web Service
- Wait for it to build and your app will be live