# https://www.superprof.es/diccionario/matematicas/estadistica/sumatoria.html#:~:text=La%20sumatoria%20o%20sumatorio%20se,letra%20griegra%20sigma%20may%C3%BAscula%20%CE%A3.
# https://www.geeksforgeeks.org/python-central-limit-theorem/
# A FIRST COURSE IN PROBABILITY -> Page 391
# Central Limit Theorem

import numpy
import matplotlib.pyplot as plt
from scipy.stats import norm 

# 1) Genere n valores independientes al azar y calcule la media aritmética
def aritmethic_media(n: int) -> float:
    r = 0
    for i in range(1, n + 1):
        x = numpy.mean(numpy.random.randint(-40, 40, i))
        r += x
    return (1 / n) * r

def central_means(n: int, s_n: int, mean = 0, variance = 1) -> float:    
    return (s_n - mean) / (variance / numpy.sqrt(n))

def plotting_all_means(means : list, N : list):
    k = 0
    # graficar todos los promedio en una sola figura
    fig, ax = plt.subplots(2, 2, figsize =(8, 8))
    for i in range(0, 2):
        for j in range(0, 2):
            # Histograma por cada x alamenado en los promedios
            ax[i, j].hist(means[k], 10, density = True)
            ax[i, j].set_title(label = N[k])
            k = k + 1
    plt.savefig("lab2b.png") # Guarda la figura en png, por si plt.show rippea
    plt.show()

def plot_cdfs (means: list, N: list):
    k = 0
    fig, ax = plt.subplots(2, 2, figsize =(8, 8))
    for i in range(0, 2):
        for j in range(0, 2):
            # Funcion de distribucion empirica
            # ax[i, j].ecdf(means[k]) # Posible en matplotlib 3.8
            x = numpy.sort(means[k])
            y = numpy.linspace(0, 1, len(means[k]), endpoint=False)
            ax[i, j].plot(x, y)
            ax[i, j].hist(x, density=True, cumulative=True, histtype='step', alpha=0.8)
            ax[i, j].set_title(label = N[k])
            k = k + 1
    plt.savefig("lab2b_2.png") # Guarda la figura en png, por si plt.show rippea
    plt.show()
 

# Función para plotear histograma y función de densidad normal
def plot_histogram_with_normal(means: list, N: list):
    k = 0
    fig, ax = plt.subplots(2, 2, figsize=(8, 8))
    for i in range(0, 2):
        for j in range(0, 2):
            # Histograma por cada x almacenado en los promedios
            ax[i, j].hist(means[k], bins=20, density=True, alpha=0.6)
            ax[i, j].set_title(label=N[k])

            # Agregamos la función de densidad normal estándar en la misma gráfica
            x_vals = numpy.linspace(min(means[k]), max(means[k]), 100)
            y_vals = norm.pdf(x_vals, loc=0, scale=1)
            ax[i, j].plot(x_vals, y_vals, color='red', linewidth=2)

            k = k + 1
    plt.savefig("histogram_with_normal.png")
    plt.show()  # Ahora debería mostrar la figura correctamente

if __name__ == "__main__":
    print("Lab 2.b")

    n = [20, 40, 60, 100]
    N = [50, 100, 1000, 10000]
    # N = [50, 100, 1000, 1500] # Por si quieren ver resultados más rápido
    N_means = []

    # 2) Repita N veces el inciso anterior calculando los promedios centrados
    for N_element in N:
        means = []        
        for e in range(0, N_element):
            for i in n:
                s_n = aritmethic_media(i)
                c_m = central_means(i, s_n)
                means.append(c_m)
        print(f"Se guardo un elemento desde {N_element} para means")
        N_means.append(means)
        
    # 3) Elabore un histograma de estos N valores
    plotting_all_means(N_means, N)

    plot_histogram_with_normal(N_means, N)

    # 4) Elabore una grafica de frecuencia relativa acumulada
    plot_cdfs(N_means, N)

    print("END")