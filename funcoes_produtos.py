from funcoes_usuarios import limpar_tela,salvar_produto

def cadastrar_produto(produtos):
    proximo_id= max([int(k) for k in produtos.keys()]+[0])+1
    while True:
        nome = input("Digite o nome do produto: ")
        if nome in produtos:
            print("Produto já cadastrado!")
            continue
        if not nome:
            print("O nome do produto não pode estar vazio!")
            continue
        preco = float(input("Digite o preço do produto: "))
        if preco < 0:
            print("O preço do produto não pode ser negativo!")
            continue
        estoque = int(input("Digite a quantidade do produto: "))
        if estoque < 0:
            print("A quantidade do produto não pode ser negativa!")
            continue
        produtos[str(proximo_id)] = {
            'nome': nome,
            'preco': preco,
            'estoque': estoque
        }
        salvar_produto(produtos)
        print(f"Produto cadastrado com sucesso!")
        cadastro=input("Deseja cadastrar outro produto? (s/n): ").lower()
        if cadastro != 's':
            return
def remover_produto(produtos):
    while True:
        if not produtos:
            print("Nenhum produto cadastrado!")
            return
        
        id_produto = int(input("Digite o ID do produto que deseja remover: "))
        if id_produto in produtos:
            del produtos[id_produto]
            salvar_produto(produtos)
            print("Produto removido com sucesso!")
            limpar_tela()
            break

        else:
            print("Produto não encontrado!")
            continue

def visualizar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    
    print("Produtos disponíveis:")
    for id_produto, detalhes in produtos.items():
        print(f"ID: {id_produto}")
        print(f"Nome: {detalhes['nome']}")
        print(f"Preço: R$ {detalhes['preco']:.2f}")
        print(f"Estoque: {detalhes['estoque']} unidades")
        print("-" * 20)    

def comprar_produto(produtos,carrinho):
    
    while True:
        if not produtos:
            print("Nenhum produto disponível para compra!")
            return
        visualizar_produtos(produtos)
        id_produto = (input("Digite o ID do produto que deseja comprar: "))
        if id_produto in produtos:
            try:
                quantidade = int(input("Digite a quantidade que deseja comprar: "))
            except ValueError:
                print("Quantidade inválida!")
                continue
            if quantidade > produtos[id_produto]['estoque']:
                print("Quantidade solicitada excede o estoque disponível!")
                continue
            item={
                'id': id_produto,
                'nome': produtos[id_produto]['nome'],
                'preco': produtos[id_produto]['preco'],
                'quantidade': quantidade
            }
            carrinho.append(item)
            print(f"{quantidade} unidade(s) de {produtos[id_produto]['nome']} adicionada(s) ao carrinho!")
            adicionar_mais = input("Deseja adicionar mais produtos ao carrinho? (s/n): ").lower()
            if adicionar_mais != 's':
                break
        else:
            print("Produto não encontrado!")
            continue