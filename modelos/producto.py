class Producto:
    """
    Clase que representa un producto del restaurante con su respectivo stock.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def a_diccionario(self) -> dict:
        """
        Convierte el objeto Producto en un diccionario para su almacenamiento en JSON.
        """
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }