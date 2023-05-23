import numpy as np
import pandas as pd
from funcoesTermosol import *
from trelica import *
from gauss import *

n_nos,matriz_nos,n_membros,matriz_incidencia,n_cargas,vetor_carregamento,n_restricoes,vetor_restricoes = importa('entrada-teste.xls')
print('número de nós = ',n_nos)
print('número de membros = ',n_membros)
print('número de cargas = ',n_cargas)
print('número de restrições = ',n_restricoes)

lock_flattened = [int(i) for i in vetor_restricoes.flatten()]
carregamento_flatenned = vetor_carregamento.flatten()
lis_no = []
for index_no in range(n_nos):
    x = matriz_nos[0,index_no]
    y = matriz_nos[1,index_no]
    x_numeracao_liberdade = 2*index_no
    y_numeracao_liberdade = 2*index_no+1
    x_lock = x_numeracao_liberdade in lock_flattened
    y_lock = y_numeracao_liberdade in lock_flattened
    x_carga = carregamento_flatenned[x_numeracao_liberdade]
    y_carga = carregamento_flatenned[y_numeracao_liberdade]
    no = No(matriz_nos[0,index_no],matriz_nos[1,index_no],x_lock,y_lock,x_carga,y_carga,x_numeracao_liberdade,y_numeracao_liberdade)
    lis_no.append(no)

lis_barra = []
for barra in matriz_incidencia:
    no1 = lis_no[int(barra[0])-1]
    no2 = lis_no[int(barra[1])-1]
    modulo_elasticidade = barra[2]
    area_secao = barra[3]
    lis_barra.append(Barra(no1,no2,modulo_elasticidade,area_secao))

matrix_rigidez = np.zeros(shape=(2*len(lis_no),2*len(lis_no)))
for i in range(len(lis_barra)):
    barra = lis_barra[i]
    matrix_rigidez[np.ix_(barra.dof,barra.dof)] += barra.k_local

vector_carga = np.zeros(shape=(2*len(lis_no),1))
for no in lis_no:
    vector_carga[no.x_numeracao_liberdade] = no.x_carga
    vector_carga[no.y_numeracao_liberdade] = no.y_carga

for no in lis_no:
    if no.x_lock:
        idx = no.x_numeracao_liberdade
        matrix_rigidez[idx,:] = 0
        matrix_rigidez[:,idx] = 0
        matrix_rigidez[idx,idx] = 1
        vector_carga[idx] = 0
    if no.y_lock:
        idx = no.y_numeracao_liberdade
        matrix_rigidez[idx,:] = 0
        matrix_rigidez[:,idx] = 0
        matrix_rigidez[idx,idx] = 1
        vector_carga[idx] = 0

det = np.linalg.det(matrix_rigidez)
u = np.linalg.solve(matrix_rigidez,vector_carga)
print(f"GAUSS: {gaussSeidel(100, 1e-8, matrix_rigidez, vector_carga)[0]}")

#print('matriz de rigidez = \n',matrix_rigidez)
#print('vetor de carga = \n',vector_carga)
print('deslocamentos = \n',u)