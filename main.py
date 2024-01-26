## ---------------------------------
## ---- Ejercicio 1 ---- 
## ---------------------------------

# Impresión en consola
print("Hola Mundo")

# ---- Datos primitivos ----
#1. String 
texto = "Campus" 
print(texto)
print(type(texto))
#2. Int
numeroEntero = 1
print(numeroEntero)
#3. Float
numeroDecimal = 3.1
print(numeroDecimal)
#4. Double
numeroDecimalLargo = 3.14167582737283
print(numeroDecimalLargo)
#5. Boolean
booleano = True
print(booleano)
# ---- Entradas parte del usuario ----
entradaUsuario = input("Ingresa tu nombre: ")
print ("Tu nombre es: ", entradaUsuario)
# ---- Entradas parte del usuario con definición de tipo de dato primitivo ----
entradaUsuarioNumero = input("Ingresa tu edad: ")
numeroFinal = int(entradaUsuarioNumero)
print ("Tu edad es: ", numeroFinal)
# ---- Ciclos ----
#Ciclo for
for i in range (5,10,2):#for contador in range (desde,hasta,pasos):
    print (i)
#Ciclo while
booleanito = True
while booleanito == True:#while condición_a_cumplir :
    print("sigo vivo")
    booleanito = False 
# ---- Condicionales ----
texto1 = "campus"
if texto1 == "campus":
    print ("Soy campus")
else:
    print ("No soy campus")
# ---- Listas (Arrays) ----
#Listas
nombres = ["pedro","morocho","yeir","coste","pedraza"] #Crea una lista de nombres
print("Lista de nombres: ",nombres)
firstElement = nombres[0]#Acceder a elementos individuales 
secondElement = nombres[1]
print("First Element:", firstElement)
print("SecondElement:", secondElement)
nombres[3]="javier" #Modificar el elemento de la posicion indicada 
print("El elemento fue modificado: ", nombres)
nombres.append("sarawel")#Añadir en la ultima posición un elemento nuevo 
print("Lista después de añadir elementos: ", nombres)
longi = len(nombres)#Cantidad de posiciones 
print("Longitud de la lista: ",longi)
# ---- Funciones ----
#Sin parámetros y sin retorno 
def saludar():#DEFinir la funcion su nombre()
    print("Hey, good morning mondaes.")
## Llamado a la funcion 
saludar()
#Sin parámetros y con retorno
def obtengoSaludo():
    return "Hi, welcome"
##Llamo a la función dentro de una variable 
llamarFuncion = obtengoSaludo()
print(llamarFuncion)
#Con parámetros y sin retorno 
def saludar(name):
    print(f"Hi, {name} Welcome")
saludar("Majo")
#Con parámetros y con retorno 
def obtengoSaludi(name):
    return f"Hey, {name} Welcome"
mensajillo = obtengoSaludi("Maria") #Llamo la función y la variable donde tengo almacenado el dato 
print(mensajillo)


## Desarrollado por BRAYAN YESID LINDARTE ANAYA - 1010120365