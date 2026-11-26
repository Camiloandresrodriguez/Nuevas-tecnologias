#Estructura de metodos: (nombre_variable = Dato.Metodo(parametro), los parametros no siempre se requieren)

#metodo upper (convierte todas las letras en mayusculas)
cadena1 = "mayusculas"
upper = cadena1.upper()
print(upper)

#metodo lower (convierte todas las letras en minuscula)
cadena2 = "MINUSCULAS"
lower = cadena2.lower()
print(lower)

#metodo capitalize (convierte a primera letra en mayuscula)
cadena3 = "primera letra en mayuscula"
capitalize = cadena3.capitalize()
print(capitalize)

#metodo find (busca un dato dentro de una cadena mediante un parametro)devuelve la posicion, si no enucentra el dato devuelve -1
cadena4 = "busca un dato dentro de una cadena"
find = cadena4.find("dato")
print(find)

#metodo index(busca un dato dentro de una cadena mediante un parametro)devuelve la posicion,si no enucentra el dato devuelve un error
cadena5 = "busca un dato dentro de una cadena"
index = cadena5.index("dato")
#print(index)

#metodo isnumeric(valida si un dato es numerico o no, devolviendo asi un booleano de tipo true o false.)
cadena6 = "123456789"
isnumeric = cadena6.isnumeric()
print(isnumeric)

#metodo isalphanumeric(valida si un dato es numerico o no, devolviendo asi un booleano de tipo true o false.)
cadena7 = "Abcdefghijk"
isalphanumeric =  cadena7.isalpha()
print(isalphanumeric)

#metodo count (valida ciuantas veces aparece un dato en una cadena (coincidencias),devuleve el numero de veces que se repite el dato)
cadena8 = "busca cuantas coincidencias hay en esta cadena"
count = cadena8.count("a")
print(count)

#funcion len (cuenta cuantos caracteres tiene una cadena), devuleve el numero de caracteres encontrados.
cadena9 = "cuenta cuantos caracteres tiene esta cadena"
len = len(cadena9)
print(len)

#metodo startswith verifica como cominnza el primer dato de una cadena y retorna verdadero o falso segun el paremtro arrojado
cadena10 = "esta cadena empieza asi"
startswith = cadena10.startswith("esta")
print(startswith)

#metodo endswith verifica como termina el ultimo dato de una cadena y retorna verdadero o falso segun el paremtro arrojado
cadena11 = "esta cadena termina asi"
endswith = cadena11.endswith("asi")
print(endswith)