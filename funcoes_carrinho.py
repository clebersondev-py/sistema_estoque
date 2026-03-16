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
    if confirmar == 'sim':
        return "sim"

def pagamento(carrinho,produtos):
    escolha = input("Escolha a forma de pagamento (1: Cartão \n2: Boleto\n3: Pix): ")
    if escolha == '1':
        forma=input("(1: Crédito \n2: Débito): ")
        if forma == '1':
            print("Pagamento com Cartão de Crédito selecionado.")
            input("Pressione Enter para processar o pagamento...")
            print("Pagamento com Cartão de Crédito confirmado!")    
            
        elif forma == '2':
            print("Pagamento com Cartão de Débito selecionado.")
            input("Pressione Enter para processar o pagamento...")
            print("Pagamento com Cartão de Débito confirmado!") 
            
        else:
            print("Opção de pagamento inválida!")
    elif escolha == '2':
        print("Pagamento com Boleto selecionado.") 
        input("Pressione Enter para gerar o boleto...")
        print("Boleto gerado! Por favor, realize o pagamento para concluir a compra.")  
        input("Pressione Enter para confirmar o pagamento do boleto...")
        print("Pagamento do boleto confirmado!")   
           
    elif escolha == '3':
        print("Pagamento com Pix selecionado.")
        print("nossa chave Pix: 12345678900")
        input("Pressione Enter para confirmar o pagamento via Pix...")
        print("Pagamento via Pix confirmado!")  
        
        
    else:
        print("Opção de pagamento inválida!")

    atualizar_estoque(carrinho,produtos)
    carrinho.clear()
    print("Compra finalizada com sucesso!") 

def atualizar_estoque(carrinho,produtos):
    for item in carrinho:
        id_produto = item['id']
        quantidade_comprada = item['quantidade']
        if id_produto in produtos:
            produtos[id_produto]['estoque'] -= quantidade_comprada
    salvar_produto(produtos)