# Django-first
My effort on building a full-stack basic web application built with Python, Django, HTML, and CSS. With backend routing, views, and templates.

# Pyshop - an interface of a shopping page of products

## Stack

- Python 3 + Django 6
- Bootstrap 5 (via CDN)
- SQLite

## What's inside

A `pyshop` Django project with a `products` app. The products app has:

- A `Product` model
- An `index` view that lists all products
- A `new` view at `/products/new/`
- A `base.html` template using Bootstrap 5

## Running locally

```bash
python -m venv venv
source venv/bin/activate          # macOS / Linux
venv\Scripts\Activate.ps1         # Windows PowerShell
pip install django
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/products/

## What I'm learning next

Turning this into a proper, beautifully styled shop with product cards, a cart, and a real catalogue.
