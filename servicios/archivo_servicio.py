import json
import os
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario


class ArchivoServicio:
    """
    Servicio encargado de leer y escribir los datos locales en archivos JSON.
    """

    def __init__(self) -> None:
        self.dir_datos = "datos"
        self._asegurar_directorio()

    def _asegurar_directorio(self) -> None:
        if not os.path.exists(self.dir_datos):
            try:
                os.makedirs(self.dir_datos)
            except PermissionError:
                pass

    def cargar_productos(self, ruta: str = "datos/productos.json") -> List[Producto]:
        productos = []
        if not os.path.exists(ruta):
            return productos
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
                if not isinstance(data, list):
                    return []
                for item in data:
                    try:
                        productos.append(Producto(
                            item["codigo"],
                            item["nombre"],
                            item["categoria"],
                            float(item["precio"]),
                            int(item["stock"])
                        ))
                    except (KeyError, ValueError, TypeError):
                        continue
        except (json.JSONDecodeError, PermissionError):
            pass
        return productos

    def guardar_productos(self, productos: List[Producto], ruta: str = "datos/productos.json") -> None:
        try:
            data = [p.a_diccionario() for p in productos]
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(data, archivo, indent=4, ensure_ascii=False)
        except PermissionError:
            pass

    def cargar_usuarios(self, ruta: str = "datos/usuarios.json") -> List[Usuario]:
        usuarios = []
        if not os.path.exists(ruta):
            return usuarios
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
                if not isinstance(data, list):
                    return []
                for item in data:
                    try:
                        usuarios.append(Usuario(
                            item["identificacion"],
                            item["nombre"],
                            item["correo"]
                        ))
                    except (KeyError, ValueError, TypeError):
                        continue
        except (json.JSONDecodeError, PermissionError):
            pass
        return usuarios