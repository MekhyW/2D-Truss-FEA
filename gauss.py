import numpy as np

def calculateError(xAtual, xAnterior):
    if xAtual > 0:
        return np.divide(np.abs(xAtual - xAnterior), xAtual)
    return 0

def gaussSeidel(iteracoes, tolerancia, K, F):
    n = len(F)  # Number of unknowns
    
    deslocamentos = np.zeros(n)
    erro = np.zeros(n)
    erroAnterior = np.zeros(n)
    
    for _ in range(iteracoes):
        for i in range(n):
            soma1 = np.dot(K[i, :i], deslocamentos[:i])
            soma2 = np.dot(K[i, i + 1:], deslocamentos[i + 1:])
            deslocamentos[i] = np.divide(F[i] - soma1 - soma2, K[i, i])
        
        erro = np.array([calculateError(deslocamentos[i], erroAnterior[i]) for i in range(n)])
        erroAnterior = np.copy(deslocamentos)
        
        print(erro)
        
        if np.max(erro) < tolerancia:
            return deslocamentos, np.max(erro)
    
    return deslocamentos, np.max(erro)


if __name__ == "__main__":
    deslocamentos = [0, 0, 0]

    erroX1 = 0
    erroX2 = 0
    erroX3 = 0



    forcas = [0, 150, -100]

    limite = 1e-20
    pesos = [
    [1.59e8, -0.4e8, -0.54e8],
    [-0.4e8, 1.7e8, 0.4e8],
    [-0.54e8, 0.4e8, 0.54e8],
    ]
    print(gaussSeidel(100, 1e-8, pesos, forcas))