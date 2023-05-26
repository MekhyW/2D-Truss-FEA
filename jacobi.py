import numpy as np

def calculateError(xAtual, xAnterior):
    if xAtual > 0:
        return np.divide(np.abs(xAtual - xAnterior), xAtual)
    return 0

def jacobi(iteracoes, tolerancia, pesos, forcas):
    n = len(forcas)
    
    deslocamentos = np.zeros(n)
    deslocamentoAux = np.zeros(n)
    erro = np.zeros(n)
    
    limite = tolerancia
    
    for _ in range(iteracoes):
        for i in range(n):
            soma = np.dot(pesos[i, :], deslocamentos)
            soma -= pesos[i, i] * deslocamentos[i]
            deslocamentoAux[i] = np.divide(forcas[i] - soma, pesos[i, i])
        
        erro = np.array([calculateError(deslocamentoAux[i], deslocamentos[i]) for i in range(n)])
        deslocamentos = np.copy(deslocamentoAux)
        
        if np.max(erro) < limite:
            return deslocamentos, np.max(erro)
    
    return deslocamentos, np.max(erro)
