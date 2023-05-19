# arquivo de classes para criar a treliça e poder resolve-la
# a primeira classe é para definir o nó, sempre em 2d
# a segunda classe para criar a viga, que é uma ligação entre dois nós
# por fim a classe treliça, que é uma lista de nós e uma lista de vigas

# a classe no recebera as cordenadas x,y, se o nó está treavado ou não em x,y
# e a carga aplicada em x,y

import numpy as np

class No:
    # x_lock é variavel booleana que diz se o nó está travado em x
    # y_lock é variavel booleana que diz se o nó está travado em y
    
    def __init__(self, x, y, x_lock, y_lock, x_carga, y_carga, x_numeracao_liberdade, y_numeracao_liberdade):
        self.x = x
        self.y = y
        self.x_lock = x_lock
        self.y_lock = y_lock
        self.x_carga = x_carga
        self.y_carga = y_carga
        self.x_numeracao_liberdade = x_numeracao_liberdade
        self.y_numeracao_liberdade = y_numeracao_liberdade
        
# a classe viga recebera os dois nós que ela liga, o modulo de elasticidade
# a dimensão aplicada na viga e a carga aplicada na viga (com a coordenada x,y)

class Barra:
    # x carga é a coordenada x onde a carga é aplicada
    # y carga é a coordenada y onde a carga é aplicada
    # x_size é a dimensão da viga em x
    # y size é a dimensão da viga em y
    
    def __init__(self, no1, no2, modulo_elasticidade, area_secao):
        self.no1 = no1
        self.no2 = no2
        self.modulo_elasticidade = modulo_elasticidade
        self.area_secao = area_secao
        self.size = np.sqrt((no1.x-no2.x)**2 + (no1.y-no2.y)**2)
        self.dof = np.array([no1.x_numeracao_liberdade, no1.y_numeracao_liberdade, no2.x_numeracao_liberdade,no2.y_numeracao_liberdade])
        self.cos = (no2.x-no1.x)/self.size
        self.sin = (no2.y-no1.y)/self.size
        self.k_local = ((modulo_elasticidade*area_secao)/self.size)*np.array([[self.cos**2,self.cos*self.sin,-self.cos**2,-self.cos*self.sin],
                                 [self.cos*self.sin,self.sin**2,-self.cos*self.sin, -self.sin**2],
                                 [-self.cos**2,-self.cos*self.sin,self.cos**2,self.cos*self.sin],
                                 [-self.cos*self.sin,-self.sin**2,self.cos*self.sin,self.sin**2]])
        
# class MatrixRigidez:
#     # a entrada é uma lista de barras e a saida é a matriz de rigidez associada
#     def __init__(self,lis_no,lis_barra):
#         self.lis_no = lis_no
#         self.lis_barra = lis_barra
        
#     def processa(self):
#         # o shape é 2x o grau de liberdade x o numero de nos
#         matrix_rigidez = np.zeros(shape=(self.lis_no[0].grau_liberdade*len(self.lis_no),self.lis_no[0].grau_liberdade*len(self.lis_no)))
#         for i in range(len(self.lis_barra)):
#             barra = self.lis_barra[i]
#             matriz_local = np.array([[1,-1],[-1,1]]) * barra.modulo_elasticidade * barra.area_secao / barra.size
#             matrix_rigidez[i:i+2,i:i+2] += matriz_local
#         return matrix_rigidez