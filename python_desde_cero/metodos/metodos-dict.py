diccionario = {
    'nombre': 'Camilo',
    'apellido': 'Rodriguez',
    'edad': 25,
    'altura': 1.65
}

#el metodo keys() devuelve las claves del diccionario, en este caso devuelve un objeto 
# dict_keys que contiene todas las claves del diccionario.
clave = diccionario.keys()
print(clave)

#el metodo get() devuelve el valor de una clave especifica del diccionario, si no encuentra la clave devuelve None.
valor = diccionario.get('nombre')
print(valor)

#el metodo pop() elimina una clave y su valor del diccionario, si no encuentra la clave devuelve un error.
clave_eliminada = diccionario.pop('apellido')
print(clave_eliminada)

#metodo items() devuelve un objeto dict_items que contiene una lista de tuplas con las claves y valores del diccionario.
items = diccionario.items()
print(items)

#el metodo clear() elimina todos los elementos del diccionario, dejandolo vacio.
#diccionario.clear()
#print(diccionario)

#el metodo update() actualiza el diccionario con los elementos de otro diccionario, si la clave ya existe se actualiza su valor.
diccionario.update({'nombre': 'Juan', 'edad': 30})
print(diccionario)

#el metodo popitem() elimina el ultimo elemento agregado al diccionario y lo devuelve como una tupla,
# si el diccionario esta vacio devuelve un error.
clave_valor_eliminada = diccionario.popitem()
print(clave_valor_eliminada)