import time

# Letra A
def fibonacci_recursivo(n):
    if n < 0:
        raise ValueError("n deve ser não negativo")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def demonstrar_fibonacci(n):
    print(f"=== CALCULANDO Fibonacci({n}) RECURSIVAMENTE ===")
    resultado = fibonacci_recursivo(n)
    print(f"Fibonacci({n}) = {resultado}")

    print(f"\nPara calcular Fibonacci({n}), a função fez:")
    if n <= 1:
        print(f"= 1 chamada direta")
    else:
        print(f"= Chamou Fibonacci({n - 1}) e Fibonacci({n - 2})")
        print(f"= Que por sua vez chamaram outros valores recursivamente")
        print(f"= Total de chamadas: aproximadamente {2 ** n} operações\n\n")


# Letra C
def fibonacci_dp(n):
    if n < 0:
        raise ValueError("n deve ser não negativo")

    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


def fibonacci_dp_otimizado(n):
    if n <= 1:
        return n

    anterior2 = 0  # fib(n-2)
    anterior1 = 1  # fib(n-1)

    for i in range(2, n + 1):
        atual = anterior1 + anterior2
        anterior2 = anterior1
        anterior1 = atual

    return anterior1

# Letra D
def comparar_desempenho():
    valores_teste = [5, 10, 15, 20, 25, 30, 35]

    print("n\tRecursivo\tDP\t\tDP Otimizado")
    print("-" * 50)

    for n in valores_teste:
        if n <= 35:
            inicio = time.time()
            resultado_rec = fibonacci_recursivo(n)
            tempo_rec = time.time() - inicio
        else:
            tempo_rec = "N/A"
            resultado_rec = "N/A"

        inicio = time.time()
        resultado_dp = fibonacci_dp(n)
        tempo_dp = time.time() - inicio

        inicio = time.time()
        resultado_dp_opt = fibonacci_dp_otimizado(n)
        tempo_dp_opt = time.time() - inicio

        print(f"{n}\t{tempo_rec:.6f}s\t\t{tempo_dp:.6f}s\t{tempo_dp_opt:.6f}s")

        if n <= 35:
            assert resultado_rec == resultado_dp == resultado_dp_opt


if __name__ == "__main__":
    demonstrar_fibonacci(5)

    print("=== TESTES BÁSICOS ===")
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci_dp(i)}")

    print("\n=== COMPARAÇÃO DE DESEMPENHO ===")
    comparar_desempenho()

    print("\n=== VALORES MAIORES (APENAS DP) ===")
    for n in [40, 50, 100]:
        inicio = time.time()
        resultado = fibonacci_dp_otimizado(n)
        tempo = time.time() - inicio
        print(f"Fibonacci({n}) = {resultado} | Tempo: {tempo:.6f}s")