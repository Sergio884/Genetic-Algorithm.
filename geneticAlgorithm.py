import random
def evaluar(x,y,z):
    return 2*x + 3*y - 5*z + 1

def generarIndividuo():
    individuo = []
    for i in range(3):
        individuo.append(random.randint(-9,9))

    return individuo

def generarPoblacion(cantidad):
    poblacion = []
    for i in range(cantidad):        
        poblacion.append(generarIndividuo())

    return poblacion

def fitness(individuo):
    valor = evaluar(individuo[0],individuo[1],individuo[2])
    return abs(valor)

def seleccionar(poblacion):
    mejores = []
    for individuo in poblacion:
        mejores.append((fitness(individuo),individuo))
    mejores.sort()        
    return mejores[:5]

def reproducir(mejores):
    pareja = random.sample(mejores,2)
    hijo = []
    hijo.append(pareja[0][1][0])
    hijo.append(pareja[1][1][1])
    hijo.append(pareja[1][1][2])    
    return hijo

def mutar(hijo,mutacion):
    if mutacion > random.random():
        alelo = random.randint(0,2)
        hijo[alelo]=hijo[alelo]+(random.randint(-9,9))
    return hijo

def nuevaGeneracion(cantidad,mutacion):
    poblacion = generarPoblacion(cantidad)
    continuar = True
    cont = 0
    while(continuar):
        cont += 1
        print("Generacion : "+str(cont))
        mejores = seleccionar(poblacion)
        print(mejores)
        for i in range(cantidad):            
            hijo = reproducir(mejores)
            poblacion.append(mutar(hijo,mutacion))
        print('s para salir, cualquier otra tecla para continuar')
        entrada = input()
        if entrada == 's':
            continuar = False


nuevaGeneracion(100,0.3)

