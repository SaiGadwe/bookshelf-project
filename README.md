# 📚 BookShelf

A Django web app where logged-in users can add, view, edit, and delete books.

## Features

- 🔐 Login-protected book list
- ➕ Add new books
- ✏️ Edit existing books
- 🗑️ Delete books
- 🎨 Styled with custom CSS

## Setup

```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and log in with the superuser account you created.

## Project structure

```
bookshelf_day1/
├── manage.py
├── requirements.txt
├── bookshelf_project/      # settings, root urls
└── books/                  # the app
    ├── models.py           # Book model
    ├── forms.py            # BookForm
    ├── views.py             # list, add, edit, delete, logout
    ├── urls.py
    ├── static/books/style.css
    └── templates/
        ├── books/
        └── registration/
```

## Routes

| URL | Description |
|---|---|
| `/` | List all books |
| `/add/` | Add a new book |
| `/edit/<id>/` | Edit a book |
| `/delete/<id>/` | Delete a book (with confirmation) |
| `/login/` | Login page |
| `/logout/` | Logout |
| `/admin/` | Django admin |
