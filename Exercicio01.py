from numba import jit
import time
import numpy as np

# Letra A
@jit(nopython=True,parallel=True)
def soma_quadrados_otimizada(lista):
    soma = 0
    for num in lista:
        soma += num ** 2
    return soma


def soma_quadrados(lista):
    soma = 0
    for num in lista:
        soma += num ** 2
    return soma

# Letra C e D
dados_teste = np.random.rand(10000000)

inicio = time.time()
resultado_original = soma_quadrados(dados_teste)
tempo_original = time.time() - inicio

inicio = time.time()
resultado_otimizada = soma_quadrados_otimizada(dados_teste)
tempo_otimizada_primeira = time.time() - inicio

inicio = time.time()
resultado_otimizada = soma_quadrados_otimizada(dados_teste)
tempo_otimizada_segunda = time.time() - inicio

print(f"Tempo função original: {tempo_original:.4f}s")
print(f"Tempo função otimizada (1ª exec): {tempo_otimizada_primeira:.4f}s")
print(f"Tempo função otimizada (2ª exec): {tempo_otimizada_segunda:.4f}s")
print(f"Resultados iguais: {resultado_original == resultado_otimizada}")