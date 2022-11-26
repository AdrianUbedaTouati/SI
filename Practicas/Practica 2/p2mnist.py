import matplotlib.pyplot as plt
import numpy
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import random

def mnist():
    (x_train,y_train), (x_test,y_test) = keras.datasets.mnist.load_data()

    print("Haciendo listas")

    x_train = x_train.reshape((x_train.shape[0],28*28))
    x_train = x_train.astype('float32') / 255.0

    y_train = salida(y_train)
    y_train = numpy.array(y_train,dtype=numpy.int32)

    x_test = x_test.reshape((x_test.shape[0], 28 * 28))
    x_test = x_test.astype('float32') / 255.0

    y_test = salida(y_test)
    y_test = numpy.array(y_test, dtype=numpy.int32)

    print("Terminando listas")

    model = keras.Sequential(
        [
            layers.Dense(units=128, input_shape=[784], activation="relu"),
            layers.Dense(units=128, activation="relu"),
            layers.Dense(units=10, activation="softmax"),
        ]
    )

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    historial = model.fit(x_train, y_train, epochs=15, batch_size=128, validation_split=0.1)

    plt.xlabel("Epocas")
    plt.ylabel("Error")
    plt.plot(historial.history["loss"])
    plt.show()

    print(model.evaluate(x_test,y_test))

    auxX = []
    auxY = []
    for i in range(1000):
        num = random.randint(1, 10000)

        auxX.append(x_train[num])
        auxY.append(y_train[num])


    auxX = tf.stack(auxX)
    auxY = tf.stack(auxY)

    print(f"1000 aleatorios de entrenamiento {model.evaluate(auxX, auxY)}")

    auxX = []
    auxY = []
    for i in range(1000):
        num = random.randint(1, 10000)

        auxX.append(x_test[num])
        auxY.append(y_test[num])


    auxX = tf.stack(auxX)
    auxY = tf.stack(auxY)

    print(f"1000 aleatorios de test {model.evaluate(auxX, auxY)}")



def salida(y_train):
    i = 0
    salida = []

    for elemento in y_train:
        if elemento == 0:
            salida.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif elemento == 1:
            salida.append([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        elif elemento == 2:
            salida.append([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
        elif elemento == 3:
            salida.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
        elif elemento == 4:
            salida.append([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
        elif elemento == 5:
            salida.append([0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
        elif elemento == 6:
            salida.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
        elif elemento == 7:
            salida.append([0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
        elif elemento == 8:
            salida.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
        elif elemento == 9:
            salida.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        i += 1

    return salida

def main():
    mnist()

if __name__=="__main__":
    main()