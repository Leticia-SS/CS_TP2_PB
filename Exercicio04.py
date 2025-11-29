# Letra A
def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não está definido para números negativos")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


# b) Letra B
def testar_fatorial():
    print("=== TESTE DA FUNÇÃO FATORIAL ===")

    testes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]

    for n in testes:
        resultado = fatorial(n)
        print(f"{n}! = {resultado}")


def fatorial_iterativo(n):
    if n < 0:
        raise ValueError("Fatorial não está definido para números negativos")

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# Letra D
def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci não está definido para números negativos")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    testar_fatorial()

    print("\n========= COMPARAÇÃO RECURSIVO vs ITERATIVO =========")
    n = 10
    print(f"Fatorial recursivo de {n}: {fatorial(n)}")
    print(f"Fatorial iterativo de {n}: {fatorial_iterativo(n)}")

    print("\n========= SEQUÊNCIA DE FIBONACCI =========")
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci(i)}")