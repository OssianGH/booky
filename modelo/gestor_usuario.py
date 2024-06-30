import pickle
from modelo.usuario import Usuario


class GestorUsuario:
    usuarios: list[Usuario] = []

    @staticmethod
    def agregar(usuario):
        GestorUsuario.usuarios.append(usuario)

    @staticmethod
    def eliminar(index):
        GestorUsuario.usuarios.pop(index)

    @staticmethod
    def index(cedula):
        for i, usuario in enumerate(GestorUsuario.usuarios):
            if usuario.cedula == cedula:
                return i
        raise ValueError(f"No se ha encontrado un usuario con cedula {cedula}.")

    @staticmethod
    def l_usuarios(query=""):
        return [
            usuario
            for usuario in GestorUsuario.usuarios
            if usuario.cedula.startswith(query)
        ]

    @staticmethod
    def proveedores(query=""):
        return [
            usuario
            for usuario in GestorUsuario.usuarios
            if usuario.tipo == Usuario.Tipo.proveedor
            and usuario.cedula.startswith(query)
        ]

    @staticmethod
    def clientes(query=""):
        return [
            usuario
            for usuario in GestorUsuario.usuarios
            if usuario.tipo == Usuario.Tipo.cliente and usuario.cedula.startswith(query)
        ]

    @staticmethod
    def grabar_datos():
        with open("./modelo/usuarios.dat", "wb") as out_file:
            pickle.dump(GestorUsuario.usuarios, out_file)
            out_file.flush()
            out_file.close()

    @staticmethod
    def cargar_datos():
        with open("./modelo/usuarios.dat", "rb") as in_file:
            GestorUsuario.usuarios = pickle.load(in_file)
            in_file.close()
