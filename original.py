from modelo import *

#Após importar a pasta adjunta do projeto, iniciamos a construcao do Sistema da plataforma

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
        self.Categoria_plano = []


    #Adicianando um novo plano ao projeto
    def adicionar_plano(self, descricao, valor, titulo):
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
            print(f"\nId = {plan.id}\nTitulo = {plan.titulo}\nDescrição: {plan.descricao}\nValor = R${plan.valor}\n")



    #Decidindo o plano do usuario
    def escolher_plano(self, id_usuario):

        print('Esses são os planos disponíveis: ')
        self.listar_planos()
        id_plano = input('Digide o id do plano escolhido: ')

        plano_usuario = Usuario_plano(id_plano, id_usuario)
        self.Usuario_plano.append(plano_usuario)

        return id_plano
    
    def obter_id_plano(self, id_usuario):
        for relacao in self.Usuario_plano:
            if relacao.id_usuario == id_usuario:
                return relacao.id_plano
        return None



    #Cria uma nova categoria de aulas
    def adicionar_categoria(self, nome):
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

    #Adiciona uma categoria no plano
    def adicionar_categoria_plano(self, id_categoria, id_plano):
        cat_plan = Categoria_plano(id_categoria, id_plano)
        self.Categoria_plano.append(cat_plan)
        return cat_plan

    def obter_id_categoria(self, id_plano):
        for cat_plan in self.Categoria_plano:
            plano_id_int = int(cat_plan.plano_id)

            if (plano_id_int == id_plano):
                return cat_plan.categoria_id
    
        return None

    #Adiciona uma aula na categoria
    def adicionar_aula_categoria(self, id_categoria, id_aula):
        aula_categoria = Aula_Categoria(id_categoria, id_aula)
        self.Aula_categoria.append(aula_categoria)

    def obter_id_aula(self, id_categoria):

        for aula_categoria in self.Aula_Categoria:
            if(aula_categoria.id_categoria == id_categoria):
                return aula_categoria.id_aula

        return None


    #Adiciona uma nova aula
    def adicionar_aula_ao_curso(self, url, titulo, id_categoria):
        self.id_aula += 1
        id = self.id_aula
        aul = Aula(id, url, titulo)
        self.Aula.append(aul)
        self.adicionar_aula_categoria(id_categoria, id)
        return aul
    
    
    
    def acessar_usuario(self):
        while True:
            email = input('\nDigite seu email (ou digite 0 para voltar ao menu principal): ')
            
            if email == '0':
                return None  # Retorna None para indicar a opção de voltar ao menu principal
            
            for usu in self.Usuario:
                if usu.email == email:
                    senha = input('\nDigite sua senha: ')
                    if usu.senha == senha:
                        print('\nBem-vindo(a) de volta!\n')
                        return usu
                    else:
                        print('\nSenha incorreta. Tente novamente.\n')
                    break  # Sair do loop for quando o usuário é encontrado
            else:
                print('\nEmail inválido. Tente novamente.\n')
        return None
        
    def procurar_aula_por_id(self, id_aula):
        for aula in self.Aula:
            if aula.id == id_aula:
                print(f'Aula encontrada: {aula.url}')
                return aula
        print(f'Aula com ID {id_aula} não encontrada.')
        return None

    def listar_videos_por_categoria(self, id_plano):
        id = int(id_plano)
        if id == 1:

            for aul in self.Aula:
                print(aula.id)
                x = int(aula.id)
                if x == 1:
                    print("A URL da aula com ID 1 é: {}".format(aula.url))
                    return



            print("Seu plano é: DESAFIO GEOMÉTRICO\nAqui estão as aulas da sua categoria: ")

            for aul in Aula:
                print(f"\nID da Aula: {aula_item.id}\nTítulo: {aula_item.titulo}\nURL: {aula_item.url}\n")




        elif(id == 2):
            print("Seu plano é: DESAFIO DE EQUAÇÕES")


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

#criando uma categoria
cat = sistema.adicionar_categoria('GEOMETRIA')
id_categoria = cat.id

#criando as primeiras aulas
aula = sistema.adicionar_aula_ao_curso('https://www.youtube.com/watch?v=5e8Ua4RhhXg', 'Poligonos', id_categoria)
id_aula = aula.id

#adicionando as aulas na categoria criada
sistema.adicionar_aula_categoria(id_categoria, id_aula)

