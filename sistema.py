from modelo import *

#Sistema da plataforma

class Sistema:
    def __init__(self):
        self.id_plano = 0
        self.id_usuario = 0
        self.id_aula = 0
        self.id_categoria = 0
        self.Usuario = []
        self.Aula = []
        self.Plano = []
        self.categoria = []
        self.Aula_categoria = []
        self.Usuario_aula = []
        self.Usuario_plano = []


    #Adicianandoco um novo plano ao projeto
    def adicionar_plano(self):
        descricao = input('Digite uma descricao para o plano: ')
        valor = input('Digite o valor do plano: ')
        titulo = input("Digite um titulo para o plano: ")
        self.id_plano += 1
        id = self.id_plano
        plan = Plano(id, valor, titulo, descricao)
        self.Plano.append(plan)
        return plan

    
    
    #Busca um plano pelo identificador na lista de plano
    def procurar_plano(self):
        id = int(input('Digite o Id do plano:')) 
        for plan in self.Plano:
            if (plan.id == id):
                return plan
        
        return None

    #Lista todos os planos
    def listar_planos(self):
        for plan in self.Plano:
            print(f"\nId = {plan.id}, Titulo = {plan.titulo}, Descrição: {plan.descricao}, Valor = R${plan.valor}\n")



    #Decidindo o plano do usuario
    def escolher_plano(self, id_usuario):

        print('Esses são os planos disponíveis: ')
        sistema.listar_planos()
        id_plano = input('Digide o id do plano escolhido: ')

        plano_usuario = Usuario_plano(id_plano, id_usuario)
        self.Usuario_plano.append(plano_usuario)

        return plano_usuario


    #Cria uma nova categoria de aulas
    def adicionar_categoria(self, nome):
        nome = input("Digite o nome da Categoria: ")
        self.id_categoria += 1
        id = self.id_categoria
        cat = Categoria(id, nome)
        self.categoria.append(cat)
        return cat

    #Busca uma categoria pelo identificador na lista de categorias
    def procurar_categoria(self):
        id = int(input('Digite o Id da categoria:')) 
        for cat in self.categoria:
            if (cat.id == id):
                return cat
        
        return None

    #Lista todas as categorias
    def listar_categorias(self):
        for cat in self.categoria:
            print(f"Id = {cat.id}, Nome = {cat.nome}")

    #Adiciona uma aula na categoria
    def adicionar_aula_categoria(self, id_categoria, id_aula):
        aula_categoria = Aula_Categoria(id_categoria, id_aula)
        self.Aula_categoria.append(aula_categoria)

    
    #Adiciona uma nova aula
    def adicionar_aula_ao_curso(self):
        print('Digite o numero correspodente a uma das opcoes: \n1 - Adicionar a uma categoria existente\n2 - Criar uma nova categoria\n=> ')
        x = int(input())
        #Garantindo que o usuario escolheu uma opção valida
        is_valid = False
        while not is_valid:
            if x == 1:
                is_valid = True
                cat = self.procurar_categoria()
            elif(x == 2):
                is_valid = True
                cat = self.adicionar_categoria()
            else:
                print("Opcao inválida")
        #criando o objeto aula
        url = input('Digite o URL da aula:')
        titulo = input('Digite o titulo da aula:')
        self.id_aula += 1
        id = self.id_aula
        aul = Aula(id, url, titulo)
        self.aula.append(aul)
        self.adicionar_aula_categoria(cat.id, id)
        return aul
    
    
    
    def acessar_usuario(self):
        is_valid = False
        while not is_valid:
            email = input('\nDigite seu email: ')
            for usu in self.Usuario:
                if (usu.email == email):
                    senha = input('\nDigite sua senha: ')
                    for usu in self.usuario:
                        if usu.senha == senha:
                            is_valid = True
                            print('\nBem-vindo(a) de volta!\n')
                            return usu
                        else:  print('\nSenha incorreta. Tente novamente.\n')
                else: print('\nEmail invalido. Tente novamente.\n')        
        
        return None


    #Buscar se o email ja tem cadastro
    def procurar_usuario(self, email):
        for usu in self.Usuario:
            if (usu.email == email):
                return usu
        
        return None
    
    #adiciona novo usuario
    def adicionar_usuario(self, nome):
        email = input('Digite seu email:')
        if sistema.procurar_usuario(email) == None:
            senha = input('Digite uma senha:')
            self.id_usuario += 1
            id = self.id_usuario
            usu = Usuario(id, email, senha)
            self.Usuario.append(usu)
            print(f"Seja Bem-vindo(a), {nome}! Seu cadastro foi efetuado.")
            return usu
        else: 
            x = int(input('Email ja cadastrado! Digite o numero correspondente a uma das opções:\n1- Criar uma conta\n2- Acessar minha conta'))
            is_valid = False
            while not is_valid:
                if x == 1:
                    is_valid = True
                    sistema.adicionar_usuario(nome)
                elif(x == 2):
                    is_valid = True
                    sistema.acessar_usuario()
                else:
                    print("Opcao inválida")



#Iniciando o sistema
sistema = Sistema()


cat = self.adicionar_categoria('Matematica')

https://www.youtube.com/watch?v=5e8Ua4RhhXg', 'https://www.youtube.com/watch?v=1VjauwyHV0o', 'https://www.youtube.com/watch?v=o-srrvPTo0Y',
                     'https://www.youtube.com/watch?v=YTJPkVMdKho'



#coletando o nome do usuario
nome = input('Digite seu nome:')
print(f'Olá, {nome}! Seja Bem-vindo(a)! \nDigite o numero correspondente a uma das opções:\n1- Criar uma conta\n2- Acessar minha conta')

#Garantindo que o usuario escolheu uma opção valida
is_valid = False
while not is_valid:
    x = int(input())
    if x == 1:
        is_valid = True
        novo_usuario = sistema.adicionar_usuario(nome)
        id_usuario = novo_usuario.id
        sistema.escolher_plano(id_usuario)

    elif(x == 2):
        is_valid = True
        sistema.acessar_usuario()
    else:
        print("Opcao inválida. Tente novamente. \nDigite o numero correspondente a uma das opções:\n1- Criar uma conta\n2- Acessar minha conta")





#sistema.adicionar_categoria()
#sistema.adicionar_categoria()
#sistema.listar_categorias()
#print(sistema.procurar_categoria().__dict__)
