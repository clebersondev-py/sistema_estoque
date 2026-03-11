import json
from funcoes import login_usuarios,cadastrar_usuarios,limpar_tela,pagina_principal
try:
    with open('usuarios.json', 'r') as arquivos:
        usuarios = json.load(arquivos) 

except FileNotFoundError:
    usuarios = {}
while True:
        print("MENU INICIAL")
        print("escolha uma opçao")
        print("1: cadastro")
        print("2: login")
        print("3: sair")
        escolha=input("sua escolha: ")

        if escolha not in ['1','2']:
            print("escolha um opção valida")
            continue
        
        elif escolha == '1':
             cadastrar_usuarios(usuarios)

        elif escolha == '2':
             nome=login_usuarios(usuarios)
             if nome:
                resultado=pagina_principal(usuarios,nome)
                if resultado == 'logout':
                     break


