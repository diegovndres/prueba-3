import os, time


trabajadores = []
cargos = ("CEO","DESARROLLADOR","ANALISTA")
while True:
    print("MENU TRABAJADORES")
    print("1. REGISTRAR TRABAJADORES")
    print("2. LISTAR TRABAJADORES")
    print("3. IMPRIMIR PLANILLA DE SUELDOS")
    print("4. SALIR DEL PROGRAMA")
    opc =  int(input("Ingrese opcion: "))
    os.system('cls')
    if opc == 1:
        print("REGISTRO TRABAJADOR")
        nombre_apellido = input("Ingrese nombre y apellido: ")
        cargo = int(input("Ingrese cargo(1. CEO 2. DESARROLLADOR 3. ANALISTA): "))
        sueldo_bruto = int(input("Ingrese sueldo bruto: "))
        desc_salud = 7/100 * sueldo_bruto
        desc_afp = int(12/100 * sueldo_bruto)
        sueldo_liquido = sueldo_bruto * 0.81
        trabajador = [nombre_apellido,cargo[cargo-1],sueldo_bruto,desc_salud,desc_afp,sueldo_liquido]
        trabajadores.append(trabajador)
        print("TRABAJADOR REGISTRADO")

    elif opc == 2:
        pass
    elif opc==3:
        pass
    else:
        print("GRACIAS ADIOS")
        break
    time.sleep(3)               
