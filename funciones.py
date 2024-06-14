
trabajadores = []
cargos = ("CEO","DESARROLLADOR","ANALISTA")
def registrar_trabajador():
    print("REGISTRO TRABAJADOR")
    nombre_apellido = input("Ingrese nombre y apellido: ")
    cargo = int(input("Ingrese cargo(1. CEO 2. DESARROLLADOR 3. ANALISTA): "))
    sueldo_bruto = int(input("Ingrese sueldo bruto: "))
    desc_salud = 7/100 * sueldo_bruto
    desc_afp = int(12/100 * sueldo_bruto)
    sueldo_liquido = sueldo_bruto * 0.81
    trabajador = [nombre_apellido,cargos[cargo-1],sueldo_bruto,desc_salud,desc_afp,sueldo_liquido]
    trabajadores.append(trabajador)
    print("TRABAJADOR REGISTRADO")

def listar_trabajador():
    if len(trabajadores)==0:
        print("LISTA VACIA, REGISTRE UN TRABAJADOR EN LA LISTA 1")
    else:
        print("\tLISTA DE TRABAJADORES")
        for t in trabajadores:
            print(f"NOMBRE: {t[0]}\nCargo: {t[1]}\nBruto: {t[2]}\nSalud: {t[3]}\nAFP: {t[4]}\nLIQUIDO: {t[5]}")
    
def exportar_archivo_txt():
    if len(trabajadores)==0:
        print("Lista vacia, registre un trabajador en la opcion 1")
    else:
        cargo = int(input("Ingrese cargo para planilla(1.CEO,2.DESARROLLADOR,3.ANALISTA,4.TODOS): "))
        if cargo == 4:
            with open("todos_los_trabajadores"+".txt","w") as archivo:
                for t in trabajadores:
                    archivo.writeprint(f"NOMBRE: {t[0]}\nCargo: {t[1]}\nBruto: {t[2]}\nSalud: {t[3]}\nAFP: {t[4]}\nLIQUIDO: {t[5]}")
            print("ARCHIVO CREADO CON EXITO!")


def salir():
    print("GRACIAS, ADIOS")
    exit()

