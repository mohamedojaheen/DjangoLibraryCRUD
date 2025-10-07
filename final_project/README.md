# Django Project – Library System

## Project Overview

This is a simple web application built with Django.
It demonstrates the use of models, views, templates, forms, and the Django admin panel.

The project implements a Library System with two related models:

- **Author** (name, birth year)
- **Book** (title, price, publication date, author)

Users can:

- View all books (homepage)
- View details about a single book
- Add new books through a form
- Add authors through a form if you enter admin credentials
- Manage authors and books via the Django Admin panel

-----

## Modules Explanation

- **models.py** → Defines the data structure (Author, Book)
- **views.py** → Business logic (list books, show details, handle form)
- **forms.py** → `BookForm` for creating new books
- **urls.py** (in `final_project/`) → Routes URLs to views
- **templates/** → HTML templates using Django template tags
- **admin.py** → Registers models for the Django admin interface

-----

## Requirements Coverage

- Django framework used
- Two models with relationship (Book ↔ Author)
- Models include `CharField`, `IntegerField`, `DecimalField`, `DateField`
- Three pages: homepage, details, form
- Templates with `{% for %}`, `{{ variable }}`, `{% if %}`
- `base.html` with inheritance
- Models registered in admin

-----

## Features

### Homepage (`http://127.0.0.1:8000/`)

- Displays a list of all books
- Each book shows its **title**, **author**, and **price**
- Links to each book’s details page

### Book Details Page (`/book/<id>/`)

- Shows more information about a selected book
- Includes **title**, **author**, **price**, and **publication date** (if available)

### Add Book Page (`/add/`)

- Allows adding a new book through a form
- Dropdown to select an existing author
- Date format: `YYYY-MM-DD` (for example, `2025-08-20`)

### Add Author Page (`/add_author/`)

- Login with superuser credentials to add authors
- Allows adding a new author through a form
- Have to reauthenticate everytime you add new author
- Prevent URL Tampering to skip authentication

### Admin Panel (`/admin/`)

- Manage authors and books
- Requires logging in with superuser credentials
- Create authors here before adding books

-----

## Project Structure

```text
final_project/
│
├── final_project/          # Main project folder (settings, urls, etc.)
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── library/                    # Django app for the library system
│   ├── models.py               # Defines Author and Book models
│   ├── views.py                # Contains logic for homepage, details, and add-book form
│   ├── forms.py                # Defines BookForm for adding new books
│   ├── templates/library/      # HTML templates
│   │   ├── base.html           # Base layout
│   │   ├── home.html           # Homepage (list of books)
│   │   ├── book_detail.html    # Detail page for a book
│   │   ├── add_author.html     # Form Page to add new author
│   │   ├── reauthenticate.html # Authentication Page for adding author
│   │   └── add_book.html       # Form page to add a new book
│   └── admin.py                # Registers models for Django Admin
│
└── manage.py                   # Django project manager
```

-----

## Installation & Setup

### 1\. Clone or Download the Project

```bash
git clone <repo-url>
cd final_project
```

### 2\. Create a Virtual Environment (recommended)

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate # Linux/Mac
```

### 3\. Install Dependencies

```bash
pip install django
```

### 4\. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5\. Create a Superuser (for admin access)

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username and password.

### 6\. Run the Development Server

```bash
python manage.py runserver
```

Open the site at: `http://127.0.0.1:8000/`

-----

## How to Test

1. Start server:

```bash
python manage.py runserver
```

2. Go to homepage → books list should appear (empty if none exist).
3. Go to `/admin/` → login with superuser → add authors.
4. Go to `/add/` → add new books linked to authors.
5. Go to `/book/<id>/` → confirm book details page works.
6. Delete a book in admin → check homepage updates automatically.

-----

## Notes

- Authors must be created before adding books
- Works with Django version **4.0** and above
