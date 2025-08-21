def crear_archivo():
    with open("usuarios.txt","w",encoding="utf-8") as f:
        f.write("cedula,nombre,saldo\n")
        f.write("12345,jose,50.43\n")
        f.write("54321,dario,43.12\n")
        f.write("67890,santiago,99.60\n")
        f.write("98765,maria,20.00\n")
        f.write("24680,carolina,55.30\n")
        f.write("72682,jorge,12.01\n")
    print("archivo creado\n")

def consultar_saldo():
    nombre_buscar = input("nombre del cliente: ")
    with open("usuarios.txt","r",encoding="utf-8") as f:
        f.readline()
        encontrado = False
        for linea in f:
            cedula,nombre,saldo = linea.strip().split(",")
            if nombre == nombre_buscar:
                print("saldo de",nombre,":",saldo,"\n")
                encontrado = True
                break
        if not encontrado:
            print("cliente no encontrado\n")

def contar_mayores_50():
    contador = 0
    with open("usuarios.txt","r",encoding="utf-8") as f:
        f.readline()
        for linea in f:
            cedula,nombre,saldo = linea.strip().split(",")
            if float(saldo) > 50:
                contador += 1
    print("clientes con saldo mayor a 50:",contador,"\n")

def ordenar_por_saldo():
    usuarios = []
    with open("usuarios.txt","r",encoding="utf-8") as f:
        f.readline()
        for linea in f:
            cedula,nombre,saldo = linea.strip().split(",")
            usuarios.append([nombre,float(saldo)])
    for i in range(len(usuarios)):
        for j in range(i+1,len(usuarios)):
            if usuarios[i][1] > usuarios[j][1]:
                usuarios[i],usuarios[j] = usuarios[j],usuarios[i]
    print("clientes ordenados por saldo:")
    for c in usuarios                           :
        print(c[0],c[1])
    print()

while True:
    print("1.crear archivo  2.consultar saldo  3.mayores a 50  4.ordenar  5.salir")
    op = input("opcion: ")
    if op=="1":
        crear_archivo()
    elif op=="2":
        consultar_saldo()
    elif op=="3":
        contar_mayores_50()
    elif op=="4":
        ordenar_por_saldo()
    elif op=="5":
        break
    else:
        print("opcion no existente\n")