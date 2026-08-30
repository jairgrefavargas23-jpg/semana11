class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor a cero.")

        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    def a_diccionario(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Venta":
        try:
            return cls(
                usuario_id=str(datos["usuario_id"]),
                producto_codigo=str(datos["producto_codigo"]),
                cantidad=int(datos["cantidad"])
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave requerida en Venta: {e}")