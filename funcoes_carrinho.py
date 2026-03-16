from funcoes_produtos import salvar_produto,limpar_tela
def finalizar_compra(carrinho,produtos):
    if not carrinho:
        print("O carrinho está vazio!")
        return
    
    total = sum(item['preco'] * item['quantidade'] for item in carrinho)
    print("Itens no carrinho:") 
    for item in carrinho:
        print(f"{item['nome']} - Quantidade: {item['quantidade']} - Preço unitário: R$ {item['preco']:.2f}")    
    print(f"Total da compra: R$ {total:.2f}")
    confirmar = input("Deseja finalizar a compra? (sim/não): ").strip().lower()
    if confirmar == "sim":
        for item in carrinho:
            produtos[item['id']]['estoque'] -= item['quantidade']
        salvar_produto(produtos)
        carrinho.clear()
        print("Compra finalizada com sucesso!")
        limpar_tela()