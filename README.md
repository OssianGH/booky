# Booky

Tienda Libros is a Python-based application for managing a bookstore. It provides functionalities for managing books, customers, suppliers, transactions, and reports  . The application uses PyQt6 for the graphical user interface.

## Features

### Book, Customer and Supplier Management:

Add, edit, delete, and view books, customers and suppliers.

### Transactions:

Handle sales and purchases.

### Reports

Generate reports for sales and inventory.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/OssianGH/booky.git
    cd booky
    ```
2. Navigate to the project directory:
    ```sh
    cd booky
    ```
3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
5. Install the required dependencies:
    ```sh
    pip install PyQt6
    ```

## Usage

To run the application, execute the following command:
```sh
python main.py
```

## Code overview

### Controllers

- `principal.py`: The main controller of the application, managing the dashboard to access its functionalities.
- `alterar_libro.py`: Provides the base functionality required for both adding and editing books.
- `agregar_libro.py`: Extends `alterar_libro.py` functionality to handle adding new books.
- `editar_libro.py`: Extends `alterar_libro.py` functionality to handle editing book details.
- `select_libro.py`: Handles the detailed display of the books and their selection.
- `ver_libro.py`: Handles the viewing of details for a specific book.
- `alterar_usuario.py`: Provides the base functionality required for both adding and editing users (customers or suppliers).
- `agregar_cliente.py`: Extends `alterar_usuario.py` functionality to handle adding new customers.
- `agregar_proveedor.py`: Extends `alterar_usuario.py` functionality to handle adding new suppliers.
- `editar_usuario.py`: Extends `alterar_usuario.py` functionality to handle editing user (customers or suppliers) information.
- `select_usuario.py`: Handles the detailed display of the users and their selection.
- `select_proveedor.py`: Extends `select_usuario.py` functionality to be specific to suppliers.
- `detalle.py`: Handles the detailed display of a specific invoice.
- `transacciones.py`: Handles the detailed display of transactions performed with a specific book.
- `negocio.py`: Provides the base functionality for managing business transactions
- `abastecimiento.py`: Extends `negocio.py` functionality to handle the supply management process.
- `venta.py`: Extends `negocio.py` functionality to handle the sales process.

### Models

Contains data models and business logic.

### Views

Contains the UI components and views.
