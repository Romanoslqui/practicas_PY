"""
    las listas nos permiten almacenar informacion
    en un lugar, la cantidad que desee: ya sea pocos 
    elemntos o millones de elementos.

    Una lista es una colección de items (elementos) que tienen
    un orden particular. Se pueden crear listas que incluyan
    strings, números, los nombres de las personas de tu familia, 
    etc. podemos almacenar (los tipos de datos permitidos en 
    Python) lo que queramos en una lista.
    
    Se recomienda nombrar una variable en plural, si la variable 
    es una lista.
    
    En Python, los corchetes [] indican una lista, sus elementos 
    se separan por comas.
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
"""

    Accessando a los elementos de una lista.
    
"""
# Para acceder a cualquier elemento de una lista
print(bicycles[0].title())
print(bicycles[1].lower())
print(bicycles[2].upper())

message = f"my fisrta bicyclese was a {bicycles[0].upper()}"
print(message)
