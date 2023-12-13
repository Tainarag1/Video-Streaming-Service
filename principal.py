class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.assinaturas = []

class Video:
    def __init__(self, titulo, url):
        self.titulo = titulo
        self.url = url

class ServicoStreaming:
    def __init__(self):
        self.usuarios = []
        self.videos = []

    def cadastrar_usuario(self, email, senha):
        novo_usuario = Usuario(email, senha)
        self.usuarios.append(novo_usuario)
        return novo_usuario

    def cadastrar_video(self, titulo, url):
        novo_video = Video(titulo, url)
        self.videos.append(novo_video)
        return novo_video

    def assinar_video(self, usuario, video):
        usuario.assinaturas.append(video)
        print(f"{usuario.email} assinou o vídeo: {video.titulo}")

nome = input('Digite seu nome: ')
print("Olá, " + nome + "! Seja bem-vindo(a)!\nDigite o número correspondente a uma das opções: 1 - Já tenho cadastro, desejo acessar.\n2 - Não tenho cadastro, desejo me cadastrar.\n")

# Obtenha a escolha do usuário
x = int(input())

# Crie um serviço de streaming fora do bloco if
meu_servico = ServicoStreaming()

# Se o usuário deseja se cadastrar
if x == 2:
    # Solicite informações de cadastro
    usuario_email = input("Digite seu e-mail: ")
    usuario_senha = input("Digite sua senha: ")

    # Cadastre o usuário
    novo_usuario = meu_servico.cadastrar_usuario(usuario_email, usuario_senha)
    print(f"{nome} cadastrado com sucesso!")
# Se o usuário escolheu acessar cadastro
elif x == 1:
    # Solicite informações de acesso
    usuario_email = input("Digite seu e-mail: ")
    usuario_senha = input("Digite sua senha: ")

    # Verifique se o usuário está cadastrado
    usuario_encontrado = None
    for usuario in meu_servico.usuarios:
        if usuario.email == usuario_email and usuario.senha == usuario_senha:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        print(f"Bem-vindo de volta, {usuario_encontrado.email}!")
    else:
        print("Usuário não encontrado. Por favor, verifique suas informações de acesso.")

else:
    print('Número Inválido! Digite um novo número.')
