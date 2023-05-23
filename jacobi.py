import numpy as np

pesos = [
    [3, -0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10],
]

deslocamentos = [0, 0, 0]
deslocamentoAux = [0, 0, 0]

erroX1 = 0
erroX2 = 0
erroX3 = 0

forcas = [7.85, -19.3, 71.4]

limite = 1e-8

def calculateError(xAtual, xAnterior):
    if xAtual > 0:
        return np.divide(np.abs(xAtual - xAnterior), xAtual)
    return 0


while(1):
    deslocamentoAux[0] = np.divide(forcas[0] - np.multiply(pesos[0][1], deslocamentos[1]) - np.multiply(pesos[0][2], deslocamentos[2]), pesos[0][0])
    deslocamentoAux[1] = np.divide(forcas[1] - np.multiply(pesos[1][0], deslocamentos[0]) - np.multiply(pesos[1][2], deslocamentos[2]), pesos[1][1])
    deslocamentoAux[2] = np.divide(forcas[2] - np.multiply(pesos[2][0], deslocamentos[0]) - np.multiply(pesos[2][1], deslocamentos[1]), pesos[2][2])
    
    erroX1 = calculateError(deslocamentoAux[0], deslocamentos[0])
    erroX2 = calculateError(deslocamentoAux[1], deslocamentos[1])
    erroX3 = calculateError(deslocamentoAux[2], deslocamentos[2])
    deslocamentos = np.copy(deslocamentoAux)


    print(erroX1, erroX2, erroX3)
    if (max(erroX1, erroX2, erroX3) < limite):
        print(deslocamentos)
        print(f"{erroX1:.6f}")
        break