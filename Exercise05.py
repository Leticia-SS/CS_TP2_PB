# Letra A
class TreeNode:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def inserir(self, valor):
        if valor < self.valor:
            if self.esquerda is None:
                self.esquerda = TreeNode(valor)
            else:
                self.esquerda.inserir(valor)
        else:
            if self.direita is None:
                self.direita = TreeNode(valor)
            else:
                self.direita.inserir(valor)

    def buscar(self, valor):
        if valor == self.valor:
            return True
        elif valor < self.valor and self.esquerda:
            return self.esquerda.buscar(valor)
        elif valor > self.valor and self.direita:
            return self.direita.buscar(valor)
        return False

    def em_ordem(self):
        resultado = []
        if self.esquerda:
            resultado.extend(self.esquerda.em_ordem())
        resultado.append(self.valor)
        if self.direita:
            resultado.extend(self.direita.em_ordem())
        return resultado


# Letra C
class ListNode:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class LinkedList:
    def __init__(self):
        self.cabeca = None

    def inserir_final(self, valor):
        novo_no = ListNode(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def imprimir(self):
        valores = []
        atual = self.cabeca
        while atual:
            valores.append(str(atual.valor))
            atual = atual.proximo
        return " -> ".join(valores) + " -> None"


# Letra B
def testar_arvore():
    print("=== ÁRVORE BINÁRIA ===")
    arvore = TreeNode(50)
    valores = [30, 70, 20, 40, 60, 80, 10, 25, 35, 45]

    for valor in valores:
        arvore.inserir(valor)

    print("Valores em ordem:", arvore.em_ordem())

    testes_busca = [25, 70, 100, 35]
    for valor in testes_busca:
        encontrado = arvore.buscar(valor)
        print(f"Buscar {valor}: {'Encontrado' if encontrado else 'Não encontrado'}")


def testar_lista():
    print("\n=== LISTA ENCADEADA ===")
    lista = LinkedList()
    valores = [50, 30, 70, 20, 40, 60, 80]

    for valor in valores:
        lista.inserir_final(valor)

    print("Valores na lista:", lista.imprimir())

    testes_busca = [40, 90, 20, 100]
    for valor in testes_busca:
        encontrado = lista.buscar(valor)
        print(f"Buscar {valor}: {'Encontrado' if encontrado else 'Não encontrado'}")


if __name__ == "__main__":
    testar_arvore()
    testar_lista()