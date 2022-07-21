from utils2 import limpiarPantalla
from models2 import Producto

ruta_archivo = "./archivos/producto.txt"


def crearPastilla():
    codigo = input("Codigo: ")
    nombre = input("Nombres: ")
    detalle = input("Detalle: ")
    precio = input("Precio: ")

    pastilla = Producto(codigo,nombre,detalle,precio)

    archivoPastilla = open(ruta_archivo, "a")
    archivoPastilla.write(str(pastilla))
    archivoPastilla.close()

def validarCodigoPastilla(codigo):
    pastilla = None 
    archivoPastilla = open(ruta_archivo, "r")
    for linea in archivoPastilla.readlines():
        atributos = linea.split(";")
        if codigo == atributos[0]:
             pastilla = Producto(atributos[0], atributos[1], atributos[2], atributos[3])
             break
    archivoPastilla.close()
    
    return pastilla

def gestionPastilla():
    limpiarPantalla()
    while True:
        print("SUBMENU: GESTION DE PASTILLAS ")
        print("1. Ingresar pastilla")
        print("2. Mostrar medicina")
        print("3. Buscar medicina")
        print("4. Regresar al menu principal")
        op = int(input("Opción: "))

        match (op):
            case 1:
                limpiarPantalla()
                crearPastilla()
                print("creado correctamente")
            case 2:
                limpiarPantalla()
                print("mostrar medicina")
                  


            case 3:
                limpiarPantalla()
                codigo = input("ingrese codigo de la pastilla: ")
                fila =str(validarCodigoPastilla(codigo))
                print(f"fila")
                #"001"; "Paracetamol";"Alivia dolores"; "4.00"
                output = fila.split(";")
                #001 Paracetamol Alivia dolores 4.00
                print(output)

            case 4:
                limpiarPantalla()
                print("buscar medicina")
            case 5:
                limpiarPantalla()
                print("Gracias por preferirnos")
                break
            case _:
                print("opcion incorrecta") 
                time.sleep(2)
                limpiarPantalla()               

       
    