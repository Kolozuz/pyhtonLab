
lista = list()

cantprimos = 0
cantdivisibles = int()

numero = int(input("Ingrese un número entero positivo: "))

while numero != 0:


    divisor = 1
    cantdivisibles = 0

    while divisor < numero:
        divisor = divisor +1
        if numero % divisor == 0 :
            cantdivisibles += 1
            if cantdivisibles > 2:
                break
            
    if cantdivisibles == 2:
        cantprimos = cantprimos + 1

    if numero > 0:  
        lista.append(numero)

    numero = int(input("Ingrese un número entero positivo: "))
    
    
# for x in lista:
#     divisor = 0
#     cantdivisibles = 0
    
#     while divisor < x:
#         divisor = divisor +1
#         if x % divisor == 0 :
#             cantdivisibles += 1
#             if cantdivisibles > 2:
#                 break
            
#     if cantdivisibles == 2:
#         cantprimos = cantprimos + 1


print("La lista", lista ,"contiene", cantprimos ,"números primos" )
