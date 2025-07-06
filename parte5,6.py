"""
Trabalho de Programação Orientada a Objetos: Hierarquia de Classes de Estruturas de Dados Lineares.

Parte 5 e 6: Classe ListaDuplamenteEncadeada e Classe Fila

Este arquivo contém:
- As classes base e as implementações anteriores (Lista Simples, Pilha).
- A implementação da Classe ListaDuplamenteEncadeada.
- A implementação da Classe Fila, que utiliza a Lista Dupla por composição.
- A resolução dos problemas da "Fila de Prioridades" e "Fila do Bandejão".
"""

from abc import ABC, abstractmethod
import datetime

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
# CLASSE LISTA SIMPLESMENTE ENCADEADA (Das partes anteriores)
# =============================================================================

class ListaSimplesmenteEncadeada(EstruturaLinear):
    def __init__(self, iterable=None):
        self._head = None
        self._size = 0
        if iterable:
            for item in reversed(iterable):
                self.push(item)
    def __len__(self): return self._size
    def push(self, item):
        new_node = Node(item)
        new_node.next = self._head
        self._head = new_node
        self._size += 1
    def pop(self):
        if self.is_empty(): raise IndexError("Remoção de uma lista vazia (underflow).")
        item_removido = self._head.data
        self._head = self._head.next
        self._size -= 1
        return item_removido
    def find_at(self, index):
        if not 0 <= index < self._size: raise IndexError("Índice fora dos limites.")
        current = self._head
        for _ in range(index): current = current.next
        return current.data
    def insert(self, item, **kwargs): self.push(item)
    def remove(self, **kwargs): return self.pop()
    def find(self, key, **kwargs):
        current = self._head
        while current:
            if current.data == key: return current.data
            current = current.next
        raise ValueError(f"Chave '{key}' não encontrada.")
    def __str__(self):
        items = []
        current = self._head
        while current:
            items.append(str(current.data))
            current = current.next
        return f"ListaSimples: [{' -> '.join(items)}]"

# =============================================================================
# CLASSE PILHA (STACK) - (Das partes anteriores)
# =============================================================================

class Pilha(EstruturaLinear):
    def __init__(self): self._lista = ListaSimplesmenteEncadeada()
    def __len__(self): return len(self._lista)
    def push(self, item): self._lista.push(item)
    def pop(self):
        if self.is_empty(): raise IndexError("Pilha vazia (Stack underflow).")
        return self._lista.pop()
    def peek(self):
        if self.is_empty(): raise IndexError("Pilha vazia.")
        return self._lista.find_at(0)
    def insert(self, item, **kwargs): self.push(item)
    def remove(self, **kwargs): return self.pop()
    def find(self, **kwargs): return self.peek()
    def __str__(self): return f"Pilha(topo={self._lista})"

# =============================================================================
# CLASSE LISTA DUPLAMENTE ENCADEADA (NOVA - Parte 5)
# =============================================================================

class ListaDuplamenteEncadeada(EstruturaLinear):
    """Implementação de uma Lista Duplamente Encadeada."""
    def __init__(self, iterable=None):
        self._head = None
        self._tail = None
        self._size = 0
        if iterable:
            for item in iterable:
                self.push_back(item)

    def __len__(self):
        return self._size

    def push(self, item):
        """Insere um item no início da lista (O(1))."""
        new_node = DoubleNode(item)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def push_back(self, item):
        """Insere um item no fim da lista (O(1))."""
        new_node = DoubleNode(item)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def pop(self):
        """Remove e retorna o item do início da lista (O(1))."""
        if self.is_empty(): raise IndexError("Remoção de uma lista vazia (underflow).")
        item_removido = self._head.data
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._size -= 1
        return item_removido

    def pop_back(self):
        """Remove e retorna o item do fim da lista (O(1))."""
        if self.is_empty(): raise IndexError("Remoção de uma lista vazia (underflow).")
        item_removido = self._tail.data
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._size -= 1
        return item_removido

    def find_at(self, index):
        """Consulta (sem remover) o item na i-ésima posição."""
        if not 0 <= index < self._size: raise IndexError("Índice fora dos limites.")
        current = self._head
        for _ in range(index): current = current.next
        return current.data

    def swap(self, index1, index2):
        """Troca os dados de dois nós em posições sucessivas."""
        if index1 > index2: index1, index2 = index2, index1
        if index2 != index1 + 1 or not (0 <= index1 < self._size and 0 <= index2 < self._size):
            raise ValueError("A troca só pode ocorrer entre posições sucessivas e válidas.")
        
        node1 = self._head
        for _ in range(index1): node1 = node1.next
        node2 = node1.next
        
        node1.data, node2.data = node2.data, node1.data

    def bubble_sort(self, key=lambda x: x):
        """Ordena a lista usando o algoritmo Bubble Sort, com base numa chave."""
        if self._size < 2: return
        for i in range(self._size):
            current = self._head
            for j in range(self._size - i - 1):
                if key(current.data) > key(current.next.data):
                    current.data, current.next.data = current.next.data, current.data
                current = current.next

    # --- Implementação dos métodos abstratos ---
    def insert(self, item, **kwargs): self.push_back(item)
    def remove(self, **kwargs): return self.pop_back()
    def find(self, key_value, **kwargs):
        current = self._head
        while current:
            if current.data == key_value: return current.data
            current = current.next
        raise ValueError(f"Chave '{key_value}' não encontrada.")
    def __str__(self):
        items = []
        current = self._head
        while current:
            items.append(str(current.data))
            current = current.next
        return f"ListaDupla: [{' <-> '.join(items)}]"

