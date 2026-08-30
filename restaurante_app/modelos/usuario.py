class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str):
        if not identificacion or not nombre or not correo:
            raise ValueError("Todos los campos del usuario son obligatorios.")

        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Usuario":
        try:
            return cls(
                identificacion=str(datos["identificacion"]),
                nombre=str(datos["nombre"]),
                correo=str(datos["correo"])
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave requerida en Usuario: {e}")