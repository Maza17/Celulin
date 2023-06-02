import json
base_datos = "dbCelulin.txt"
tablaVentas = [[0] , [0] , [0] , [0] , [0] , [0]];
opcion = 0;
with open(base_datos, "r") as db:
    if db.readline().strip():
        with open(base_datos,"r") as db:
            tablaVentas = json.load(db);

def value_int_input (msj1, msj2):
    error_mensaje = msj1
    while True:
        try:
            numero = int(input(error_mensaje))
            return numero
#aca no es necesario el return int, osea el return si, el int no, porque en la variable número ya la definiste como int "Appuru"
   
        except ValueError:
            error_mensaje = msj2

def no_string_input (msj1, msj2):
    error_mensaje = msj1
    while True:
        entrada = input(error_mensaje)
        if not entrada.isdigit() and entrada == None:   
            return entrada
        error_mensaje = msj2

# Deberían definir primero la función value int input para que no les vaya a dar error por llamar a una funcion que todavía no han definido "Appuru"
def buscar_Numero ():
    numero = value_int_input("Ingrese un número registrado: " , "Ingrese un caracter válido\nIngrese un número registrado: ")
    for i in range(len(tablaVentas[0])):
        if tablaVentas[0][i] == numero:
            encontrado = True;
        else:
            encontrado = False;
            
    return encontrado, i;

def AgregarVenta():
    print("------------Ingresar un nuevo registro-------------")
# acá podrían usar la función buscar número que es lo mismo prácticamente que el bloque que sigue a este comentario, y así ahorrarse un par de lineas "appuru"
    numtelefono = value_int_input("Ingrese un número de teléfono: " , "Ingrese un caracter válido\nIngrese un número de teléfono: ")
    for i in range(len(tablaVentas[0])):
        if tablaVentas[0][i] == numtelefono:
            encontrado = True;
        else:
            encontrado = False;
    
    if encontrado == True:
        print("Ya existe un registro con ese número, ingrese uno diferente. \n");
    else:
        tablaVentas[0].append(numtelefono);
        tablaVentas[1].append(no_string_input("Ingrese el nombre de la compañia telefónica: ", "Error: No se permiten números. Por favor intente de nuevo: "));
        tablaVentas[2].append(input("Ingrese el modelo del teléfono: "));
        tablaVentas[3].append(no_string_input("Ingrese el nombre del propietario: ", "Error: No se permiten números. Por favor intente de nuevo: "));
        tablaVentas[4].append(input("Ingrese la dirección del propietario: "));
        tablaVentas[5].append(no_string_input("Ingrese el tipo de pago a realizar: ", "Error: No se permiten números. Por favor intente de nuevo: "));
        print("Se añadido exitosamente")
    Actualizar();

def ModificarVenta():
    encontrado, i = buscar_Numero()
    if encontrado == True:
        opcion = value_int_input("¿Qué desea cambiar de este registro?\n 1. Numero\n 2. Compania telefónica\n 3. Modelo de Teléfono\n 4. Nombre propietario\n 5. Dirección\n 6. Tipo pago\n 7. Salir\n Ingrese su opcion: ","Ingrese una opción válida: ")
        if opcion == 1:
            columna = i;
            numeronuevo = value_int_input ("Ingrese el nuevo número: ", "Ingrese un caracter válido: ")
            tablaVentas[0][columna] = numeronuevo;
            print ("Se ha modificado exitosamente")
        elif opcion == 2:
            columna = i;
            telefonianueva = input("Ingrese la nueva telefoía: ")
            tablaVentas[1][columna] = telefonianueva;
            print ("Se ha modificado exitosamente")
        elif opcion == 3:
            columna = i;
            modelonuevo = input("Ingrese el nuevo modelo: ");
            tablaVentas[2][columna] = modelonuevo;
            print ("Se ha modificado exitosamente")
        elif opcion == 4:
            columna = i;
            nombrenuevo = input("Ingrese el nombre nuevo: ");
            tablaVentas[3][columna] = nombrenuevo;
            print ("Se ha modificado exitosamente")
        elif opcion == 5:
            columna = i;
            direcionnueva = input("Ingrese la nueva dirección: ");
            tablaVentas[4][columna] = direcionnueva;
            print ("Se ha modificado exitosamente")
        elif opcion == 6:
            columna = i;
            pagonuevo = input("Ingrese el nuevo metodo de pago: ");
            tablaVentas[5][columna] = pagonuevo;
            print ("Se ha modificado exitosamente")
        elif opcion == 7:
            opcion ==7
        else: 
            print("Seleccione una de las opciones antes mostradas.\n");
            value_int_input("¿Qué desea cambiar de este registro?\n 1. Numero\n 2. Compania telefónica\n 3. Modelo de Teléfono\n 4. Nombre propietario\n 5. Dirección\n 6.Tipo pago\n 7. salir\n  Ingrese su opcion: ","Ingrese una opción válida: ")
    else:
        print("Numero no encontrado")
        ModificarVenta()
    Actualizar();

def EliminarDatos():
    numero = value_int_input("Ingrese un número de teléfono: " , "Ingrese un caracter válido\nIngrese un número de teléfono: ")
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
    
        print("Se ha elimiado exitosamente")
    else:
        print("Numero no encontrado")
        EliminarDatos()
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
    print("3. Eliminar una venta");
    print("4. Mostrar ventas");
    print("5. Salir");
    opcion = value_int_input("Ingrese una opción : " , "Ingrese un carácter válido:  ")

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
        print("Ingrese una opción válida")