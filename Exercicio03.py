import random
import time


# a) Letra A
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]
    arr = arr.copy()

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Letra B
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return quickselect(right, k - len(left) - len(middle))


def carregar_dados(arquivo="outputTP1.txt"):
    with open(arquivo, 'r', encoding='utf-8') as file:
        return [linha.strip() for linha in file.readlines() if linha.strip()]



def main():
    dados = carregar_dados()
    print(f"Carregados {len(dados)} nomes de arquivos")

    k = 500

    inicio = time.time()
    k_esimo_select = quickselect(dados.copy(), k)
    tempo_select = time.time() - inicio
    print(f"QuickSelect == {k}º menor elemento: '{k_esimo_select}'")
    print(f"Tempo: {tempo_select:.4f}s")

    inicio = time.time()
    dados_ordenados = quicksort(dados.copy())
    k_esimo_sort = dados_ordenados[k]
    tempo_sort = time.time() - inicio
    print(f"QuickSort == {k}º menor elemento: '{k_esimo_sort}'")
    print(f"Tempo: {tempo_sort:.4f}s")

    print(f"Resultados iguais: {k_esimo_select == k_esimo_sort}")
    print(f"QuickSelect foi {tempo_sort / tempo_select:.2f}x mais rápido")


# Letra C
print("COMPLEXIDADES:")
print("QuickSort: O(n log n) tempo médio, O(n²) pior caso, O(log n) espaço")
print("QuickSelect: O(n) tempo médio, O(n²) pior caso, O(log n) espaço")
print("QuickSelect é mais eficiente para encontrar um único elemento")
print("QuickSort é necessário quando a lista ordenada completa é necessária")

if __name__ == "__main__":
    main()