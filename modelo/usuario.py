class Usuario:
    def __init__(self, cedula, nombre, direccion, telefono, correo, tipo):
        self.cedula = cedula
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.tipo = tipo

    class Tipo:
        proveedor = 1
        cliente = 2
