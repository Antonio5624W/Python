# Variables 
#Nombramiento de Variables
my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 3
print(my_int_variable)

my_int_to_variable = str(my_int_variable)
print(my_int_to_variable)
print(type(my_int_to_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_string_variable, my_int_to_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

# Algunas Funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea ¡Cuidado de abusar de esta sintaxis!
name, surname, alias, age = "Antonio", "Salazar", "Toño", 21
print("Me llamo:", name, surname, "Y tengo la edad de:",age, "Y mi alias es:",alias)


# Input
# Input es una funcion que permite recibir datos del usuario    
name = input("¿Cual es tu nombre? ")
age = input("¿Cuantos anios tienes? ")

print("Nombre al imprimirlo en consola: ", name)
print("Tu edad al imprimirlo en consola: ", age)


#cambiamos su tipo
name = 22
age= "Antonio"
print(name)
print(age)

# ?Forzamos el tipo de variable¿
address: str = "Mi direccion es: "
address = 5
address = 1.23
address = True
print(type(address))