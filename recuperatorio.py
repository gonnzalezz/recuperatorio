lista_compras = []

def menu():
    print("1-Mostrar lista")
    print("2-agregar elementos")
    print("3-eliminar elementos")
    print("4-salir")

def eliminar(eliminar):
    lista_compras.remove(eliminar)

def agregar(elemento):
    lista_compras.append(elemento)

    
while True:
    menu()
    opcion = int(input("elige una opcion: "))
    if opcion == 1:
        print("lista de compras: ", lista_compras if lista_compras else "vacia")
    elif opcion == 2:
       elemento = input("elemento a agregar: ")
       agregar(elemento)
    elif opcion == 3:
        #try:
        #    lista_ compras.remove(input("elemento a eliminar: "))
        # eccvept ValueError:
        #    print("el elemento no esta en la lista")
        eliminar_elemt = input("ingrese elelemento a eli: ")
        eliminar(eliminar_elemt)
    elif opcion == 4:
        break
    else:
        print("opcion no valida")