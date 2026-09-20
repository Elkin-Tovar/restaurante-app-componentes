class Venta:
    """
    Clase que representa la operación de venta que relaciona un usuario con un producto.
    """

    def __init__(
        self,
        usuario_id: str,
        producto_codigo: str,
        cantidad: int
    ) -> None:
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        if cantidad <= 0:
            raise ValueError("La cantidad de venta debe ser mayor a cero.")
        self.cantidad = cantidad

    def mostrar_informacion(self) -> str:
        """
        Retorna la información general de la venta.
        """
        return (
            f"Usuario ID: {self.usuario_id} | "
            f"Producto Código: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )

    def a_diccionario(self) -> dict:
        """
        Convierte el objeto Venta en un diccionario para su almacenamiento en JSON.
        """
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }