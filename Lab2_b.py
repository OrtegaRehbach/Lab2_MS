# https://www.superprof.es/diccionario/matematicas/estadistica/sumatoria.html#:~:text=La%20sumatoria%20o%20sumatorio%20se,letra%20griegra%20sigma%20may%C3%BAscula%20%CE%A3.
# https://www.geeksforgeeks.org/python-central-limit-theorem/
# A FIRST COURSE IN PROBABILITY -> Page 391
# Central Limit Theorem

import numpy
import matplotlib.pyplot as plt

# 1) Genere n valores independientes al azar y calcule la media aritmética
def aritmethic_media(n: int) -> float:
    r = 0
    for i in range(1, n + 1):\
        # representar distribucion uniforme en el intervalo de (0, 1)
        x = numpy.mean(numpy.random.randint(0, 2, i))
        r += x
    return (1 / n) * r

def central_means(n: int, s_n: int, mean = 0, variance = 1) -> float:    
    return (s_n - mean) / (variance / numpy.sqrt(n))

def plotting_all_means(means : list, N : list):
    k = 0

    # plotting all the means in one figure
    fig, ax = plt.subplots(2, 2, figsize =(8, 8))
    for i in range(0, 2):
        for j in range(0, 2):
            # Histogram for each x stored in means
            ax[i, j].hist(means[k], 10, density = True)
            ax[i, j].set_title(label = N[k])
            k = k + 1
    plt.show()

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
                # print(f'==> {i}')
                s_n = aritmethic_media(i)
                # print(f'Media aritmetica: {s_n}')
                c_m = central_means(i, s_n)
                # print(f'Central means: {c_m}\n')
                means.append(c_m)
        print(f"Se guardo un elemente desde {N_element} para means")
        N_means.append(means)
        
    # 3) Elabore un histograma de estos N valores
    plotting_all_means(N_means, N)

    print("END")