"""
Trabalho de Programação Orientada a Objetos: Hierarquia de Classes de Estruturas de Dados Lineares.

Parte 1: Classes Base

Este arquivo contém as classes fundamentais para a hierarquia:
- EstruturaLinear: A classe base abstrata que define a interface comum.
- Node e DoubleNode: As classes de nós para as listas encadeadas.
"""

from abc import ABC, abstractmethod

# =============================================================================
# CLASSE BASE ABSTRATA
# =============================================================================

class EstruturaLinear(ABC):
    """
    Classe abstrata que define a interface comum para todas as estruturas
    de dados lineares na hierarquia.

    Força as subclasses a implementarem um conjunto mínimo de funcionalidades.
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
        Verifica se a estrutura está cheia. Por padrão, estruturas dinâmicas
        não ficam cheias, a menos que a memória se esgote.
        Subclasses com tamanho fixo devem sobrescrever este método.
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
# NÓS PARA LISTAS ENCADEADAS
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