#3. Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

numero=int(input("Ingrese un número entero: "))
sumatodos= 0
sumapos= 0
mayor = 0
cantpares = int()
cantimpares = int()
cantprimos = int()
lista=[numero]

while numero != 0:
    sumatodos = sumatodos+numero

    if numero>0:
        sumapos = sumapos + numero

    if numero>mayor:
            mayor=numero

    divisor = 0
    cantdivisibles = 0

    while divisor < numero:
        divisor = divisor +1
        if numero % divisor == 0 :
            cantdivisibles += 1
            if cantdivisibles > 2:
                break
            
    if cantdivisibles == 2:
        cantprimos = cantprimos + 1

    numero=int(input("Ingrese un número entero: "))       
    
    if numero>0:  
        lista.append(numero)

for item in lista:
    if item % 2 == 0:
        cantpares+=1
    else:
        cantimpares+=1

print("La suma de todos los numeros de la lista", lista, "es ->",sumatodos)
print("La suma de los números positivos de la lista", lista, "es ->",sumapos)
print("El mayor de los números positivos de la lista", lista, " es ->",mayor)
print("La lista", lista, "contiene", cantpares,"pares y", cantimpares , "impares")
print("La lista", lista ,"contiene", cantprimos ,"números primos" )

