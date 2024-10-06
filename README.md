# Django Project with Store and Order Apps

This is a basic Django project that contains two applications: `store` and `order`. Each app has two views: `index` and `about`.

## Project Structure




## Installation

1. Clone the repository:

    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Applications

### 1. `store`

- **Index View**: Displays "Store index page".
- **About View**: Displays "Store about page".

### 2. `order`

- **Index View**: Displays "Order index page".
- **About View**: Displays "Order about page".

## URLs

- `/store/`: Access the store's index page.
- `/store/about/`: Access the store's about page.
- `/order/`: Access the order's index page.
- `/order/about/`: Access the order's about page.

## License

This project is licensed under the MIT License.
