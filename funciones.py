
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
    pass

def exportar_archivo_txt():
    pass

def salir():
    print("GRACIAS, ADIOS")
    exit()

