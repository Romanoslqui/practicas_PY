# Concatenacion
#uso por orden 
first_name = "eloyi"
last_name = "romanolshqui"
full_name = first_name +" " + last_name 
print(full_name.title())

print("hola".upper(), first_name + " " + last_name)
"""
    el white space se refieren a cualquier 
    caracter que no se imprime, es decir, un espacio
    tabulador(\t) y finales de linea (\n)

    los whitepaces se utilizan comunmente 
    para organisar el codigo de modo legible 
"""
print("################################")
print("python")

print("saluditos\t\tpyton")
print("\nhola \nsaludos \ngrasa")

# f-strings - comvierte una veriable es string 
famous_person = "Romanoslqui"
age = 18
message = f"{famous_person} una vez dijo: python es amor"
print(message)
message_2 = f"{famous_person} tiene {age} años"
print(message_2) 
posdat = "posdata: es hermoso. "
print(posdat.title())

print("####################")
#metodo join
"""
    Junta dstintas ileras de dentro de 
    una sola varible y las junto 
"""
joinswords = f"hola", str(famous_person), "graso"
text = " ".join(joinswords)
print(text)

"""
    El Bild -in "str" comviente cualquier variable
    un string 
"""
print("ISACA COBIT 2019 Framework".title())
