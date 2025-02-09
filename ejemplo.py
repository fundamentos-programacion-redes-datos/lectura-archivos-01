"""
    Lectura de archivos
"""

# 1. Crear la variable que manejará el archivo, a través de open
#

archivo = open("data/informacion-01.txt", "r")

# Donde:
# data es la carpeta donde está el archivo
# mis-datos.txt, es el nombre del archivo que se desea leer
# "r" es el modo lectura que deseamos usar para manejar el archivo

# se usa el método/función readlines, que ubica cada línea del archivo en una
# posición de una lista
textos = archivo.readlines()
# se imprime texto a esta altura se tiene
# ['ID,Nombre,Apellido,Edad,Departamento,Salario\n',
#  '1,Juan,Pérez,30,Contabilidad,2500\n',
# '2,María,López,27,Recursos Humanos,2800\n',
# '3,Carlos,García,35,IT,3200\n',
# '4,Ana,Rodríguez,29,Marketing,2700\n']
#
# Donde se observa que cada posición es una cadena, el método usado
# agrega un salto de línea, que se lo debería eliminar para evitar 
# problemas con los datos

# Se usa una lista compresa de python - list comprehension
# que permite aplicar la función strip (para elminar espacios espacios y 
# saltos de línea de una cadena) a cada iteración (de tipo cadena) 
# de la lista.
textos = [l.strip() for l in textos]


# Cerrar el archivo después de la lectura para liberar recursos del sistema
archivo.close()  # Se cierra el archivo para evitar bloqueos o fugas de memoria

# se presenta cada posición de la lista en pantalla

for t in textos:
    print(t)

print("---------------------------")
# la salida es:
#
# ID,Nombre,Apellido,Edad,Departamento,Salario
# 1,Juan,Pérez,30,Contabilidad,2500
# 2,María,López,27,Recursos Humanos,2800
# 3,Carlos,García,35,IT,3200
# 4,Ana,Rodríguez,29,Marketing,2700

# Al considerar que el archivo tiene información estructurada
# Se puede hacer lo siguiente por cada iteración

for t in textos:
    # se almacena en una variable mi_cadena, el valor de cada 
    # iteración, a la cual se le aplica la función split,
    # que permite separar la cadena mediante el caracter
    # coma (,) en una lista
    mi_cadena = t.split(",") # mi_cadena es una lista ahora
    for v in mi_cadena:
        print(v)
    print("###################")


print("---------------------------")

"""
La salida es:

ID
Nombre
Apellido
Edad
Departamento
Salario
###################
1
Juan
Pérez
30
Contabilidad
2500
###################
2
María
López
27
Recursos Humanos
2800
###################
3
Carlos
García
35
IT
3200
###################
4
Ana
Rodríguez
29
Marketing
2700
###################
---------------------------
"""
