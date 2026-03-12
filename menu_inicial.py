import json
from funcoes_usuarios import login_usuarios,cadastrar_usuarios,limpar_tela,pagina_principal
try:
    with open('usuarios.json', 'r') as arquivos:
        usuarios = json.load(arquivos) 

except FileNotFoundError:
    usuarios = {}

try:
     with open ('produtos','r') as arquivos:
        produtos =json.load(arquivos)
except FileNotFoundError:
    produtos = {}
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
             resultado=login_usuarios(usuarios)

             if resultado:
                  nome,tipo=resultado
                  pagina_principal(nome,tipo,produtos)
             
                
                 


