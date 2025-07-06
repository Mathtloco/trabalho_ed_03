# trabalho_ed_03

# Trabalho de Programação Orientada a Objetos  
## Hierarquia de Classes de Estruturas de Dados Lineares
---

## 📘 Objetivo

Este projeto tem como finalidade implementar uma **hierarquia de classes para estruturas de dados lineares**, aplicando conceitos de **Programação Orientada a Objetos (POO)** com o uso de herança, composição e polimorfismo.

---

## 📁 Organização do Projeto

O projeto está dividido em quatro partes principais:

1. **Parte 1**: Definição da classe abstrata `EstruturaLinear` e das classes auxiliares `Node` e `DoubleNode`.
2. **Parte 2**: Implementação da classe `Array`, um array dinâmico com redimensionamento automático.
3. **Parte 3**: Implementação da classe `ListaSimplesmenteEncadeada`, utilizando nós encadeados.
4. **Parte 4**: Implementação da classe `Pilha`, baseada na lista encadeada, com interface LIFO.

---

## 🧠 Estruturas de Dados Utilizadas

- **Array Dinâmico**: baseado em listas Python, com redimensionamento automático.
- **Lista Encadeada**: usa `Node` com ponteiro para o próximo.
- **Pilha**: usa **composição** com a lista encadeada para implementar a lógica LIFO (último a entrar, primeiro a sair).

---

## 🔍 Descrição das Principais Funções

| Função / Método     | Estrutura         | Descrição                                                                 | Complexidade |
|---------------------|-------------------|---------------------------------------------------------------------------|--------------|
| `insert(item)`      | Array / Lista     | Insere um item (no fim ou início)                                        | O(n) / O(1)  |
| `remove(index)`     | Array / Lista     | Remove elemento por índice ou topo                                       | O(n) / O(1)  |
| `find(key)`         | Array / Lista     | Busca por valor                                                          | O(n)         |
| `push(item)`        | Lista / Pilha     | Insere no início ou no topo                                              | O(1)         |
| `pop()`             | Lista / Pilha     | Remove do início ou do topo                                              | O(1)         |
| `peek()`            | Pilha             | Visualiza o topo da pilha                                                | O(1)         |
| `_resize(capacity)` | Array             | Dobra a capacidade do array                                              | O(n)         |

---

## ⏱️ Complexidade

### Tempo

- **Array**: O(1) para inserções no final (amortizado); O(n) para inserção no meio.
- **Lista**: inserções/remoções no início são O(1); busca é O(n).
- **Pilha**: push/pop/peek são O(1).

### Espaço

- **Array**: pré-alocação de memória, o que pode gerar espaços vazios.
- **Lista**: usa memória sob demanda, mas com overhead de ponteiros.
- **Pilha**: depende da lista.

---

## ⚠️ Problemas e Observações

- Foi necessário cuidar do redimensionamento do `Array` com cópia manual de elementos.
- A inicialização da lista encadeada com iterável exigiu inserção em ordem reversa.
- O uso de **interfaces genéricas** como `insert` e `remove` nas subclasses facilitou a extensão e reuso.
- A classe `Matriz` foi criada apenas como exemplo de composição utilizando a classe `Array`.

---

## ✅ Conclusão

Este projeto demonstrou, na prática, a aplicação de **POO** em estruturas de dados. Através da herança e da composição, foi possível implementar classes reutilizáveis, organizadas e extensíveis. A hierarquia `EstruturaLinear` permitiu garantir que cada estrutura possuísse uma interface comum, favorecendo polimorfismo e testes.

---

## 🗂️ Estrutura de Diretórios Sugerida

