# primero creamos una matriz bidimensional 3*3
matriz = [
   [9,5,6],
   [3,4,2],
   [7,2,1]
]

encontrar_valor=4

for fila in range (len(matriz)):
 for columna in range(len(matriz)):
  if matriz [fila][columna]==encontrar_valor:
    print(f"la posición es ({fila},{columna})")
    break

