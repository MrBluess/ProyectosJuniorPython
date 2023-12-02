""" Par o impar
Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000

Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.

Ejemplo:

Mensaje que se muestra: ¿En qué número estás pensando?
Entrada: 25
Salida: ¡Es un número impar! ¿Puedes añadir otro? """ 


print("Bienvenido a Par o Impar\nPor favor selecciona un numero entre el 1 y 1000")

# Utiliza input() para obtener la entrada del usuario y conviértelo a entero
num_select = int(input())

# Verifica si el número es par o impar usando el operador de módulo
if 1 <= num_select <= 1000:
    if num_select % 2 == 0:
        print(f"{num_select} es un número par.")
    else:
        print(f"{num_select} es un número impar.")
else:
    print("No sea payaso")
