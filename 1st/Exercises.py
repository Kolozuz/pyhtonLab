# --------------- ~ Ejercicio 1 ~ --------------- #
print("\n# --------------- ~ Ejercicio 1 ~ --------------- # \n > ", end=" ")
CadenaCaract = "SETI"
SETI="SETI"

if CadenaCaract == SETI:
    print("es igual a SETI")
else:
	print("no es igual a SETI")


# --------------- ~ Ejercicio 2 ~ --------------- #
print("\n# --------------- ~ Ejercicio 2 ~ --------------- # \n  > ", end=" ")
num1 = 10
num2 = 9

if num1 == num2:
	print (num1*num2)
else:
	if num1 > num2:
		print (num1-num2)
	else:
		print (num1+num2)


# --------------- ~ Ejercicio 3 ~ --------------- # 
#(El número mayor de los tres)
print("\n# --------------- ~ Ejercicio 3 ~ --------------- # \n  > ", end=" ")
num1 = 2
num2 = 3
num3 = 1

if num1 > num2 and num1 > num3:
    print("El numero mayor es: ", num1)
elif num2 > num3:
    print("El numero mayor es: ", num2)
else:
    print("El numero mayor es: ", num3)
    

# --------------- ~ Ejercicio 4 ~ --------------- #
print("\n# --------------- ~ Ejercicio 4 ~ --------------- # \n  > ", end=" ")
sueldomensual=1000000
tiempo=2

if tiempo<1:
   porcentaje=5
elif tiempo<2:
   porcentaje=7
elif tiempo<5:
   porcentaje=10
elif tiempo<10:
   porcentaje=15
else:
   porcentaje=20

utilidad=sueldomensual*porcentaje/100

print('El empleado tiene una utilidad de',utilidad)


# --------------- ~ Ejercicio 5 ~ --------------- #
print("\n# --------------- ~ Ejercicio 5 ~ --------------- # \n  > ", end=" ")
computadoras = 8
precio = 1100000
descuento = 0

if computadoras < 5: # alternativa: uso de switch
	descuento = 0.1
if computadoras >= 5 and computadoras < 10:
	descuento = 0.2
if computadoras >= 10:
	descuento = 0.4

subtotal = computadoras*precio
total = subtotal*descuento

print("Subtotal  para", computadoras, "computadoras -> ", subtotal, "\n  >  Total (con descuento) es de -> ", total)


# --------------- ~ Ejercicio 6 ~ --------------- #
print("\n# --------------- ~ Ejercicio 6 ~ --------------- # \n  > ", end=" ")
canthoras = 50
sueldobase = 20
sueldoextra = 25

if canthoras <= 40:
   salario = sueldobase * canthoras
else:
   horasextras = canthoras - 40
   salario = (sueldobase * 40) + (sueldoextra * horasextras)

print("El salario del empleado es: ",salario)


# --------------- ~ Ejercicio 7 ~ --------------- #
print("\n# --------------- ~ Ejercicio 7 ~ --------------- # \n  > ", end=" ")
a1 = 4
a2 = 5
a3 = 7

b1 = 2
b2 = 1
b3 = 4 # alternativa: uso de arrays

inter = ""

if a1==b1 or a1==b2 or a1==b3: # alternativa para evaluar varias condiciones para una misma variable: uso de Switch
   inter=a1

if a2==b1 or a2==b2 or a2==b3:
   inter=a2

if a3==b1 or a3==b2 or a3==b3:
   inter=a3

if inter: # las variables str vacias equivalen a false, si no estan vacias equivale a true
   print("La intersección de los conjuntos A y B es: ",inter)
else:  
   print("No existe ningún número que pertenezca a los dos conjuntos") 


# --------------- ~ Ejercicio 8 ~ --------------- #
print("\n# --------------- ~ Ejercicio 8 ~ --------------- # \n  > ", end=" ")
num = 1 #int(input("type a number"))
absolute_value = 0

if num >= 0:
     absolute_value = num
else:
     absolute_value = num*-1

print("El valor absoluto de", num, "es", absolute_value)

print("\n")


# --------------- ~ Ejercicio 9 ~ --------------- #
print("\n# --------------- ~ Ejercicio 9 ~ --------------- # \n  > ", end=" ")
var = "a" # input("Type a letter")
es_una_vocal = False

if var == "a" or var == "e" or var == "i" or var == "o" or var == "u": # alternatva: Switch, Loop de un array etc
   es_una_vocal = True

if len(var) == 1: # Metodo len() nos dice la longitud del objeto que le pasemos como parametro
   if es_una_vocal == True :
        print("Es una vocal!")
   else:
        print("No es vocal!")
else:
   print("No puede procesarse el dato")


# --------------- ~ Ejercicio 10 ~ --------------- #
print("\n# --------------- ~ Ejercicio 10 ~ --------------- # \n  > ", end=" ")
num = 1 # input("Type a number")

if num % 2 == 0:           # Operador % retorna el residuo de una division, si al dividir
     print(num, "Es par")  # un numero entre 2 el residuo es igual a 1, entonces es un número primo,
else:                      # si no hay residuo (0) entonces el numero es par.
     print(num, "Es impar")
       
                           


     