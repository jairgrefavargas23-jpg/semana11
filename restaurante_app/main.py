from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

def menu():
    print("\n" + "="*40)
    print("      SISTEMA RESTAURANTE APP (SEM 11)")
    print("="*40)
    print("1. Registrar Producto")
    print("2. Listar Productos")
    print("3. Registrar Usuario")
    print("4. Listar Usuarios")
    print("5. Realizar Venta")
    print("6. Consultar Ventas por Usuario")
    print("7. Salir")
    return input("Seleccione una opción: ")

def main():
    restaurante = Restaurante()

    while True:
        opcion = menu()

        if opcion == "1":
            print("\n--- REGISTRAR PRODUCTO ---")
            try:
                codigo = input("Código: ").strip()
                nombre = input("Nombre: ").strip()
                precio = float(input("Precio: "))
                stock = int(input("Stock inicial: "))

                prod = Producto(codigo, nombre, precio, stock)
                if restaurante.agregar_producto(prod):
                    print("✓ Producto registrado con éxito.")
                else:
                    print("✕ Error: Ya existe un producto con ese código.")
            except ValueError as e:
                print(f"✕ Error en el ingreso de datos: {e}")

        elif opcion == "2":
            print("\n--- LISTA DE PRODUCTOS ---")
            productos = restaurante.listar_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                for p in productos:
                    print(f"Código: {p.codigo} | Nombre: {p.nombre} | Precio: ${p.precio:.2f} | Stock: {p.stock}")

        elif opcion == "3":
            print("\n--- REGISTRAR USUARIO ---")
            try:
                identificacion = input("Identificación / Cédula: ").strip()
                nombre = input("Nombre completo: ").strip()
                correo = input("Correo electrónico: ").strip()

                usr = Usuario(identificacion, nombre, correo)
                if restaurante.agregar_usuario(usr):
                    print("✓ Usuario registrado con éxito.")
                else:
                    print("✕ Error: Ya existe un usuario con esa identificación.")
            except ValueError as e:
                print(f"✕ Error en el ingreso de datos: {e}")

        elif opcion == "4":
            print("\n--- LISTA DE USUARIOS ---")
            usuarios = restaurante.listar_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                for u in usuarios:
                    print(f"ID: {u.identificacion} | Nombre: {u.nombre} | Correo: {u.correo}")

        elif opcion == "5":
            print("\n--- REALIZAR VENTA ---")
            id_usr = input("Identificación del Usuario: ").strip()
            cod_prod = input("Código del Producto: ").strip()
            try:
                cant = int(input("Cantidad a comprar: "))
                exito, msj = restaurante.vender_producto(cod_prod, id_usr, cant)
                print(f"{'✓' if exito else '✕'} {msj}")
            except ValueError:
                print("✕ Error: La cantidad debe ser un número entero.")

        elif opcion == "6":
            print("\n--- CONSULTAR VENTAS POR USUARIO ---")
            id_usr = input("Identificación del Usuario: ").strip()
            usuario = restaurante.buscar_usuario(id_usr)

            if not usuario:
                print("✕ Error: Usuario no encontrado.")
            else:
                ventas = restaurante.obtener_ventas_por_usuario(id_usr)
                print(f"\nVentas registradas para {usuario.nombre} (ID: {usuario.identificacion}):")
                if not ventas:
                    print("El usuario no ha realizado compras.")
                else:
                    for idx, v in enumerate(ventas, 1):
                        print(f"{idx}. Producto: {v['nombre_producto']} (Cód: {v['codigo_producto']}) | Cantidad: {v['cantidad']} | Subtotal: ${v['subtotal']:.2f}")

        elif opcion == "7":
            print("\n¡Gracias por utilizar restaurante_app!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()