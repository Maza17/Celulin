import json
import os
import time 
base_datos = "dbCelulin.txt"
tablaVentas = [[0] , [0] , [0] , [0] , [0] , [0], [0]];
opcion = 0;


with open(base_datos, "r") as db:
    if db.readline().strip():
        with open(base_datos,"r") as db:
            tablaVentas = json.load(db);

 
def bienvenida():
    if os.name == "posix":
        var = "clear"       
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
 
    time.sleep(1)
 
    os.system(var) 
    print("****************************************") 
    print("*                                      *")
    print("*    ¡Bienvenidos a Sistema Celulin!   *")
    print("*                                      *")
    print("****************************************")
 
    time.sleep(1)
    os.system(var)
 
    print("****************************************")
    print("*                                      *")
    print("*      Aquí se almacenarán datos       *")
    print("*                                      *")
    print("****************************************")
 
    time.sleep(1)
    os.system(var)
 
    print("****************************************")
    print("*                                      *")
    print("*      De las ventas realizadas        *")
    print("*                                      *")
    print("****************************************")
 
    time.sleep(1)

def borrarpantalla():
    if os.name == "posix":
        borrarPantalla = lambda: os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        borrarPantalla = lambda: os.system ("cls") 


def value_int_input (msj1, msj2):
    error_mensaje = msj1
    while True:
        try:
            numero = no_spaces(input(error_mensaje))
            return int(numero);
    
        except ValueError:
            error_mensaje = msj2

def no_string_input (msj1, msj2):
    error_mensaje = msj1
    while True:
        entrada = no_spaces(input(error_mensaje))        
        if entrada.isdigit():  
            error_mensaje = msj2
            continue
        else:
            return entrada

def no_spaces (nombre_entrada):
        while True:
            check = str(nombre_entrada).replace(" ", "")
            if len(check) == 0:
                nombre_entrada = input("No se permiten los espacios vacíos: ")
                continue
            else:
                return nombre_entrada

def input_limitado(msj1, msj2, limite):
    error_mensaje = msj1
    while True:
        entrada = str(value_int_input(msj1, msj2))
        if len(entrada) <= limite:
            return int(entrada)
        error_mensaje = f"Error: La entrada debe tener máximo {limite} caracteres."
        print(error_mensaje);

def buscar_Numero():
    numero = no_spaces(input_limitado("\nIngrese un número de teléfono: " , "Ingrese un caracter válido\nIngrese un número registrado: ", 8));
    for i in range(len(tablaVentas[0])):
        if numero == tablaVentas[0][i]:
            encontrado = True;
            break;
        else:
            encontrado = False;      
    return numero, encontrado, i;

def Companias():
    opcionCompanias = 0;
    while opcionCompanias != 5:
        opcionCompanias = value_int_input("\nMenú de compañías telefónicas:\n1. Claro \n2. Tigo \n3. Movistar \n4. Digicel\n5. Salir\nSeleccione una compañia telefónica: ", "Por favor ingrese una opción válida, intente de nuevo: ");
        if opcionCompanias == 1:
            return opcionCompanias;
        elif opcionCompanias == 2:
            return opcionCompanias;
        elif opcionCompanias == 3:
            return opcionCompanias;
        elif opcionCompanias == 4:
            return opcionCompanias;
        elif opcionCompanias == 5:
            opcionCompanias = 5;

def TipoPago():
    opcionPago = 0;
    while opcionPago != 3:
        opcionPago = value_int_input("\nMenú de tipos de pago:\n1. Prepago\n2. Pospago\nSeleccione un tipo de pago: ", "Por favor ingrese una opción válida, intente de nuevo: ");
        if opcionPago == 1:
            valor = 0.00;
            return opcionPago, valor;
        elif opcionPago == 2:
            valor = 25.00;
            return opcionPago, valor;
        elif opcionPago == 3:
            opcionPago = 3;