#Repetindo o processo para cadastrar outras aulas.
aula = sistema.adicionar_aula_ao_curso( 'https://www.youtube.com/watch?v=o-srrvPTo0Y', 'Angulos e Retas', id_categoria)
id_aula = aula.id
sistema.adicionar_aula_categoria(id_categoria, id_aula)


#criando um plano
plano = sistema.adicionar_plano('Adquira uma compreensão abrangente da geometria, desde seus princípios fundamentais até suas aplicações práticas e dimensões avançadas', 50, 'Desafios Geometricos')
id_plano = plano.id
#adicionando uma categoria a um plano
sistema.adicionar_categoria_plano(id_categoria, id_plano)

#criando outra categoria
cat = sistema.adicionar_categoria('EQUACOES')
id_categoria = cat.id

aula = sistema.adicionar_aula_ao_curso('https://www.youtube.com/watch?v=1VjauwyHV0o', 'Equação do Segundo Grau', id_categoria)
id_aula = aula.id
sistema.adicionar_aula_categoria(id_categoria, id_aula)


aula = sistema.adicionar_aula_ao_curso('https://www.youtube.com/watch?v=YTJPkVMdKho', 'Sistema de Equacoes', id_categoria)
id_aula = aula.id
sistema.adicionar_aula_categoria(id_categoria, id_aula)

#Criando o segundo plano
plano = sistema.adicionar_plano('Desbrave o universo dos sistemas de equações por meio de uma abordagem educacional meticulosa, explorando desde os fundamentos até aplicações práticas', 50, 'Desafios de Equacoes')
id_plano = plano.id
sistema.adicionar_categoria_plano(id_categoria, id_plano)


#coletando o nome do usuario
nome = input('Digite seu nome:')

#Garantindo que o usuario escolheu uma opção valida
while True:
    print(f"Olá, {nome}! Seja Bem-vindo(a)!\nVocê está no menu principal!\nDigite o número correspondente a uma das opções:")
    print("1- Criar uma conta\n2- Acessar minha conta\n3- Sair")

    x = int(input())

    if x == 1:
        novo_usuario = sistema.adicionar_usuario(nome)
        id_usuario = novo_usuario.id
        print("Agora escolha uma das opções:")
        print("1- Escolher plano\n2- Voltar ao menu principal")

        y = int(input())

        if y == 1:
            id_plano = sistema.escolher_plano(id_usuario)
            if(id_plano == '1'):
                opcao = 1

            elif(id_plano == '2'):
                opcao = 2

            else:
                print('QUALLLLLLLLLLLLLLLLLLLLLLLLLLLLLL OPCAO')


            print("Plano escolhido!")

        elif y == 2:
            # Voltar ao menu principal
            continue

    elif x == 2:
        novo_usuario = sistema.acessar_usuario()
        if(novo_usuario == None):
            continue
        else:
            id_usuario = novo_usuario.id
            print(f"Bem-vindo(a) de volta, {novo_usuario.nome}!")
            break

    elif x == 3:
        print("Saindo do programa. Até logo!")
        exit()

    else:
        print("Opção inválida. Tente novamente.")

    print("Agora escolha uma das opções:")
    y = int(input('\n1- Listar Videos\n2- Voltar ao menu principal: '))


    if(y == 1):
        if(opcao == 1):
            print('A seguir está o link dos vídeos, clique para assistir: \nVídeo Poligonos: https://www.youtube.com/watch?v=5e8Ua4RhhXg \n Vídeo Angulos e Retas: https://www.youtube.com/watch?v=o-srrvPTo0Y')
        elif(opcao == 2):
            print('A seguir está o link dos vídeos, clique para assistir: \nVídeo Equacao do Segundo Grau: https://www.youtube.com/watch?v=1VjauwyHV0o \nVídeo Sistemas de Equacoes: https://www.youtube.com/watch?v=YTJPkVMdKho')

    else:


        print("\nOperação concluída. Obrigado por usar nosso sistema!")

        # Adicionando uma mensagem de despedida
        print("Deseja realizar mais alguma operação?")
        print("1- Sim\n2- Sair")

        opcao_final = int(input())

        if opcao_final == 1:
            # Reinicia o loop para permitir que o usuário escolha outra opção
            continue
        elif opcao_final == 2:
            # Sai do programa
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Saindo do programa. Até logo!")
            break
