"""
Trabalho de Programação Orientada a Objetos: Hierarquia de Classes de Estruturas de Dados Lineares.

Parte 2: Classe Array

Este arquivo contém as classes base e a implementação da classe Array.
"""

from abc import ABC, abstractmethod

# =============================================================================
# CLASSE BASE ABSTRATA (Da Parte 1)
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
        """
        Verifica se a estrutura está cheia.
        """
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
# NÓS PARA LISTAS ENCADEADAS (Serão usados depois)
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
# CLASSE ARRAY (DINÂMICO) - NOVA IMPLEMENTAÇÃO
# =============================================================================

class Array(EstruturaLinear):
    """
    Implementação de um Array Dinâmico que se expande quando necessário.
    Herda de EstruturaLinear.
    """
    def __init__(self, initial_capacity=10):
        """
        Construtor do Array.
        :param initial_capacity: A capacidade inicial do array interno.
        """
        self._data = [None] * initial_capacity
        self._size = 0
        self._capacity = initial_capacity

    def __len__(self):
        """Retorna o número de elementos armazenados no array."""
        return self._size

    def _resize(self, new_capacity):
        """
        Método privado para redimensionar o array interno.
        Normalmente, dobra a capacidade.
        """
        print(f"--- Array redimensionando de {self._capacity} para {new_capacity} ---")
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def __getitem__(self, index):
        """
        Permite acesso via indexação para consulta (Rvalue).
        Ex: var = arr[i]
        Lança um IndexError se o índice estiver fora dos limites.
        """
        if not 0 <= index < self._size:
            raise IndexError("Índice fora dos limites do array.")
        return self._data[index]

    def __setitem__(self, index, value):
        """
        Permite atribuição via indexação para atualização (Lvalue).
        Ex: arr[i] = valor
        Lança um IndexError se o índice estiver fora dos limites.
        """
        if not 0 <= index < self._size:
            raise IndexError("Índice fora dos limites do array.")
        self._data[index] = value

    def insert(self, item, index=None):
        """
        Insere um item no array.
        Se o índice não for fornecido, insere no final.
        Se o índice for fornecido, insere na posição especificada, deslocando os elementos.
        """
        if index is None:
            index = self._size

        if not 0 <= index <= self._size:
            raise IndexError("Índice de inserção fora dos limites.")

        # Redimensiona se a capacidade for atingida
        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        # Desloca elementos para a direita para abrir espaço
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i-1]

        self._data[index] = item
        self._size += 1

    def remove(self, index):
        """
        Remove e retorna o item no índice especificado.
        Lança um IndexError se o índice estiver fora dos limites.
        """
        if not 0 <= index < self._size:
            raise IndexError("Índice de remoção fora dos limites.")

        item_removido = self._data[index]
        # Desloca elementos para a esquerda
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i+1]

        self._data[self._size - 1] = None # Limpa a última posição
        self._size -= 1
        return item_removido

    def find(self, key):
        """
        Encontra e retorna a primeira ocorrência do item com a chave especificada.
        Lança um ValueError se a chave não for encontrada.
        """
        for i in range(self._size):
            if self._data[i] == key:
                return self._data[i]
        raise ValueError(f"Chave '{key}' não encontrada.")

    def __str__(self):
        """Representação em string do Array."""
        return f"Array: {str([self._data[i] for i in range(self._size)])}"

# =============================================================================
# BLOCO DE TESTE
# =============================================================================

if __name__ == "__main__":

    # --- Teste da Classe Array ---
    print("--- Teste: Classe Array ---")
    arr = Array(3)
    print(f"Array inicial: {arr}, Tamanho: {len(arr)}, Capacidade: {arr._capacity}")
    arr.insert(10)
    arr.insert(20)
    arr.insert(30)
    print(f"Após 3 inserções: {arr}")

    print("\nTentando inserir o 4º item (deve causar redimensionamento)...")
    arr.insert(40)
    print(f"Após 4ª inserção: {arr}, Tamanho: {len(arr)}, Capacidade: {arr._capacity}")

    arr.insert(5, index=1)
    print(f"\nApós inserir 5 no índice 1: {arr}")

    removido = arr.remove(2)
    print(f"Após remover do índice 2 (item removido: {removido}): {arr}")

    arr[0] = 99
    print(f"Após arr[0] = 99: {arr}")
    print("-" * 40)

    # --- Teste da Classe Matriz usando a Classe Array ---
    print("\n--- Teste: Classe Matriz usando a Classe Array ---")

    class Matriz:
        def __init__(self, linhas, colunas):
            self.linhas = linhas
            self.colunas = colunas
            # Usa a classe Array desenvolvida para armazenar as linhas
            self._data = Array(linhas)
            for i in range(linhas):
                # Cada linha é outro objeto Array
                self._data.insert(Array(colunas))
                for j in range(colunas):
                    self._data[i].insert(0) # Inicializa com zeros

        def __getitem__(self, pos):
            linha, coluna = pos
            return self._data[linha][coluna]

        def __setitem__(self, pos, valor):
            linha, coluna = pos
            self._data[linha][coluna] = valor

        def __str__(self):
            s = ""
            for i in range(self.linhas):
                # Constrói a representação da linha
                linha_str = [str(self._data[i][j]) for j in range(self.colunas)]
                s += "[" + ", ".join(linha_str) + "]\n"
            return s

    mat = Matriz(3, 4)
    print("Matriz 3x4 Inicializada:")
    print(mat)

    mat[1, 2] = 5
    mat[0, 0] = 9
    print("Matriz após atribuições (mat[1,2]=5, mat[0,0]=9):")
    print(mat)
    print(f"Valor em mat[1,2]: {mat[1,2]}")
    print("-" * 40)