def AgregarVenta():
    print("------------Ingresar un nuevo registro-------------")
    numtelefono, encontrado, i = buscar_Numero();
    if encontrado == True:
        print("Ya existe un registro con ese número, ingrese uno diferente. \n");
    else:
        tablaVentas[0].append(numtelefono);
        tablaVentas[1].append(Companias());
        tablaVentas[2].append(no_spaces(input("\nIngrese el modelo del teléfono: ")));
        tablaVentas[3].append(no_string_input("\nIngrese el nombre del propietario: ", "Error: No se permiten números. Por favor intente de nuevo: "));
        tablaVentas[4].append(no_spaces(input("\nIngrese la dirección del propietario: ")));
        opcionCompania, valorPago = TipoPago();
        tablaVentas[5].append(opcionCompania);
        tablaVentas[6].append(valorPago);
        print("Se añadido exitosamente")
        borrarpantalla()
    Actualizar();

def ModificarVenta():
    MostrarVentas()
    numero, encontrado, i = buscar_Numero()
    if encontrado == True:
        opcion = value_int_input("\n¿Qué desea cambiar de este registro?\n 1. Número\n 2. Compañía telefónica\n 3. Modelo de Teléfono\n 4. Nombre propietario\n 5. Dirección\n 6. Tipo pago\n 7. Salir\n Ingrese su opcion: ","Ingrese una opción válida: ")
        if opcion == 1:
            columna = i;
            numeronuevo = value_int_input ("\nIngrese el nuevo número: ", "Ingrese un caracter válido: ")
            tablaVentas[0][columna] = numeronuevo;
            print ("Se ha modificado exitosamente")
        elif opcion == 2:
            columna = i;
            telefonianueva = Companias()
            tablaVentas[1][columna] = telefonianueva;
            print ("Se ha modificado exitosamente")
        elif opcion == 3:
            columna = i;
            modelonuevo = input("Ingrese el nuevo modelo: ");
            tablaVentas[2][columna] = modelonuevo;
            print ("Se ha modificado exitosamente")
        elif opcion == 4:
            columna = i;
            nombrenuevo = no_string_input("Ingrese el nombre nuevo: ", "Error: No se permiten números. Por favor intente de nuevo: ");
            tablaVentas[3][columna] = nombrenuevo;
            print ("Se ha modificado exitosamente")
        elif opcion == 5:
            columna = i;
            direcionnueva = input("Ingrese la nueva dirección: ");
            tablaVentas[4][columna] = direcionnueva;
            print ("Se ha modificado exitosamente")
        elif opcion == 6:
            columna = i;
            pagonuevo = value_int_input("\nMenú de tipos de pago:\n1. Prepago\n2. Pospago\nSeleccione un tipo de pago: ", "Por favor ingrese una opción válida, intente de nuevo: ");
            tablaVentas[5][columna] = pagonuevo;
            columna = i;
            if pagonuevo == 1:
                mensualidadnueva = 0.00
            elif pagonuevo == 2:
                mensualidadnueva = 25.00
            tablaVentas[6][columna] = mensualidadnueva;
            print ("Se ha modificado exitosamente")
        elif opcion == 7:
            opcion == 7
        else: 
            print("Seleccione una de las opciones antes mostradas.\n");
            value_int_input("¿Qué desea cambiar de este registro?\n 1. Número\n 2. Compañía telefónica\n 3. Modelo de Teléfono\n 4. Nombre propietario\n 5. Dirección\n 6.Tipo pago\n 7. salir\n  Ingrese su opcion: ","Ingrese una opción válida: ")
    else:
        print("Numero no encontrado")
        ModificarVenta()
        borrarpantalla()
    Actualizar();

def EliminarDatos():
    MostrarVentas()
    numero = value_int_input("\nIngrese el número de venta a eliminar: " , "Ingrese un caracter válido\nIngrese un número de teléfono: ")
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
        tablaVentas[6].pop(i);
    
        print("Se ha elimiado exitosamente")
    else:
        print("Numero no encontrado")
        EliminarDatos()
        borrarpantalla()
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
    bienvenida()
    print(f"\n------------BIENVENIDO AL SISTEMA DE CELULIN SV------------")
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
        print("Ingrese una opción válida");