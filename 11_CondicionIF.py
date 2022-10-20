print("*******************************")
print('*    Welcome to Calculator    *')
print("*******************************")
print('1. Suma')
print('2. Resta')
print('3. Division')
print('4. Multiplication')
print('5. Potencia')
print('0. Salir')
print("-----------------------------------")
op = int(input('¿Selecciona una Opción?: '))
print("-----------------------------------")

if op >=1 and op <=5:
    a = int(input("Digita un numero: \n"))
    b = int(input("Digita un numero: \n"))

    if op == 1:
        suma = a + b
        print(f"La suma es: {suma}")
    elif op == 2:
        resta = a - b
        print(f"La Resta es: {resta}")
    elif op == 3:
        division = a / b
        print(f"La División es: {division}")
    elif op == 4:
        multiplication = a * b
        print(f"La Multiplicación es: {multiplication}")
    elif op == 5:
        potencia = a ** b
        print(f"La Potencia es: {potencia}")
    else:
        print("")
else:
    print("Good bye")


# print("Banco Central de Reserva del Perú")
# saldo = float(input('¿Cuánto va a depositar a su Cuenta Financiera?: '))
#
# print("1. Deposito")
# print("2. Retiro")
# print("3. Transferencia")
#
# op = int(input("Eliga Opción: "))
#
# if op >=1 and op <=3:
#
#     if op == 1:
#         deposito = float(input("Cuanto desea Depositar a su Cuenta: "))
#         saldo = saldo + deposito
#         print(f"Su saldo total es de: {saldo}")
#     elif op == 2:
#         retiro = float(input("Cuanto desea Retirar de su Cuenta: "))
#         saldo = saldo - retiro
#         print(f"Su saldo total es de: {saldo}")
#     elif op == 3:
#         cuentanueva = int(input("Ingrese el numero de Cuenta: "))
#         tranferencia = float(input("Ingrese el monto a Transferir: "))
#         saldo = saldo - tranferencia
#         print(f"Su saldo total es de {saldo}")
#     else:
#         print("")
# else:
#     print("Good Bye!")


