class Produto:
    
    # Variáveis nome, preço, quantidade
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Inventario:
    def __init__(self):
        self.produtos = {}

    # Adicionar os produtos
    def adicionar_produto(self, produto, quantidade):
        if produto.nome in self.produtos:
            self.produtos[produto.nome].quantidade += quantidade
        else:
            self.produtos[produto.nome] = produto

    # Vender os produtos
    def vender_produto(self, nome_produto, quantidade):
        if nome_produto in self.produtos:
            produto = self.produtos[nome_produto]
            if produto.quantidade >= quantidade:
                produto.quantidade -= quantidade
                print(f"{quantidade} {nome_produto}(s) vendido(s) com sucesso.")
            else:
                print("Quantidade insuficiente em stock.")
        else:
            print("Produto não encontrado no inventário.")

    # Mostrar os produtos
    def mostrar_inventario(self):
        print("Inventário:")
        for produto in self.produtos.values():
            print(f"Nome: {produto.nome}, Preço: ${produto.preco}, Quantidade: {produto.quantidade}")


# Exemplo dos produtos
if __name__ == "__main__":
    # Criando alguns produtos
    produto1 = Produto("Laptop", 800, 10)
    produto2 = Produto("Smartphone", 250, 20)

    # Criar o inventário e adicionar os produtos
    inventario = Inventario()
    inventario.adicionar_produto(produto1, 5)
    inventario.adicionar_produto(produto2, 10)

    # Mostrar o inventário
    inventario.mostrar_inventario()

    # Vendeu alguns produtos
    inventario.vender_produto("Laptop", 2)
    inventario.vender_produto("Smartphone", 15)

    # Mostrar o inventário após as vendas
    inventario.mostrar_inventario()