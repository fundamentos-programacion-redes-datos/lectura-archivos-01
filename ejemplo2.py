"""
    Lectura de archivos
"""

# 1. Abrir el archivo de texto en modo lectura ("r")
archivo = open("data/informacion-01.txt", "r")

# 2. Leer todas las líneas del archivo y almacenarlas en una lista
textos = archivo.readlines()

# 3. Cerrar el archivo después de la lectura para liberar recursos del sistema
archivo.close()  

# 4. Eliminar los saltos de línea "\n" en cada línea del archivo usando lista por comprensión
textos = [l.strip() for l in textos]

# 5. Eliminar la primera línea (encabezados) del archivo
textos = textos[1:]

# 6. Inicializar una variable para almacenar la suma de los salarios
suma_salarios = 0

# 7. Recorrer cada línea del archivo procesado
for t in textos:
    # 7.1. Separar la línea en una lista utilizando la coma como delimitador
    mi_cadena = t.split(",")  
    # Ejemplo de la lista generada en cada iteración:
    # ['1', 'Juan', 'Pérez', '30', 'Contabilidad', '2500']
    print(t)
    # 7.2. Extraer el valor de la columna "Salario" (posición 5 en la lista)
    valor = mi_cadena[5]

    # 7.3. Convertir el valor de salario de string a float
    valor = float(valor)

    # 7.4. Acumular el salario en la variable "suma_salarios"
    suma_salarios = suma_salarios + valor

# 8. Mostrar el resultado de la suma de todos los salarios
print(f"La suma de salarios es: {suma_salarios}")

"""
Salida esperada:
La suma de salarios es: 11200.0
"""

