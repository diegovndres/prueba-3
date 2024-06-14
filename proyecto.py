import os, time
from funciones import * 

while True:
    print("MENU TRABAJADORES")
    print("1. REGISTRAR TRABAJADORES")
    print("2. LISTAR TRABAJADORES")
    print("3. IMPRIMIR PLANILLA DE SUELDOS")
    print("4. SALIR DEL PROGRAMA")
    opc =  int(input("Ingrese opcion: "))
    os.system('cls')
    if opc == 1:
        registrar_trabajador()

    elif opc == 2:
        pass
    elif opc==3:
        pass
    else:
        print("GRACIAS ADIOS")
        break
    time.sleep(3)               
