import json
import os 
import hashlib
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
            senha_hash=gerar_hash(senha)
            usuarios[usuario]={
                'senha':senha_hash
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
              return nome
         else:
              tentativas += 1
              print("usuario ou senha invalidos")
              continue
    print("numero maximo de tantativas atingidos!")
    return None
def pagina_principal(usuarios,nome):
      print(f"ola {nome}!")