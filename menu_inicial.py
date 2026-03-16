import json
from funcoes_usuarios import login_usuarios,cadastrar_usuarios,limpar_tela,pagina_principal
from funcoes_produtos import cadastrar_produto,visualizar_produtos,comprar_produto,remover_produto
from funcoes_carrinho import finalizar_compra,pagamento
carrinho = []
try:
    with open('usuarios.json', 'r') as arquivos:
        usuarios = json.load(arquivos) 

except FileNotFoundError:
    usuarios = {}

try:
     with open ('produtos.json','r') as arquivos:
        produtos =json.load(arquivos)
except FileNotFoundError:
    produtos = {}
while True:
        print("=" * 20 )
        print("MENU INICIAL")
        print("=" * 20 )
        print("escolha uma opçao")
        print("1: cadastro")
        print("2: login")
        print("3: sair")
        escolha=input("sua escolha: ")

        if escolha not in ['1','2','3']:
            print("escolha um opção valida")
            continue
        
        elif escolha == '1':
             cadastrar_usuarios(usuarios)

        elif escolha == '2':
             resultado=login_usuarios(usuarios)

             if resultado:
                  nome,tipo=resultado
                  while True:
                        escolha2=pagina_principal(nome,tipo,produtos)
                        if escolha2 == "1" and tipo == "admin":
                                cadastrar_produto(produtos)
                        elif escolha2 == "2" and tipo == "admin":
                                remover_produto(produtos)  
                        elif escolha2 == "3" and tipo == "admin":
                                visualizar_produtos(produtos)
                        elif escolha2 == "4" and tipo == "admin":
                                comprar=comprar_produto(produtos,carrinho)
                                if comprar == 'comprar':
                                    finalizar=finalizar_compra(carrinho,produtos)
                                    if finalizar == "sim":
                                        pagamento(carrinho,produtos)
