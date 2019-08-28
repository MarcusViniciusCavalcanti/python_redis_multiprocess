import random

def cria_matriz(linhas, colunas):
  A = []
  for i in range(linhas):
    linha = []
    for j in range(colunas):
      linha = linha + [random.randint(1, 10)]
    A = A + [linha]
  return A

def multiplica_linha_coluna(matrizA, matrizB):
  valor = 0

  print(matrizB)
  for k in range(len(matrizB)):
    b_ = matrizB[k]
    print(b_)
    valor = valor + matrizA[k] * b_
  return valor