"------------------------------Variables simples--------------------------------"

"Variables:"                  "Valor de las variables:"

nombre             =               "Camilo"

A                  =                  5
B                  =                  5
C                  =                 (A + B)

"------------Concatenación de variables---------------"
'''se pueden concatenar variables para una respuesta, 
lo reocmenable es usar la (f) para comvertir todo tipo de datos
a un formato de salida tipo texto.
'''

Nombre = "Camilo"
FraseConcatenada = (f"hola, {Nombre} ¿como estas?")
print(FraseConcatenada)

"------------------Formas de manejo de variables-------------------------"

'''se una (del) antes de cualquier variable parta eliminar dicha variable
(esto funciona en forma de cascada segun donde pongas esta funcion funciona o no)
'''

'''Apellido1 = "Rodriguez"
del Apellido1
Frase1 = f"esta frase evidencia que del puede alterar la llamada de {Apellido1} segun donde se ubique la funcion "
print(Frase1)'''

Apellido2= "Rodriguez"
Frase1 = f"esta frase evidencia que del puede alterar la llamada de {Apellido2} segun donde se ubique la funcion "
del Apellido2
print(Frase1)

'''Tambien se puede usar la validacion del uso de ciertas variables y textos en las salidas mediante salidas de booleanos
confirmando si existe o no algun caracter mediante las funciones ((in) o (not in))
'''

Frase3 = "Prueba de existencia de caracteres dentro de esta frase"
print("existencia de caracteres" in Frase3)
print("no existe" in Frase3)
print("no existe" not in Frase3)

# Recomendable usar snake_case par trabajar en python

snake_case = "esta es la manera mas recomendable para nombrar una variable."