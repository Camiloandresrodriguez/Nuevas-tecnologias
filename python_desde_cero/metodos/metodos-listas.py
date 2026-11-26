#Se crea una lista usando el metodo list.
lista = list(['manzana', 'banana', 'cereza'])
print(lista)

#Dvuelve la cantidad de elementos que tiene una list, usando el metodo len
cantidad_elementos = len(lista)
print(cantidad_elementos)

# append agrega un valor nuevo a la lista creada.
lista.append('naranja')
print(lista)

# insert agrega un valor nuevo a la lista creada en una posicion especifica.
lista.insert(1, 'kiwi')
print(lista)

# extend agrega varios valores nuevos a la lista creada.
lista.extend(['pera', 'uva'])
print(lista)

# pop elimina un valor de la lista creada en una posicion especifica, Nota si se elimina el indice 0 se elimina la primera, 
# si es -1 se elimina la ultima, si es 2 se elimina la tercera y asi sucesivamente.
lista.pop(2)
print(lista)

# remove elimina un valor de la lista creada, se elimina la primera coincidencia encontrada.
lista.remove('pera')
print(lista)

# clear elimina todos los valores de la lista creada.
lista.clear()

# del metodo sort ordena los valores de la lista creada de menor a mayor.
lista2 = [3, 1, 4, 2]
lista2.sort()
print(lista2)
# nota si se le añade como paremetro reverse=True, ordena de mayor a menor.
lista2.sort(reverse=True)
print(lista2)

# reverse invierte el orden de los valores de la lista creada.
lista2.reverse()
print(lista2)

#index devuelve la posicion de un valor en la lista creada, si no encuentra el valor devuelve un error.
posicion = lista2.index(4)
print(posicion)