# =============================================================================
# CLASSE FILA (QUEUE) - (NOVA - Parte 6)
# =============================================================================

class Fila(EstruturaLinear):
    """
    Implementação de uma Fila (Queue) usando composição com
    ListaDuplamenteEncadeada. A lógica é FIFO (First-In, First-Out).
    """
    def __init__(self):
        self._lista = ListaDuplamenteEncadeada()

    def __len__(self):
        return len(self._lista)

    def enqueue(self, item):
        """Adiciona um item ao final da fila (O(1))."""
        self._lista.push_back(item)

    def dequeue(self):
        """Remove e retorna o item do início da fila (O(1))."""
        if self.is_empty(): raise IndexError("Fila vazia (Queue underflow).")
        return self._lista.pop()

    def peek(self):
        """Retorna o item do início da fila sem removê-lo."""
        if self.is_empty(): raise IndexError("Fila vazia.")
        return self._lista.find_at(0)

    def remove_item(self, item_to_remove):
        """Remove um item específico da fila (para desistências)."""
        current = self._lista._head
        while current:
            if current.data == item_to_remove:
                if current.prev: current.prev.next = current.next
                else: self._lista._head = current.next
                
                if current.next: current.next.prev = current.prev
                else: self._lista._tail = current.prev
                
                self._lista._size -= 1
                return True
            current = current.next
        return False

    # --- Implementação dos métodos abstratos ---
    def insert(self, item, **kwargs): self.enqueue(item)
    def remove(self, **kwargs): return self.dequeue()
    def find(self, **kwargs): return self.peek()
    def __iter__(self):
        current = self._lista._head
        while current:
            yield current.data
            current = current.next
    def __str__(self): return f"Fila: {str(self._lista)}"

# =============================================================================
# RESOLUÇÃO DOS PROBLEMAS
# =============================================================================

class FilaDePrioridades(ListaDuplamenteEncadeada):
    """
    Implementação de uma Fila de Prioridades.
    Herda da Lista Duplamente Encadeada e insere os itens de forma ordenada.
    """
    def __init__(self, key=lambda x: x['prioridade']):
        super().__init__()
        self.key = key

    def insert_ordered(self, item):
        """Insere um item mantendo a ordem de prioridade (menor para maior)."""
        if self.is_empty() or self.key(item) < self.key(self._head.data):
            self.push(item)
        elif self.key(item) >= self.key(self._tail.data):
            self.push_back(item)
        else:
            new_node = DoubleNode(item)
            current = self._head
            while self.key(current.data) < self.key(item):
                current = current.next
            
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
            self._size += 1

    def get_highest_priority(self):
        """Retorna o item de maior prioridade (o primeiro da lista)."""
        return self.pop()

