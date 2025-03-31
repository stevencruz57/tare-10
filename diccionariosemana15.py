# realizaremos un ejemplo sobre diciomarios, empezaremps nombrando nuestro diccionario y agrgando nuestros codigo_valor
informacion_personal={"Nombre":"Steven","Edad":18,"Ciudad":"Gualaceo"}
print(informacion_personal)
# luego la actividad requiiere que modifiquemos el codigo_valor Ciudad y lo cambiemos por otra
informacion_personal["Ciudad"]= "Quito"
print(informacion_personal)
# el siguiente paso es agrgar el codigo_valor Profesion
informacion_personal["Profesion"]="Barbero"
print(informacion_personal)
# luego necesitamos eliminar el codigo_valor Edad
del informacion_personal["Edad"]
print(informacion_personal)
# para finalizar debemos verificar si el codigo valor Telefono se encuentra dentro de nuestros diccionario, si este no esta lo agrgamos
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"]= 9354758362
# con la ayuda de else damos un mensaje avisando que Telefono si se encuentra dentro de nuestro diccionario en caso de que este si se encuntre agregado
else:
    if "Telefono"  in informacion_personal:
     print("Este codigo valor si se encuentra dentro del dicionario")