print(" ")#imprime un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W")#imprime mi nombre completo con mi grado y grupo
print(" ")#imprime un espacio en blanco
thislist = []#crea una lista de mis materias
print("Hola buenas tardes, dias y noches estas aqui para saber si ganaste la loteria verdad? pues entonces tienes que poner tu numero de loteria de solo 4 dijitos")#imprime el texto dentro de las ""
persona1 = input(" cual es el numero de loteria que te toco:")#le damos valor a la variable persona1
per1 = int(persona1)#la variable persona1 se combierte en una variable
thislist.append(per1)#agregamos a la lista la variable persona
persona2 = input("cual es el numero de loteria que te toco")#le damos valor a la variable persona2
per2 = int(persona2)#la variable persona1 se combierte en una variable
thislist.append(per2)#agregamos a la lista la variable persona
persona3 = input("cual es el numero de loteria que te toco")#le damos valor a la variable persona3
per3 = int(persona3)#la variable persona1 se combierte en una variable
thislist.append(per3)#agregamos a la lista la variable persona
thislist.sort()#ordenamos de menor a mayor
print("estos son los 3 boletos de loteria que habia del menor al mayor:")#imprimimos la palabra dentro de las ""
print(thislist)#imprimimos la lista
