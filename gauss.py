import numpy as np

pesos = [
    [1.59e8, -0.4e8, -0.54e8],
    [-0.4e8, 1.7e8, 0.4e8],
    [-0.54e8, 0.4e8, 0.54e8],
]

deslocamentos = [0, 0, 0]

erroX1 = 0
erroX2 = 0
erroX3 = 0



forcas = [0, 150, -100]

limite = 1e-20

def calculateError(xAtual, xAnterior):
    if xAtual > 0:
        return np.divide(np.abs(xAtual - xAnterior), xAtual)
    return 0

def gaussSeidel(iteracoes, tolerancia, K, F):
    deslocamentos = np.zeros(len(F))
    deslAnteriorx1 = 0
    deslAnteriorx2 = 0
    deslAnteriorx3 = 0
    for i in range(iteracoes):
        deslAnteriorx1 = deslocamentos[0]
        deslocamentos[0] = np.divide(forcas[0] - np.multiply(pesos[0][1], deslocamentos[1]) - np.multiply(pesos[0][2], deslocamentos[2]), pesos[0][0])
        deslAnteriorx2 = deslocamentos[1]
        deslocamentos[1] = np.divide(forcas[1] - np.multiply(pesos[1][0], deslocamentos[0]) - np.multiply(pesos[1][2], deslocamentos[2]), pesos[1][1])
        deslAnteriorx3 = deslocamentos[2]
        deslocamentos[2] = np.divide(forcas[2] - np.multiply(pesos[2][0], deslocamentos[0]) - np.multiply(pesos[2][1], deslocamentos[1]), pesos[2][2])
        erroX1 = calculateError(deslocamentos[0], deslAnteriorx1)
        erroX2 = calculateError(deslocamentos[1], deslAnteriorx2)
        erroX3 = calculateError(deslocamentos[2], deslAnteriorx3)
        print(erroX1, erroX2, erroX3)
        if (max(erroX1, erroX2, erroX3) < tolerancia):
            return deslocamentos, max(erroX1, erroX2, erroX3)
    return deslocamentos, max(erroX1, erroX2, erroX3)

print(gaussSeidel(100, 1e-8, pesos, forcas))