"""
Trabalho de Programação Orientada a Objetos: Hierarquia de Classes de Estruturas de Dados Lineares.

Parte 3 e 4: Classe ListaSimplesmenteEncadeada e Classe Pilha

Este arquivo contém:
- As classes base (EstruturaLinear, Node).
- A implementação da Classe ListaSimplesmenteEncadeada.
- A implementação da Classe Pilha, que utiliza a Lista Simples por composição.
"""

from abc import ABC, abstractmethod

# =============================================================================
# CLASSE BASE ABSTRATA (Das partes anteriores)
# =============================================================================

class EstruturaLinear(ABC):
    """
    Classe abstrata que define a interface comum para todas as estruturas
    de dados lineares na hierarquia.
    """
    @abstractmethod
    def __len__(self):
        """Retorna o número de itens na estrutura."""
        pass

    def is_empty(self):
        """Verifica se a estrutura está vazia."""
        return len(self) == 0

    def is_full(self):
        """Verifica se a estrutura está cheia."""
        return False

    @abstractmethod
    def insert(self, item, **kwargs):
        """Método genérico para inserção."""
        pass

    @abstractmethod
    def remove(self, **kwargs):
        """Método genérico para remoção."""
        pass

    @abstractmethod
    def find(self, key, **kwargs):
        """Método genérico para busca."""
        pass

# =============================================================================
# NÓS PARA LISTAS ENCADEADAS (Das partes anteriores)
# =============================================================================

class Node:
    """Nó para a Lista Simplesmente Encadeada."""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node(data={self.data})"

class DoubleNode(Node):
    """Nó para a Lista Duplamente Encadeada."""
    def __init__(self, data):
        super().__init__(data)
        self.prev = None

    def __repr__(self):
        return f"DoubleNode(data={self.data})"

# =============================================================================
# CLASSE LISTA SIMPLESMENTE ENCADEADA (NOVA - Parte 3)
# =============================================================================

class ListaSimplesmenteEncadeada(EstruturaLinear):
    """
    Implementação de uma Lista Simplesmente Encadeada.
    Herda de EstruturaLinear.
    """
    def __init__(self, iterable=None):
        """
        Construtor da Lista.
        Pode ser inicializada a partir de um objeto iterável (como uma lista Python).
        """
        self._head = None
        self._size = 0
        if iterable:
            # Inserimos na ordem inversa para que a lista final mantenha a ordem do iterável
            for item in reversed(iterable):
                self.push(item)

    def __len__(self):
        """Retorna o número de nós na lista."""
        return self._size

    def push(self, item):
        """Insere um item no início da lista (operação O(1))."""
        new_node = Node(item)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def pop(self):
        """
        Remove e retorna o item do início da lista (operação O(1)).
        Lança um IndexError se a lista estiver vazia.
        """
        if self.is_empty():
            raise IndexError("Remoção de uma lista vazia (underflow).")
        item_removido = self._head.data
        self._head = self._head.next
        self._size -= 1
        return item_removido

    def find_at(self, index):
        """
        Consulta (sem remover) o item na i-ésima posição.
        Lança um IndexError se o índice for inválido.
        """
        if not 0 <= index < self._size:
            raise IndexError("Índice fora dos limites.")

        current = self._head
        for _ in range(index):
            current = current.next
        return current.data

    # --- Implementação dos métodos abstratos ---
    def insert(self, item, **kwargs):
        """Implementação genérica de inserção. Por padrão, insere no início."""
        self.push(item)

    def remove(self, **kwargs):
        """Implementação genérica de remoção. Por padrão, remove do início."""
        return self.pop()

    def find(self, key, **kwargs):
        """Encontra e retorna o primeiro item com a chave especificada."""
        current = self._head
        while current:
            if current.data == key:
                return current.data
            current = current.next
        raise ValueError(f"Chave '{key}' não encontrada.")

    def __str__(self):
        """Representação em string da Lista."""
        items = []
        current = self._head
        while current:
            items.append(str(current.data))
            current = current.next
        return f"ListaSimples: [{' -> '.join(items)}]"

# =============================================================================
# CLASSE PILHA (STACK) - (NOVA - Parte 4)
# =============================================================================

class Pilha(EstruturaLinear):
    """
    Implementação de uma Pilha (Stack) usando composição com
    ListaSimplesmenteEncadeada. A lógica é LIFO (Last-In, First-Out).
    """
    def __init__(self):
        """Construtor da Pilha. Cria uma lista interna para armazenar os dados."""
        self._lista = ListaSimplesmenteEncadeada()

    def __len__(self):
        """Retorna o número de itens na pilha."""
        return len(self._lista)

    def push(self, item):
        """Adiciona um item ao topo da pilha."""
        self._lista.push(item)

    def pop(self):
        """
        Remove e retorna o item do topo da pilha.
        Lança um IndexError se a pilha estiver vazia (Stack Underflow).
        """
        if self.is_empty():
            raise IndexError("Pilha vazia (Stack underflow).")
        return self._lista.pop()

    def peek(self):
        """
        Retorna o item do topo da pilha sem removê-lo.
        Lança um IndexError se a pilha estiver vazia.
        """
        if self.is_empty():
            raise IndexError("Pilha vazia.")
        return self._lista.find_at(0)

    # --- Implementação dos métodos abstratos ---
    def insert(self, item, **kwargs):
        """Implementação genérica de inserção para a Pilha."""
        self.push(item)

    def remove(self, **kwargs):
        """Implementação genérica de remoção para a Pilha."""
        return self.pop()

    def find(self, **kwargs):
        """Na Pilha, 'find' é interpretado como 'peek' (olhar o topo)."""
        return self.peek()

    def __str__(self):
        """Representação em string da Pilha."""
        # A representação da lista subjacente já serve bem para a pilha
        return f"Pilha(topo={self._lista})"

# =============================================================================
# BLOCO DE TESTE
# =============================================================================

if __name__ == "__main__":

    # --- Teste da Classe Lista Simplesmente Encadeada ---
    print("--- Teste: Lista Simplesmente Encadeada ---")
    lista_s = ListaSimplesmenteEncadeada([10, 20, 30])
    print(f"Lista inicial a partir de iterável: {lista_s}")
    lista_s.push(0)
    print(f"Após push(0): {lista_s}")
    removido = lista_s.pop()
    print(f"Pop (item removido: {removido}): {lista_s}")
    print(f"Item no índice 1: {lista_s.find_at(1)}")
    print("-" * 40)

    # --- Teste da Classe Pilha ---
    print("\n--- Teste: Pilha ---")
    pilha = Pilha()
    print(f"Pilha está vazia? {pilha.is_empty()}")
    pilha.push('A')
    pilha.push('B')
    pilha.push('C')
    print(f"Pilha após 3 pushes: {pilha}")
    print(f"Tamanho da pilha: {len(pilha)}")
    print(f"Topo da pilha (peek): {pilha.peek()}")
    removido = pilha.pop()
    print(f"Pop (item removido: {removido}): {pilha}")
    print(f"Novo topo da pilha (peek): {pilha.peek()}")
    pilha.pop()
    pilha.pop()
    print(f"Pilha após mais 2 pops: {pilha}")
    print(f"Pilha está vazia? {pilha.is_empty()}")
    # A linha abaixo causaria um erro (descomente para testar)
    # pilha.pop()
    print("-" * 40)