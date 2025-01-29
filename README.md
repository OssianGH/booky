# Booky

Booky is a Python-based application for managing a bookstore. It provides functionalities for managing books, customers, suppliers, transactions, and reports  . The application uses PyQt6 for the graphical user interface.

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
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
    ```sh
    pip install PyQt6
    ```

## Usage

To run the application, execute the following command:
```sh
python main.py
```

## Modules

### Controller

- `controlador/`: Contains the controller classes that handle the business logic and user interactions.

**General**

- `controlador/principal.py`: The main controller of the application, managing the dashboard to access its functionalities.
- `controlador/detalle.py`: Handles the detailed display of a specific invoice.
- `controlador/transacciones.py`: Handles the detailed display of transactions performed with a specific book.
- `controlador/negocio.py`: Provides the base functionality for managing business transactions
- `controlador/abastecimiento.py`: Extends `controlador/negocio.py` functionality to handle the supply management process.
- `controlador/venta.py`: Extends `controlador/negocio.py` functionality to handle the sales process.

**Books**

- `controlador/alterar_libro.py`: Provides the base functionality required for both adding and editing books.
- `controlador/agregar_libro.py`: Extends `controlador/alterar_libro.py` functionality to handle adding new books.
- `controlador/editar_libro.py`: Extends `controlador/alterar_libro.py` functionality to handle editing book details.
- `controlador/select_libro.py`: Handles the detailed display of the books and their selection.
- `controlador/ver_libro.py`: Handles the viewing of details for a specific book.

**Users**

- `controlador/alterar_usuario.py`: Provides the base functionality required for both adding and editing users (customers or suppliers).
- `controlador/agregar_cliente.py`: Extends `controlador/alterar_usuario.py` functionality to handle adding new customers.
- `controlador/agregar_proveedor.py`: Extends `controlador/alterar_usuario.py` functionality to handle adding new suppliers.
- `controlador/editar_usuario.py`: Extends `controlador/alterar_usuario.py` functionality to handle editing user (customers or suppliers) information.
- `controlador/select_usuario.py`: Handles the detailed display of the users and their selection.
- `controlador/select_proveedor.py`: Extends `controlador/select_usuario.py` functionality to be specific to suppliers.

### Model

- `modelo/`: Contains the model classes that represent the data and handle data operations.

**General**

- `modelo/transaccion`: Represents a transaction (either a sale or a supply).
- `modelo/factura.py`: Represents an invoice.
- `modelo/ranura_factura.py`: Represents an item in an invoice.
- `modelo/gestor_factura.py`: Manages the collection of `Factura` objects.

**Books**

- `modelo/libro.py`: Represents a book.
- `modelo/gestor_libro.py`: Manages the collection of `Libro` objects.

**Users**

- `modelo/usuario.py`: Represents a user (either a customer or a supplier).
- `modelo/gestor_usuario.py`: Manages the collection of `Usuario` objects.

### View

- `vista/`: Contains the view classes that define the GUI components.
