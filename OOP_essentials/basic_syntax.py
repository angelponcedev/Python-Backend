print('hola mundo')

if True:
    print('Hola este es un if')

#Lista de python
lista = [1,2,3,4,5,"Hola",False]

#tupla de pyhton
tupla  = (1,2,3,4,5,"Hola",False)

lista.append("Agregado")

# a las tuplas no se le pueden agregar datos despues que se incializan
# tupla.append("Agregado")

print(lista)
print(tupla)

# diccionario de python (enum)
diccionario = {
    "uno": 1,
    "dos": 2
}

print(diccionario["uno"])