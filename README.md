# Library Management System

A Django-based library management system for managing books, students, and book issuance.

![developer](https://img.shields.io/badge/Developed%20By%20%3A-Sumit%20Kumar-red)

---

## Features

### Admin Features
- Create Admin account and Login...
- Add, View, and Delete Books
- Issue Books to registered students
- View Issued books with issued date and expiry date
- View Fine (10 rupees for each day after expiry date)
- View Students registered in the system

### Student Features
- Create account and Login
- View issued books with expiry date and fine (if any, otherwise 0)

---

## Screenshots

### Homepage
![homepage snap](./static/screenshots/homepage.png)

### Admin Dashboard
![dashboard snap](./static/screenshots/adminhomepage.png)

### Available Books
![available book snap](./static/screenshots/availablebook.png)

### Issue Book
![issue book snap](./static/screenshots/issuebook.png)

### Issued Book
![issued book snap](./static/screenshots/bookissued.png)

---

## Requirements

- Python 3.8 or higher
- Django 5.1.5

---

## HOW TO RUN THIS PROJECT

### Step 1: Clone the Repository

```
bash
git clone <repository-url>
cd librarymanagement-master
```

### Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other Python projects.

**Windows:**
```
bash
python -m venv venv
```

**macOS/Linux:**
```
bash
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment

**Windows:**
```
bash
.\venv\Scripts\activate
```

**macOS/Linux:**
```
bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```
bash
pip install -r requirements.txt
```

### Step 5: Run Migrations

```
bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser (Optional)

To access the admin panel, create a superuser account:

```
bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin credentials.

### Step 7: Run the Development Server

```
bash
python manage.py runserver
```

### Step 8: Access the Application

Open your web browser and navigate to:

```
http://127.0.0.1:8000/
```

---

## Configuration

### Email Setup (For Contact Us Page)

In `librarymanagement/settings.py`, update the email settings with your credentials:

```
python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
EMAIL_RECEIVING_USER = 'your-email@gmail.com'
```

**Note:** If using Gmail, you need to generate an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.

### Changing Secret Key (Recommended for Production)

In `librarymanagement/settings.py`, change the `SECRET_KEY`:

```
python
SECRET_KEY = 'your-new-secret-key'
```

### Setting DEBUG Mode

For production, set `DEBUG = False` in `settings.py` and add your domain to `ALLOWED_HOSTS`:

```
python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

---

## Project Structure

```
librarymanagement-master/
├── library/                  # Main Django app
│   ├── migrations/          # Database migrations
│   ├── admin.py            # Admin configuration
│   ├── models.py           # Database models
│   ├── views.py            # Views
│   └── ...
├── librarymanagement/       # Django project settings
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL configurations
│   └── ...
├── templates/              # HTML templates
├── static/                # Static files (CSS, JS, images)
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

---

## Troubleshooting

### Port Already in Use
If port 8000 is already in use, specify a different port:
```
bash
python manage.py runserver 8080
```

### Database Issues
If you encounter database issues, you can reset the database:
```
bash
python manage.py flush
python manage.py migrate
```

---

## Credits

Developed by Sumit Kumar

---

## Feedback

Any suggestions and feedback are welcome!
- [Contact on Facebook](https://fb.com/sumit.luv)
- [Subscribe my Channel LazyCoder On Youtube](https://youtube.com/lazycoders)
