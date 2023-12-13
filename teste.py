def funcao_classes():
    class Usuario:
        def __init__(self, email, senha):
            self.email = email
            self.senha = senha
            self.assinaturas = []
            self.cursos_inscritos = []

    class Video:
        def __init__(self, titulo, url):
            self.titulo = titulo
            self.url = url

    class Curso:
        def __init__(self, titulo, descricao):
            self.titulo = titulo
            self.descricao = descricao
            self.aulas = []

    class Aula:
        def __init__(self, conteudo, data):
            self.conteudo = conteudo
            self.data = data

    class ServicoStreaming:
        def __init__(self):
            self.usuarios = []
            self.videos = []
            self.cursos = []  # Lista de cursos no serviço de streaming

        def cadastrar_usuario(self, email, senha):
            novo_usuario = Usuario(email, senha)
            self.usuarios.append(novo_usuario)
            return novo_usuario

        def criar_curso(self, titulo, descricao):
            novo_curso = Curso(titulo, descricao)
            self.cursos.append(novo_curso)
            return novo_curso

        def adicionar_aula_ao_curso(self, curso, aula):
            curso.aulas.append(aula)

        def iniciar_aula(self, usuario, curso, aula):
            if curso in usuario.cursos_inscritos and aula in curso.aulas:
                print(f"{usuario.email} iniciou a aula: {aula.conteudo}")
            else:
                print("Você não está inscrito neste curso ou a aula não existe.")