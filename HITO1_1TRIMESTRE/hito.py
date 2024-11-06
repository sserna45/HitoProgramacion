#EJERCICIO1
# Primero le pediremos al usuario que escoga una opción
while True:
    print("Selecciona una opción: Cuadrado, Rectángulo o Salir:")
    print("1 - Cuadrado")
    print("2 - Rectángulo")
    print("3 - Salir")

#Aquí con el "input" le pediremos que escoga una de las tres opciones que se preguntaron anteriormente (1,2,3)
    opcion = input("Ingrese su opción, 1, 2 o 3:  ")

#Ahora crearemos con los "if" y "elif" que los datos a ingresar dependiendo si has escogido (1,2 o 3)
    if opcion == '1':
        lado = float(input("Ingresa el lado del cuadrado: "))
        area = lado ** 2
        perimetro = 4 * lado
        print("El área es:", area)
        print("El perímetro es:", perimetro)
        break

    elif opcion == '2':
        base = float(input("Ingresa la base del rectángulo:"))
        altura = float(input("Ingresa la altura del ractángulo:"))
        area = base * altura
        perimetro = 2 * (base + altura)
        print("El área es:", area)
        print("El perímetro es:", perimetro) 
    
    elif opcion == '3':
        print("Cerrando menú.")

        break  
    else:
        print("Respuesta no válida. Elija 1, 2 o 3")  #Aquí si la respuesta escogida al principio en el menú (1,2 o 3) no es válida te pedirá que escogas de nuevo.






#EJERCICIO 2
import random #Primero importaremos random para poder utilizar random.randint y que el programa escoga automaticamente piedra, papel o tijera.

#Ahora crearemos el menú para que el usuario escoja una de las tres opciones del juego
while True:
    print("Elige Piedra, Papel o Tijera")
    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")

#Con el input le diremos al usuario que escoga su opción (1,2 o 3)
    opcion = input("Ingresa tu elección (1, 2 o 3): ")

    if opcion == '1':
        opcion_elegida = 1
    elif opcion == '2':
        opcion_elegida = 2
    elif opcion == '3':
        opcion_elegida = 3
    else: 
        print("Respuesta no válida. Elija 1, 2 o 3")
        continue  

#Ahora con el random.randint haremos que el programa escoja entre las tres opciones una aleatoria.
    opcion_programa = random.randint(1, 3)
    mano = {1: "Piedra", 2: "Papel", 3: "Tijera"}

#Aquí le enseñará al usuario la opción que escogiste y la opción que a usado el programa contra ti
    print(f"\nHas elegido: {mano[opcion_elegida]}")
    print(f"Tu rival ha elegido: {mano[opcion_programa]}")

#Y aquí crearemos las combinaciones para saber si es Victoria, Empate o Derrota.
    if opcion_elegida == opcion_programa:
        print("Empate.")
    elif (opcion_elegida == 1 and opcion_programa == 3) or \
         (opcion_elegida == 2 and opcion_programa == 1) or \
         (opcion_elegida == 3 and opcion_programa == 2):
        print("Victoria")
    else:
        print("Derrota.")
    break 







#EJERCICIO 3

#Primero crearemos la opción de introducir el saldo inicial de la cuenta.
saldo = -1
while saldo < 0:
    saldo_input = input("Introduce el saldo inicial de la cuenta: ")
    
    try:
        saldo = float(saldo_input)
        if saldo < 0:
            print("El saldo no puede ser negativo. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Ahora crearemos el menú.
while True:
    print("Menú:")
    print("1 - Ingresar dinero")
    print("2 - Retirar dinero")
    print("3 - Mostrar saldo")
    print("4 - Salir")

# Ahora le pediremos al usuario que seleccione una de las 4 opciones correspondientes al menú.
    opcion = input("Elige una opción (1-4): ")

# Ahora según la opción que haya elegio anteriormente crearemos las preguntas o respuestas.
# Aquí para la opción Ingresar dinero (1), el programa preguntará la cantidad que quiere ingresar.
    if opcion == "1":
        cantidad_input = input("¿Cuánto dinero quiere ingresar ? ")   #Aquí se le pedirá que escriba la cantidad de dinero que quiere ingresar.
        
        try:
            cantidad = float(cantidad_input)
            if cantidad < 0: 
                print("No puedes ingresar una cantidad negativa.") #Si la cantidad es negativa le dirá que no deja ingresar esa cantidad al ser negativa.
            else:
                saldo += cantidad
                print(f"Has ingresado {cantidad}. Saldo actual: {saldo}") #Una vez ingresada la cantidad de dinero escogida le aparecerá la cantidad ingresada y el saldo actual.
        except ValueError:
            print("Cantidad no válida, ingresa una cantidad válida.") #Si la cantidad  no es válida, le pedirá que ingrese una cantidad válida.

# Aquí es para la opción reitrar dinero (2), el programa preguntará la cantidad que quiere retirar.
    elif opcion == "2":
        cantidad_input = input("¿Cuánto dinero quiere retirar? ") #Aquí se le pedirá qu escriba la cantidad de dinero que quiere retirar

        try:
            cantidad = float(cantidad_input) 
            if cantidad < 0:
                print("No puedes retirar una cantidad negativa.") #Aquí si a introducido un numero negativo no le dejará retirar esa cantidad
            elif cantidad > saldo:
                print("Saldo insuficiente.") # Aquí si la cantidad que a escogido a retirar es menor que el saldo actual, no le dejarña
            else:
                saldo -= cantidad
                print(f"Has retirado {cantidad}. Saldo actual: {saldo}") # Una vez retirado le aparecerá la cantidad retirada y su saldo actual.
        except ValueError:
            print("Cantidad no válida, ingresa una cantidad válida.") #Si la cantidad no era valida para retirar le pedira que ingrese una cantidad válida

#Aquí es para la opción e mostrar saldo (3), que sirve para mostrar el saldo actual
    elif opcion == "3":
        print(f"Saldo actual: {saldo}") #Aquí te mostrará el saldo actual

#Aquí es para mostrar la opción de salir (4)
    elif opcion == "4":
        print("Saliendo del banco.") #Aquí te mostrará el mensaje de que a salido del banco.
        break

    else:
        print("Opción no válida. Elige una opción entre 1 y 4.") #Este mensaje aparecé cuando no  has elgido ninguna opción correcta en el menú de inicio (1-4).    

