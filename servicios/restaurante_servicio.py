from typing import List, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """
    Servicio que administra la lógica de negocio, procesamiento de datos,
    validaciones y persistencia para la interfaz gráfica.
    """

    def __init__(self) -> None:
        self.archivo_servicio = ArchivoServicio()
        self.productos: List[Producto] = self.archivo_servicio.cargar_productos()
        self.usuarios: List[Usuario] = self.archivo_servicio.cargar_usuarios()

    def validar_acceso(self, usuario: str, clave: str) -> bool:
        """
        Valida el acceso buscando si el usuario ingresado existe 
        dentro de la lista cargada desde usuarios.json.
        """
        if not usuario.strip() or not clave.strip():
            return False
        
        # Opcional para pruebas: un acceso maestro de respaldo
        if usuario == "admin" and clave == "1234":
            return True

        # Verifica si el texto ingresado coincide con la identificación o el nombre de algún usuario del JSON
        for u in self.usuarios:
            if u.identificacion.strip() == usuario.strip() or u.nombre.lower().strip() == usuario.lower().strip():
                # Nota: Como el JSON de usuarios por defecto no tiene campo de contraseña, 
                # con que el usuario exista en el archivo se le permite el acceso.
                return True
                
        return False

    def obtener_productos(self) -> List[Producto]:
        return self.productos

    def obtener_usuarios(self) -> List[Usuario]:
        return self.usuarios

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> bool:
        if not codigo or not nombre:
            return False
        if self.buscar_producto(codigo) is not None:
            return False  # Ya existe
        if precio < 0 or stock < 0:
            return False
        nuevo_prod = Producto(codigo, nombre, categoria, precio, stock)
        self.productos.append(nuevo_prod)
        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        if precio < 0 or stock < 0:
            return False
        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock
        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        self.productos.remove(producto)
        self.archivo_servicio.guardar_productos(self.productos)
        return True