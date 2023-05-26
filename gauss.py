import numpy as np

def calculateError(xAtual, xAnterior, toleranca):
    if xAtual > 0:
        return np.divide(np.abs(xAtual - xAnterior), xAtual)
    return toleranca * 2

def gaussSeidel(iteracoes, tolerancia, K, F):
    n = len(F) 
    deslocamentos = np.zeros(n)
    erro = np.zeros(n)
    it = 0
    erroAnterior = np.zeros(n)
    
    for _ in range(iteracoes):
        for i in range(n):
            soma1 = np.dot(K[i, :i], deslocamentos[:i])
            soma2 = np.dot(K[i, i + 1:], deslocamentos[i + 1:])
            deslocamentos[i] = np.divide(F[i] - soma1 - soma2, K[i, i])
        it += 1
        
        erro = np.array([calculateError(deslocamentos[i], erroAnterior[i], tolerancia) for i in range(n)])
        erroAnterior = np.copy(deslocamentos)
        #print(np.max(erro)) 
        if (np.max(erro) < tolerancia) or (np.max(erro) ==  tolerancia * 2):
            #print(it)
            return deslocamentos, np.max(erro)
    #print(it)
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