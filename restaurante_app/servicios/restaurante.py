from typing import List, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self):
        self._productos: List[Producto] = ArchivoServicio.cargar_productos()
        self._usuarios: List[Usuario] = ArchivoServicio.cargar_usuarios()
        self._ventas: List[Venta] = ArchivoServicio.cargar_ventas()

    # --- GESTIÓN DE PRODUCTOS ---
    def agregar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        ArchivoServicio.guardar_productos(self._productos)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def listar_productos(self) -> List[Producto]:
        return self._productos

    # --- GESTIÓN DE USUARIOS ---
    def agregar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        ArchivoServicio.guardar_usuarios(self._usuarios)
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for u in self._usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def listar_usuarios(self) -> List[Usuario]:
        return self._usuarios

    # --- OPERACIÓN PRINCIPAL: VENDER PRODUCTO ---
    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> tuple[bool, str]:
        usuario = self.buscar_usuario(identificacion_usuario)
        if usuario is None:
            return False, "Error: El usuario no existe."

        producto = self.buscar_producto(codigo_producto)
        if producto is None:
            return False, "Error: El producto no existe."

        if cantidad <= 0:
            return False, "Error: La cantidad solicitada debe ser mayor a cero."

        if producto.stock < cantidad:
            return False, f"Error: Stock insuficiente. Stock disponible: {producto.stock}."

        # Ejecución de la regla de negocio
        try:
            producto.vender(cantidad)
            venta = Venta(usuario.identificacion, producto.codigo, cantidad)
            self._ventas.append(venta)

            # Persistencia de ambas colecciones modificadas
            ArchivoServicio.guardar_ventas(self._ventas)
            ArchivoServicio.guardar_productos(self._productos)
            return True, "Venta realizada con éxito."
        except ValueError as e:
            return False, f"Error en la venta: {e}"

    def obtener_ventas_por_usuario(self, identificacion_usuario: str) -> List[dict]:
        ventas_usuario: List[dict] = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                producto = self.buscar_producto(venta.producto_codigo)
                nombre_prod = producto.nombre if producto else "Producto desconocido"
                precio_prod = producto.precio if producto else 0.0
                
                # Se calcula la multiplicación directamente sin usar ':='
                ventas_usuario.append({
                    "codigo_producto": venta.producto_codigo,
                    "nombre_producto": nombre_prod,
                    "cantidad": venta.cantidad,
                    "subtotal": venta.cantidad * precio_prod
                })
        return ventas_usuario