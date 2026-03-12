import json
import os 
import hashlib
senha_administrativa='123456'
def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()
def salvar_produto(produtos):
     with open('produtos.json','w') as arquivos:
          json.dump(produtos,arquivos,indent=4)


def salvar_usuario(usuarios):
    with open('usuarios.json','w') as arquivos:
        json.dump(usuarios,arquivos,indent=4)

def limpar_tela():
    input("digite enter pra continuar!")
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_usuarios(usuarios):
    while True:
            print('Faça seu cadastro!')
            usuario=input("seu usuario: ").strip()
            
            if not usuario:
                print("usuario não pode estar vazio")
                continue
            if usuario in usuarios:
                 print("esse usuario ja existe")
                 continue
            
            senha=input("sua senha: ")
            

            if len(senha) < 6:
                print("senha muito curta") 
                continue

            admin=input("Essa conta é de um admim :").lower().strip()
            print("sim")
            print("nao")
            if admin != "sim":
                senha_hash=gerar_hash(senha)
                usuarios[usuario]={
                    'senha':senha_hash,
                    'tipo': 'user'
                }
                print("cadastro realizado!")
                salvar_usuario(usuarios)
                limpar_tela()
                break
            else:
                confirmação=input("digite a senha administrativa:")
                if confirmação == senha_administrativa:
                    senha_hash=gerar_hash(senha)
                    usuarios[usuario]={
                        'senha':senha_hash,
                        'tipo': 'admin'
                    }
                    print("cadastro realizado!")
                    salvar_usuario(usuarios)
                    limpar_tela()
                    break
            

def login_usuarios(usuarios):
    tentativas=0
    maximo_tentativas=3

    while tentativas < maximo_tentativas:
         print("faça login aqui!")

         nome=input("digite seu usuario: ").strip()
         if not nome:
              print("usuario não pode estar vazio")
              continue
         senha=input("digite sua senha: ")
         if not senha:
              print("senha não pode estar vazia!")
              continue
         senha_hash=gerar_hash(senha)
         if nome in usuarios and usuarios[nome]['senha'] == senha_hash:
              print("login realizado")
              limpar_tela()
              return nome ,usuarios[nome]['tipo']
         else:
              tentativas += 1
              print("usuario ou senha invalidos")
              continue
    print("numero maximo de tantativas atingidos!")
    return None
def pagina_principal(nome,tipo,produtos):
    while True:
        
        if tipo == "user":
            print(f"Ola ,seja bem  vindo {nome}!")

            escolha=input("escolha uma opção para prosseguir: ")
            print("1:visualizar produtos")
            print("2:comprar")
            print("3:sair")
            if escolha in("1","2","3"):
                return escolha
            else:
                print("escolha uma opção valida")
                continue
        elif tipo == "admin":
            print(f"Olá,seja bem vindo {nome}!")

            escolha2=input("escolha uma opção para prosseguir: ")
            print("1:cadastrar produto!")
            print("2:remover produto")
            print("3:visualizar produtos")
            print("4:comprar")
            print("5:sair")
            if escolha2 in("1","2","3""4","5"):
                return escolha2
            else:
                print("escolha uma opção valida")
                continue

