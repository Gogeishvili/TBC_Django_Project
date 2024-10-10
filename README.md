# Django Project

This project consists of two main apps: **store** and **order**.

## Store App

### Models

- **Category**: Manages product categories with hierarchical relationships.
- **Product**: Represents products with an image and associated categories.

### URLs

- `/store/`: Home page
- `/store/product/info/`: Product information endpoint
- `/store/category/info/`: Category information endpoint

## Installation

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the server: `python manage.py runserver`.

