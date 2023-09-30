numero=int(input("Ingrese un número entero positivo: "))

lista=[numero]
sumapares = 0
sumaimpares = 0
string = ""

while numero != 0:
   cantpares=0
   cantimpares=0
   string = str(numero)

   for x in string:
      print(x)

      if int(x) % 2 == 0:
         cantpares=cantpares + 1
      else:
         cantimpares=cantimpares + 1

   print("El número: ",numero," tiene ",cantpares," números pares y ",cantimpares," números impares")

   sumapares=sumapares + cantpares
   sumaimpares=sumaimpares + cantimpares
   numero=int(input("Ingrese un número entero positivo: "))

   
print("El número de dígitos pares es: ", sumapares, " y la cantidad de dígitos impares es: ", sumaimpares)