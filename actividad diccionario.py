
class Usuario:
    def __init__(self, nombrecompleto, nickname, clave, tipo, fecha_creacion):
        
        self.datos = {
            'nombrecompleto': nombrecompleto,
            'nickname': nickname,
            'clave': clave,
            'tipo': tipo,
            'fecha_creacion': fecha_creacion
        }


usuarios = []


def buscar_usuario(value):
    for usuario in usuarios:
        if value in usuario.datos.values():
            return usuario.datos
    return "Usuario no encontrado"


def eliminar_usuario(value):
    for usuario in usuarios:
        if value in usuario.datos.values():
            usuarios.remove(usuario)
            return f"Usuario con {value} eliminado."
    return "Usuario no encontrado"


def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Agregar Usuario")
        print("2. Buscar Usuario")
        print("3. Eliminar Usuario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            
            nombrecompleto = input("Ingrese el nombre completo: ")
            nickname = input("Ingrese el nickname: ")
            clave = input("Ingrese la clave: ")
            tipo = input("Ingrese el tipo de usuario: ")
            fecha_creacion = input("Ingrese la fecha de creación (dd-mm-yyyy): ")

            usuario = Usuario(nombrecompleto, nickname, clave, tipo, fecha_creacion)
            usuarios.append(usuario)
            print("Usuario agregado correctamente.")

        elif opcion == '2':
            
            value = input("Ingrese el valor a buscar (nombre, nickname, etc.): ")
            resultado = buscar_usuario(value)
            print(f"Resultado de la búsqueda: {resultado}")

        elif opcion == '3':
            
            value = input("Ingrese el valor del usuario a eliminar: ")
            resultado = eliminar_usuario(value)
            print(resultado)

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")


menu()
