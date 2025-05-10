# -*- coding: utf-8 -*-


import os
import subprocess

# Entradas simuladas como si fueran escritas por un usuario
inputs = [
    # Agregar 1 tarea
    "2\n", "Comprar pan\n", "Ir a la tienda del barrio\n",
    
    # Mostrar tareas
    "1\n",
    
    # Agregar 2 tarea
    "2\n", "Hacer ejercicio\n", "30 minutos de cardio\n",
    
    # Mostrar tareas
    "1\n",

    # Agregar 3 tarea
    "2\n", "Lavar ropa\n", "Ropa blanca y de color\n",
    
    # Mostrar tareas
    "1\n",

    # Agregar 4 tarea
    "2\n", "Estudiar Python\n", "Repasar estructuras de datos\n",
    
    # Mostrar tareas
    "1\n",

    
    "2\n", "Sacar la basura\n", "Antes de las 8 pm\n",
    
    # Mostrar tareas
    "1\n",


    # Mostrar tareas
    "1\n",

    # Marcar como hechas la 1 y la 3
    "5\n", "1\n",
    "5\n", "3\n",

    # Mostrar tareas
    "1\n",

    # Editar tarea 4
    "3\n", "4\n", "Estudiar Python avanzado\n", "Practicar diccionarios y listas\n",

    # Mostrar tareas
    "1\n",

    # Marcar tarea 4 como hecha
    "5\n", "4\n",

    # Mostrar tareas
    "1\n",

    # Salir
    "6\n"
]


# Convertimos los inputs en una sola cadena codificada
user_input = ''.join(inputs).encode()

# Ejecutamos el programa main.py
process = subprocess.Popen(["python", os.path.join("..", "main.py")], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Enviamos los comandos simulados al programa
output, error = process.communicate(input=user_input)

# Mostramos la salida completa del programa
try:
    print(output.decode("utf-8"))
except UnicodeDecodeError:
    print(output.decode("latin-1"))


# Si hubo errores, los mostramos también
if error:
    print("ERRORES:")
    print(error.decode())
