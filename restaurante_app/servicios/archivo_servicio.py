import json
import os
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class ArchivoServicio:
    RUTA_DATOS = "datos"

    @classmethod
    def _obtener_ruta(cls, nombre_archivo: str) -> str:
        if not os.path.exists(cls.RUTA_DATOS):
            os.makedirs(cls.RUTA_DATOS)
        return os.path.join(cls.RUTA_DATOS, nombre_archivo)

    # --- PERSISTENCIA DE PRODUCTOS ---
    @classmethod
    def guardar_productos(cls, productos: List[Producto]) -> None:
        ruta = cls._obtener_ruta("productos.json")
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump([p.a_diccionario() for p in productos], f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: Permiso denegado al intentar guardar productos.json.")

    @classmethod
    def cargar_productos(cls) -> List[Producto]:
        ruta = cls._obtener_ruta("productos.json")
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Producto.desde_diccionario(p) for p in datos]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: productos.json contiene un formato inválido. Iniciando lista vacía.")
            return []
        except (KeyError, ValueError) as e:
            print(f"Error al reconstruir objetos de productos: {e}")
            return []

    # --- PERSISTENCIA DE USUARIOS ---
    @classmethod
    def guardar_usuarios(cls, usuarios: List[Usuario]) -> None:
        ruta = cls._obtener_ruta("usuarios.json")
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump([u.a_diccionario() for u in usuarios], f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: Permiso denegado al intentar guardar usuarios.json.")

    @classmethod
    def cargar_usuarios(cls) -> List[Usuario]:
        ruta = cls._obtener_ruta("usuarios.json")
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Usuario.desde_diccionario(u) for u in datos]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: usuarios.json contiene un formato inválido. Iniciando lista vacía.")
            return []
        except (KeyError, ValueError) as e:
            print(f"Error al reconstruir objetos de usuarios: {e}")
            return []

    # --- PERSISTENCIA DE VENTAS ---
    @classmethod
    def guardar_ventas(cls, ventas: List[Venta]) -> None:
        ruta = cls._obtener_ruta("ventas.json")
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump([v.a_diccionario() for v in ventas], f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: Permiso denegado al intentar guardar ventas.json.")

    @classmethod
    def cargar_ventas(cls) -> List[Venta]:
        ruta = cls._obtener_ruta("ventas.json")
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Venta.desde_diccionario(v) for v in datos]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: ventas.json contiene un formato inválido. Iniciando lista vacía.")
            return []
        except (KeyError, ValueError) as e:
            print(f"Error al reconstruir objetos de ventas: {e}")
            return []