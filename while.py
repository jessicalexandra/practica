print("***MENU***")
print("Ingrese 1 para recibir producto: ")
print("Ingrese 2 para mostrar los  productos: ")
print("Ingrese 3 para editar producto: ")
print("Ingrese 4 para eliminar producto: ")
print("Ingrese 5 para salir: ")
productos=[]
option=1

while option!=0:
    option=(int(input("Ingrese la opcion: ")))
    
    producto={}
    if option==1:
        producto['codigo']=int(input("Ingrese el codigo: "))
        producto['nombre']=(input("Ingrese el nombre: "))
        producto['precio']=int(input("Ingrese el precio: "))
        productos.append(producto)
    elif option==2:
        print(productos)
    elif option==3:
        codigo=int(input("Digite el codigo a buscar: "))
        for prod in productos:
            if prod['codigo']==codigo:
                prod['precio']=float(input("Digite el nuevo precio: "))
            else:
                print("producto no encontrado ")
    elif option==4:
        codigo=int(input("Digite el codigo a buscar: "))
        for elim in productos:
            if elim['codigo']==codigo:
                productos.remove(elim)
                print("elemento eliminado")
            else:
               print("producto no encontrado ")
    else:
        print("opcion no valida")
    