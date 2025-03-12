#software estructuras
nombreVendedor=None
productos=[]#arreglo, lista
producto={}#objetos, diccionario

#creando un ciclo en python
opcion=100
print("***Merqueo APP***")
print("1. Crear lista de mercado")
print("2. Verificar lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("5. Salir")

while opcion != 5:
    opcion=int(input("Digita una opcion: "))
    if opcion ==1:
        print("Bienvenido a la creacion de tu lista de mercado")

        #creando claves y valores de un diccionario
        producto["id"] = 5
        producto["nombre"] = input("Digita el nombre del producto: ")
        producto["precio"] = int (input("Digita el precio del producto: "))
        producto["cantidad"] = int(input("Cuantos unidades de este producto vas a llevar: "))
        producto["presentacion"] = input("Cual presentacion llevaras?: ")

        #Mostrando mi diccionario
       #print(producto)

        #agregando elementos a una lista
        productos.append(producto)
        print(productos)

        
    elif opcion == 2:
        #utilizar un ciclo for en python para recorrer listas
        for productoSeleccionado in productos:
            print(productoSeleccionado["nombre"])
    elif opcion == 3:
        #0.preguntar que quiero editar
        #1.encontrar el elemento
        #2.selecciono el elemento
        #3.accedo a las propiedades o atrbutos que quiero modificar
        productocambio = int(("Digita el id que vas a editar: "))
        for productoBuscado in productos:
            if productoBuscado["id"]==productocambio:
                print("lo encontre")
            else:
                print("no lo encontre")    
        
        
    elif opcion == 4:
        print("opcion 4")
    else:
        print("opcion no valida")               


