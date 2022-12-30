print("bienvenido a mi computador")

playing = input("quieres jugar ?")

if playing != "yes":
    quit()
    
print("okey juguemos")
score = 0 
 

pregunta = input("pára que sirve un cpu?")
if pregunta == 'proceso central':
    print("correcto!")
    score +=1
else:
    print("incorrecto")    

pregunta = input("para que sirven los perifericos?")
if pregunta == 'elementos de entrada y salida de la pc':
    print("correcto!")
    score +=1
else:
    print("incorrecto") 
    
    pregunta = input("para que sirve un programa de pc?")
if pregunta == 'para ejecutar procesos dentro de la misma':
    print("correcto!")
    score +=1
else:
    print("incorrecto") 
    
    pregunta = input("que es un hardware?")
if pregunta == 'memoria central de la pc':
    print("correcto!")
    score +=1
else:
    print("incorrecto") 
    
print("obtuviste" + str(score) + "preguntas correctas ")
print("obtuviste" + str((score / 4) * 100) + "%.")
