import math
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

Y =[]
X =[]

def decision(x,w,peso):
    resultado = 0

    for i in range(len(x)):
        resultado = resultado + x[i]*w[i]

    resultado = resultado + peso
    funcion = 1/(1+math.exp(-resultado))

    return funcion
    
def main():
    #AND
    #print("AND")
    x = [1,1]
    w = [1,1]
    b = -2
    #print(decision(x,w,b))
    
    #OR
    #print("OR")
    x = [1,1]
    w = [1,1]
    b = -1
    #print(decision(x,w,b))
    
    #XOR
    #print("XOR")
    x = [1,1]
    w = [1,1]
    b = -1
    primerNodo = decision(x,w,b)
    #print("Primer nodo " + str(primerNodo))
    
    w = [2,2]
    b = -4
    segundoNodo = decision(x,w,b)
    #print("Segundo nodo " + str(segundoNodo))
    
    x = [primerNodo,segundoNodo]
    w = [1,-1]
    b = -0.3
    resultado = decision(x,w,b)
    #print("Tercer nodo " + str(resultado))

    prueba()

    entrenando()

    
    
def forward(a,b,c,d):

    x = [a,b,c,d]
    #Primer nodo
    w = [-2,-2,-2,-2]
    b = 1
    primerNodo = decision(x,w,b)

    #Segundo nodo
    w = [-2,-6,2,-6]
    b = 3
    segundoNodo = decision(x,w,b)

    # Tercer nodo
    w = [-4, -1, -4, 3]
    b = -1
    tercerNodo = decision(x, w, b)

    # Cuarto nodo
    w = [-6, -1, 5, 5]
    b = -6
    cuartoNodo = decision(x, w, b)

    # Quinto nodo
    w = [-6, 3, -6, 3]
    b = -4
    quintoNodo = decision(x, w, b)

    #Or
    x=[primerNodo,segundoNodo,tercerNodo,cuartoNodo,quintoNodo]
    w = [2, 2, 2, 2, 2]
    b = -2
    return decision(x, w, b)

def prueba():
    global Y
    global X
    Y.append(forward(0, 0, 0, 0) > 0.5)
    X.append((0, 0, 0, 0))
    Y.append(forward(0, 0, 0, 1) > 0.5)
    X.append((0, 0, 0, 1))
    Y.append(forward(0, 0, 1, 0) > 0.5)
    X.append((0, 0, 1, 0))
    Y.append(forward(0, 0, 1, 1) > 0.5)
    X.append((0, 0, 1, 1))
    Y.append(forward(0, 1, 0, 0) > 0.5)
    X.append((0, 1, 0, 0))

    Y.append(forward(0, 1, 0, 1) > 0.5)
    X.append((0, 1, 0, 1))
    Y.append(forward(0, 1, 1, 0) > 0.5)
    X.append((0, 1, 1, 0))
    Y.append(forward(0, 1, 1, 1) > 0.5)
    X.append((0, 1, 1, 1))
    Y.append(forward(1, 0, 0, 0) > 0.5)
    X.append((1, 0, 0, 0))
    Y.append(forward(1, 0, 0, 1) > 0.5)
    X.append((1, 0, 0, 1))

    Y.append(forward(1, 0, 1, 0) > 0.5)
    X.append((1, 0, 1, 0))
    Y.append(forward(1, 0, 1, 1) > 0.5)
    X.append((1, 0, 1, 1))
    Y.append(forward(1, 1, 0, 0) > 0.5)
    X.append((1, 1, 0, 0))
    Y.append(forward(1, 1, 0, 1) > 0.5)
    X.append((1, 1, 0, 1))
    Y.append(forward(1, 1, 1, 0) > 0.5)
    X.append((1, 1, 1, 0))

    Y.append(forward(1, 1, 1, 1) > 0.5)
    X.append((1, 1, 1, 1))

    print(Y)
    print(X)

def entrenando():
    model = keras.Sequential(
        [
            #antes solo con 5 y 1, ahora con 5 5 3 1
            layers.Dense(units=5,input_shape=[4], activation="sigmoid"),
            layers.Dense(units=5, activation="sigmoid"),
            layers.Dense(units=3, activation="sigmoid"),
            layers.Dense(units=1, activation="sigmoid"),
        ]
    )

    model.compile(loss="mean_squared_error", optimizer="adam")

    historial = model.fit(X, Y, epochs=2000, batch_size=16, verbose=False)

    #model.predict([Y[0]])
    for tubla in X:
        print(f"{tubla} {model.predict([tubla]) >0.5}")

    plt.xlabel("Epocas")
    plt.ylabel("Error")
    plt.plot(historial.history["loss"])
    plt.show()

if __name__=="__main__":
    main()



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    