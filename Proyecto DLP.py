import json

base_datos = "dbCelulin.txt"
tablaVentas = [[0] , [0] , [0] , [0] , [0] , [0]];
opcion = 0;

with open(base_datos, "r") as db:
    if db.readline().strip():
        with open(base_datos,"r") as db:
            tablaVentas = json.load(db);


def AgregarVenta():
    print("------------Ingresar un nuevo registro-------------")
    numtelefono = input("Ingrese el número de teléfono: ")
    for i in range(len(tablaVentas[0])):
        if tablaVentas[0][i] == numtelefono:
            encontrado = True;
        else:
            encontrado = False;
    
    if encontrado == True:
        print("Ya existe un registro con ese número, ingrese uno diferente. \n");
    else:
        tablaVentas[0].append(numtelefono);
        tablaVentas[1].append(input("Ingrese el nombre de la compañia telefónica: "));
        tablaVentas[2].append(input("Ingrese el modelo del teléfono: "));
        tablaVentas[3].append(input("Ingrese el nombre del propietario: "));
        tablaVentas[4].append(input("Ingrese la dirección del propietario: "));
        tablaVentas[5].append(input("Ingrese el tipo de pago a realizar: "));
    Actualizar();

def ModificarVenta():
    numero = input("Ingrese el numero del registro a modificar: ")
    for i in range(len(tablaVentas[0])):
        if tablaVentas[0][i] == numero:
            encontrado = True;
            break;
        else:
            encontrado = False;
    
    while numero.isdigit() != True:
        try: numero = (input("Ingrese el número del registro a modificar"))
        ModificarVenta()
        except ValueError: 
        print("Ingrese un caracter valido")
    
    if encontrado == True:
        opcion = int(input("¿Qué desea cambiar de este registro?\n 1. Numero\n 2. Compania telefónica\n 3. Modelo de Teléfono\n 4. Nombre propietario\n 5. Dirección\n 6.Tipo pago\n  Ingrese su opcion: "));
        if opcion == 1:
            columna = i;
            numeronuevo = input("Ingrese el nuevo número: ")
            tablaVentas[0][columna] = numeronuevo;
        elif opcion == 2:
            columna = i;
            telefonianueva = input("Ingrese la nueva telefoía: ")
            tablaVentas[1][columna] = telefonianueva;
        elif opcion == 3:
            columna = i;
            modelonuevo = input("Ingrese el nuevo modelo: ");
            tablaVentas[2][columna] = modelonuevo;
        elif opcion == 4:
            columna = i;
            nombrenuevo = input("Ingrese el nombre nuevo: ");
            tablaVentas[3][columna] = nombrenuevo;
        elif opcion == 5:
            columna = i;
            direcionnueva = input("Ingrese la nueva dirección: ");
            tablaVentas[4][columna] = direcionnueva;
        elif opcion == 6:
            columna = i;
            pagonuevo = input("Ingrese el nuevo metodo de pago: ");
            tablaVentas[5][columna] = pagonuevo;
        else: 
            print("Seleccione una de las opciones antes mostradas.\n");
    Actualizar();

def EliminarDatos():
    numero = input("Ingrese el número telefónico de la persona a eliminar: ")
    for i in range(len(tablaVentas[0])):
        if tablaVentas[0][i] == numero:
            encontrado = True;
            break;
        else:
            encontrado = False;
    
    if encontrado == True:
        tablaVentas[0].pop(i);
        tablaVentas[1].pop(i);
        tablaVentas[2].pop(i);
        tablaVentas[3].pop(i);
        tablaVentas[4].pop(i);
        tablaVentas[5].pop(i);
    Actualizar();

def MostrarVentas():
    print("-----Lista de ventas ingresadas-----")
    # Recorrer la tabla
    for registro in tablaVentas:
    # Imprimir los elementos a partir del segundo índice
        print(registro[1:])

def Actualizar():
    with open(base_datos, "w") as db:
        json.dump(tablaVentas, db)

while opcion != 5:
    print(f"------------BIENVENIDO AL SISTEMA DE CELULIN SV------------")
    print("Acciones disponibles: ")
    print("1. Ingresar nueva venta");
    print("2. Modificar una venta");
    print("3. Eliminar una venta")
    print("4. Mostrar ventas");
    print("5. Salir");
    opcion = int(input("Seleccione la acción a realizar: "));

    if opcion == 1:
        AgregarVenta();
    elif opcion == 2:
        ModificarVenta();
    elif opcion == 3:
        EliminarDatos();
    elif opcion == 4:
        MostrarVentas();
    elif opcion == 5:
        opcion == 5;
    else:
        print("Ingrese una opcion valida");