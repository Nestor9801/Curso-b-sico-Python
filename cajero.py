print(" #####CAJERO BANCO NACIONAL #####")
print(" ##########  ####  ##############")
print(" #########  ######  #############")
print(" ######### ########  ############")

#Solicitar al usuario que ingrese su contraseña

password = input("Ingrese contraseña:")
set_password = '1234'

saldo = 10000
usuarios_transferencia = ["Laura","Marcos","Pedro"]



if password == set_password:
    print("Contraseña Correcta...")
    flag = True
    while flag:
        print("Ingreseando al sistema...")
        print("#########  MENU #########")
        print("##### 1) Depositar ######")
        print("##### 2) Consultar ######")
        print("##### 3) Retirar   ######")
        print("##### 4) Transferir######")
        print("##### 5) Salir     ######")
        opcion = input("Ingresa una opción del menu:")

        if opcion == '1':
            print("Has elegido la opcion Depositar")
            monto = float(input("Ingresa el monto que deseas depositar:"))
            saldo = saldo + monto
            print("Tu saldo actual es:", saldo)
        elif opcion == '2':
            print("Has elegido opcion Consultar")
            print("Tu saldo actual es de:", saldo)
        elif opcion == '3':
            print("Tu saldo actual es:", saldo)
            monto_retiro = float(input("Ingresa la cantidad que deseas retirar:"))
            if monto_retiro > saldo:
                print("Saldo insuficiente")
            else:
                saldo = saldo - monto_retiro
                print("Tu saldo después del retiro es:", saldo)
        elif opcion == '4':
            valor_usuario = input("Ingresa el usuario al que quieres transferir:")
            if valor_usuario in usuarios_transferencia:
                print("usuario validado")
                valor_transfer = float(input("Ingrese cantidad a transferir:"))
                print("Tu transferencia ha sido exitosa")
                saldo = saldo - valor_transfer
            else:
                print("No existe usuario")
                response = input("¿Desea agregar uno? (S/N)")
                if response == 'S' or response == 's':
                    new_user = input("Ingresa usuario Nuevo:")
                    usuarios_transferencia.append(new_user)
                    print("Usuario agregado correctamente...")
                elif response == 'N' or response == 'n':
                    print("Saliendo ...")
                else:
                    print("Opcion no valida")
        elif opcion == '5':
            flag = False
            print("Saliendo...")
        else:
            print("Tu opción no esta registrada")
    
else:
    print("Contraseña incorrecta, favor de validar")
    




####WHILE

"""
while -----> esta sometido a una condición
Repetir hasta que no se cumpla dicha condición
### a = 4
while a < 3:
    print(a)

"""
