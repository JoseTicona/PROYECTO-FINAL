#!/usr/bin/env python
# coding: utf-8
# importaciones de librerias
import getpass
import time 

from utils2 import limpiarPantalla
from productos2 import gestionPastilla


def run() :
    while True:
        print("\033[91m" + "   FARMACIA  MR THOMI   " + "\033[91m")
        print("\033[0m")
        print("============================")
        print(" MENÚ PRINCIPAL DEL SISTEMA ")
        print("1. Gestión de medicamentos")
        print("2. Gestiónde Clientes")
        print("3. Gestión de Ventas")
        print("0. Salir")
        op = int(input("Opción: "))

        match (op):
            case 1:
                limpiarPantalla()
                gestionPastilla()
            case 2:
                limpiarPantalla()
                print("logica para la opcion2" )
            case 3:
                limpiarPantalla()
                print("logica para la opcion2" )
            case 0:
                limpiarPantalla()
                print("Saliendo del sistema... hasta pronto")
                break

            case _:
                print("opción incorrecta")
                time.sleep(2)
                limpiarPantalla()

    
def main():
    acumulador = 0
    while True and acumulador != 3:
        passwd = getpass.getpass("identifique su identidad: ")

        if passwd == "1234":
            limpiarPantalla()
            run()
        else : 
            print("contraseña incorrecta")
            acumulador += 1
            time.sleep(2)
            limpiarPantalla()

            #break




if __name__ == "__main__":
    main()