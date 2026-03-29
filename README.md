# 🧩 [EDECD] Estrutura de Dados Estática, Composta e Dinâmica

> **CTeSP em Redes e Sistemas Informáticos** · ISTEC Porto · Ano letivo 2023/2024

---

## 📋 Informações da UC

| Campo | Detalhe |
|-------|---------|
| **Unidade Curricular** | Estrutura de Dados Estática, Composta e Dinâmica |
| **Curso** | CTeSP — Redes e Sistemas Informáticos |
| **Período Letivo** | 2.º Semestre |
| **Ano Curricular** | 1.º |
| **Ano letivo** | 2023 / 2024 |
| **Aluno** | Gonçalo Lopes Fernandes · Nº 2022148 |
| **Nota Final** | ⏳ A aguardar — prevista para maio de 2026 |

---

## 📁 Estrutura do Repositório

```
.
├── exercicios/
│   ├── Ficha_Diagnostico_EDECD.pdf              # Ficha de diagnóstico — 27 questões teóricas
│   └── Relatorio_Andre_Costa.docx               # Relatório complementar
├── material/
│   ├── 1Produto.png                             # Classe Produto — código
│   ├── 2Inventário.png                          # Classe Inventário — código
│   ├── 3Add_produto.png                         # Método adicionar_produto — código
│   ├── 4Vender_produto.png                      # Método vender_produto — código
│   ├── 5Mostrar_produto.png                     # Método mostrar_inventario — código
│   └── 6Exemplo_de_produtos_laptop_smart.png    # Exemplo de execução — código
├── projeto/
│   ├── Projeto_Final.pdf                        # Relatório do Projeto Final — 17/04/2024
│   └── Código_Gonçalo_Fernandes_148.py          # Código Python — Sistema de Gestão de Inventário
├── notas/
└── README.md
```

---

## 📝 Trabalhos Realizados

### Projeto Final — Sistema de Gestão de Inventário
**Aluno:** Gonçalo Fernandes · Nº 148 | **Data:** 17/04/2024

Desenvolvimento em Python de um programa orientado a objetos para gestão de stock de um armazém de produtos, aplicando os conceitos de estruturas de dados dinâmicas (dicionários).

**Classes implementadas:**

| Classe | Atributos / Métodos | Descrição |
|---|---|---|
| `Produto` | `nome`, `preco`, `quantidade` | Representa um produto com os seus dados |
| `Inventario` | `produtos` (dict) | Estrutura de dados dinâmica que armazena produtos |
| `Inventario` | `adicionar_produto()` | Adiciona produto ou incrementa quantidade se já existir |
| `Inventario` | `vender_produto()` | Reduz stock com validação de quantidade disponível |
| `Inventario` | `mostrar_inventario()` | Lista todos os produtos com nome, preço e quantidade |

**Exemplo de execução:**
```python
produto1 = Produto("Laptop", 800, 10)
produto2 = Produto("Smartphone", 250, 20)

inventario = Inventario()
inventario.adicionar_produto(produto1, 5)
inventario.adicionar_produto(produto2, 10)
inventario.mostrar_inventario()

inventario.vender_produto("Laptop", 2)        # → 2 Laptop(s) vendido(s) com sucesso.
inventario.vender_produto("Smartphone", 15)   # → Quantidade insuficiente em stock.
```

---

### Ficha de Diagnóstico — Estrutura de Dados
**Aluno:** Gonçalo Fernandes · Nº 148

Ficha teórica com 27 questões sobre fundamentos de programação e estruturas de dados:

| Tema | Questões |
|---|---|
| Bases de dados | Chaves primárias, grau de relação, SGBD gratuito |
| Algoritmos | Definição, fluxo de execução, estruturas de controlo |
| Tipos de dados | Primitivos, inteiros, float, strings, booleanos, arrays |
| Linguagens | Alto nível (Python, JS, Java, C#) vs. baixo nível (Assembly, C, C++) |
| Redes | Tipos de rede (LAN, MAN, WAN, VLAN), topologias |
| Programação | Variáveis, funções, diretiva `#include`, fluxogramas |

---

## 🧠 Temas Abordados na UC

| Tema | Conteúdo |
|------|----------|
| Estruturas Estáticas | Arrays, vetores, tipos de dados primitivos |
| Estruturas Compostas | Classes e objetos em Python (POO) |
| Estruturas Dinâmicas | Dicionários, listas dinâmicas, gestão de memória |
| POO | Definição de classes, atributos, métodos, `__init__` |
| Algoritmos | Estruturas sequenciais, de decisão e de repetição |
| Python | f-strings, condicionais, iteração com `for`, `if/else` |

---

## 📬 Contacto

**Gonçalo Fernandes** · [goncalo.fernandes.2022148@my.istec.pt](mailto:goncalo.fernandes.2022148@my.istec.pt)