class FilaBandejao:
    """Simulação do problema da fila do bandejão."""
    class Usuario:
        def __init__(self, nome, id_usuario):
            self.nome = nome
            self.id = id_usuario
            self.hora_estimada_atendimento = None
        def __repr__(self): return f"Usuario({self.nome}, ID:{self.id})"

    def __init__(self, tempo_medio_atendimento_min=2):
        self.fila_de_pedidos = Fila()
        self.tempo_medio_atendimento = datetime.timedelta(minutes=tempo_medio_atendimento_min)
        self.proximo_id = 1

    def estimar_tempo_espera(self):
        return len(self.fila_de_pedidos) * self.tempo_medio_atendimento

    def entrar_na_fila(self, nome_usuario):
        agora = datetime.datetime.now()
        tempo_espera = self.estimar_tempo_espera() + self.tempo_medio_atendimento
        usuario = self.Usuario(nome_usuario, self.proximo_id)
        self.proximo_id += 1
        usuario.hora_estimada_atendimento = agora + tempo_espera
        self.fila_de_pedidos.enqueue(usuario)
        print(f"\n>> {usuario.nome} entrou na fila. Posição: {len(self.fila_de_pedidos)}, Retirada às: {usuario.hora_estimada_atendimento.strftime('%H:%M:%S')}")
        return usuario

    def atender_proximo(self):
        if self.fila_de_pedidos.is_empty():
            print("\nFila vazia. Ninguém para atender.")
            return None
        usuario_atendido = self.fila_de_pedidos.dequeue()
        print(f"\n<< {usuario_atendido.nome} foi atendido.")
        self.atualizar_tempos_todos()
        return usuario_atendido

    def desistir(self, usuario):
        if self.fila_de_pedidos.remove_item(usuario):
            print(f"\n!! {usuario.nome} desistiu e foi removido da fila.")
            self.atualizar_tempos_todos()
        else:
            print(f"\n!! {usuario.nome} não encontrado na fila.")

    def atualizar_tempos_todos(self):
        print("   -- Atualizando tempos de espera de todos na fila... --")
        agora = datetime.datetime.now()
        tempo_acumulado = datetime.timedelta()
        for usuario in self.fila_de_pedidos:
            tempo_acumulado += self.tempo_medio_atendimento
            usuario.hora_estimada_atendimento = agora + tempo_acumulado
            print(f"      - {usuario.nome}: Novo horário estimado {usuario.hora_estimada_atendimento.strftime('%H:%M:%S')}")

    def visualizar_fila(self):
        print("\n--- Fila do Bandejão Atual ---")
        if self.fila_de_pedidos.is_empty():
            print("A fila está vazia.")
            return
        for i, usuario in enumerate(self.fila_de_pedidos):
            print(f"{i+1}. {usuario.nome} - Retirada às: {usuario.hora_estimada_atendimento.strftime('%H:%M:%S')}")
        print("----------------------------")

# =============================================================================
# BLOCO DE TESTE
# =============================================================================

if __name__ == "__main__":
    # --- Teste da Classe Lista Duplamente Encadeada ---
    print("--- Teste: Lista Duplamente Encadeada ---")
    lista_d = ListaDuplamenteEncadeada([10, 30, 20])
    print(f"Lista inicial: {lista_d}")
    lista_d.push(0)
    lista_d.push_back(40)
    print(f"Após push(0) e push_back(40): {lista_d}")
    print(f"Pop: {lista_d.pop()}, Pop Back: {lista_d.pop_back()}")
    print(f"Lista após pops: {lista_d}")
    print("Ordenando a lista com bubble sort...")
    lista_d.bubble_sort()
    print(f"Lista ordenada: {lista_d}")
    print("-" * 40)

    # --- Teste da Classe Fila ---
    print("\n--- Teste: Fila ---")
    fila = Fila()
    fila.enqueue('X'); fila.enqueue('Y'); fila.enqueue('Z')
    print(f"Fila: {fila}")
    print(f"Primeiro (peek): {fila.peek()}")
    print(f"Dequeue: {fila.dequeue()}")
    print(f"Fila após dequeue: {fila}")
    print("-" * 40)

    # --- Teste da Fila de Prioridades ---
    print("\n--- Teste: Fila de Prioridades ---")
    fila_p = FilaDePrioridades()
    fila_p.insert_ordered({'tarefa': 'Lavar louça', 'prioridade': 3})
    fila_p.insert_ordered({'tarefa': 'Pagar conta', 'prioridade': 1})
    fila_p.insert_ordered({'tarefa': 'Estudar POO', 'prioridade': 2})
    print(f"Fila de prioridades: {fila_p}")
    print("Atendendo tarefas por prioridade:")
    while not fila_p.is_empty():
        tarefa = fila_p.get_highest_priority()
        print(f"- Atendendo: {tarefa['tarefa']} (Prioridade: {tarefa['prioridade']})")
    print("-" * 40)

    # --- Teste da Fila do Bandejão ---
    print("\n--- Teste: Problema da Fila do Bandejão ---")
    bandejao = FilaBandejao(tempo_medio_atendimento_min=1)
    user_ana = bandejao.entrar_na_fila("Ana")
    user_bruno = bandejao.entrar_na_fila("Bruno")
    user_carla = bandejao.entrar_na_fila("Carla")
    bandejao.visualizar_fila()
    bandejao.atender_proximo()
    bandejao.desistir(user_carla)
    bandejao.visualizar_fila()
    print("-" * 40)