# se usan listas para agrupar datos (NOTA: en las listas se oueden modificar las variabes) por ejemplo:
#posiciones: 0          1      2    3
lista = ["camilo","Rodriguez",25, 1.65]
lista[3] = 30 # esto es valido en python
print(lista[1])

#Tambien se usan tuplas, es tambien un conjunto de datos igual a las listas, solo que ne estas no se pueden modificar las variables.
#posiciones: 0          1      2    3
tupla = ("camilo","Rodriguez",25, 1.65)
tupla[3] = 30 #esto no es valido en python
print(tupla[3])

#Tambien se usan los consjuntos, estos en general no deja acceder al indice de cada dato, ademas de que no se pueden repetir datos.
conjunto = {"camilo","Rodriguez",25, 1.65}
conjunto[3] = 30 #esto no es valido en python
print(tupla[3])

#Tambien se usan diccionarios, en este caso no se maneja con numero de indice si no por nombre de la variable, y devuleve el valor de la misma.
#La estructura es (Clave : Valor)
diccionario = {
    'nombre' :'Camilo',
    'Apellido' : 'Rodriguez',
    'Edad' : 25,
    'Altura' : 1.65
}