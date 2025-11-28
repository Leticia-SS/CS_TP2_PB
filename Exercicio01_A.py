from numba import jit

@jit(nopython=True, parallel=True)
def soma_quadrados_otimizada(lista):
    soma = 0
    for num in lista:
        soma += num ** 2
    return soma
