### Sentencia de Control IF, ELSE, ELIF####
"""
Las sentencias de control IF, permiten que un programa
ejecute instrucciones cuando se cumple una condición.

Sintáxis
### if condicion:
###----->identación (espacios), Python es un leguaje identado.
        proceso
##TIP: USAR TABULAR PARA LA IDENTACIÓN###
"""

#numero = int(input("Escribe un número positivo:"))
#Condición
"""
if numero > 0:
    print("El número ingresado es positivo")
if numero < 0:
    print("El número es negativo")

###Segunda Condición con IF y ELSE

if numero > 0: #------> Valida la parte Verdadera
    print("El numero que ingresaste es positivo")
else: #-----> Valida la parte Falsa
    print("Tu valor ingresado es negativo")
    print("Favor de ingresar un número correcto")
"""

### CALCULO DE AREA###
### VALIDACIón DE TIPO DE DATOS##
"""
print("Programa para calculo de área \n")
print("           TRIÁNGULO         \n")

altura = float(input("Ingrese el valor de la altura:"))
base = float(input("Ingrese el valor de la base:"))

##None ---> NULL ----> No tienen valor, no es igual a
##algun numero o a 0

if type(altura) == int or type(base) == int:
    print("Ingresa un valor válido")
else:
    print("CALCULANDO ÁREA ...")
    area = base * altura / 2
    print("El área del triángulo es: ",area)

"""
### CALCULO DEL IMC ###

print("Calculo del IMC")
print("Inicializando programa...")
peso = float(input("Ingresa el valor de tu peso en kg:"))
altura = float(input("Ingresa el valor de tu altura en mts:"))
imc = peso/(altura*altura)
print("tuvalor de IMC es igual a:",imc)
if imc < 18.5:
    print("Tienes desnutrición")
if imc > 18.5 and imc < 25:
    print("Tu peso es normal")
if imc > 25 and imc < 190:
    print("Tienes sobrepeso")
else:
    print("Tus datos fueron incorrectos")



#### MENU CAJERO AUTOMÁTICO ###

#####1) Consultar saldo ####
#####2) Retirar         ####
#####3) Transferir      ####
#####                   ####
#####                   ####
#####                   ####

    
