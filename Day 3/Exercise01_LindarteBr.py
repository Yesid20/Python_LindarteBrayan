## -------------------------------
## ---- Ejercicio 1 ----
## -------------------------------
cajero = int(input("Digite una cantidad de 1 a 1000: "))
opera = int(cajero/10) # Divide entre 10 para obtener cantidad de esta denominación
x = cajero - (opera*10) 
operad = int(cajero/5) # Divide entre 5 para obtener cantidad de esta denominación
a = int(x/5)
operador = int(cajero/1)
c = int(a/1)
print("Su cantidad de billetes de 10 son: ", opera)
print(f"Su cantidad de billetes de 5 es: {a}")
print(f"Su cantidad en billetes de 1 es {c}") 
print(f"Cantidad de billetes totales:{opera+a+c} ")
## Desarollado por BRAYAN YESID LINDARTE ANAYA - 1010120365

