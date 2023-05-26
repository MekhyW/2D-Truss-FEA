import numpy as np

def calculateError(xAtual, xAnterior, toleranca):
    if xAtual > 0:
        return np.divide(np.abs(xAtual - xAnterior), xAtual)
    return toleranca * 2

def jacobi(iteracoes, tolerancia, K, F):
    n = len(F)  # Number of unknowns
    
    deslocamentos = np.zeros(n)
    deslocamentoAux = np.zeros(n)
    erro = np.zeros(n)
    
    for _ in range(iteracoes):
        for i in range(n):
            soma = np.dot(K[i, :], deslocamentos)
            soma -= K[i, i] * deslocamentos[i]
            deslocamentoAux[i] = np.divide(F[i] - soma, K[i, i])
        
        erro = np.array([calculateError(deslocamentoAux[i], deslocamentos[i], tolerancia) for i in range(n)])
        deslocamentos = np.copy(deslocamentoAux)
        
        if np.max(erro) < tolerancia:
            return deslocamentos, np.max(erro)
    
    return deslocamentos, np.max(erro)
