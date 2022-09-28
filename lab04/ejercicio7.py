def calcularCalificación(puntaje):
    if(puntaje >=0.9 and puntaje <=1.0):
        calificación="Sobresaliente"
    elif(puntaje>=0.8 and puntaje<0.9):
        calificación="Notable"
    elif(puntaje>=0.7 and puntaje <0.8):
        calificación="Bien"
    elif(puntaje >=0.6 and puntaje <0.7):
        calificación="Insufuciente"
    else:
        calificación="Puntaje no válido"
    return calificación

try:
    puntaje=float(input("Ingresela calificación(0.01-1.00: "))
    calificación=calcularCalificación(puntaje)
    print("El grado de su calificación es:", calificación)
except:
    print("Error, debe ingresar un valornumérico")
