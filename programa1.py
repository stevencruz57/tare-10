# primero creamos una matriz bidimensional 3*3
matriz = [
   [9,5,6],
   [3,4,2],
   [7,2,1]
]
# luego seleccionamos el valor que queremos encontrar
encontrar_valor=4
# utilizamos un for tanto para filas como para columnas, y hacemos que lean en el rango de matriz
for fila in range (len(matriz)):
 for columna in range(len(matriz)):
# usamos if para encontrar nuestro valor y print para mandar un mensaje de la posición del valor a encontrar
  if matriz [fila][columna]==encontrar_valor:
    print(f"la posición es ({fila},{columna})")
    break

