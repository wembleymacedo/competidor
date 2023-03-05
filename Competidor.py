#----------------------------------------------------------------------------------------------------------------Modulos
import datetime
hoje = datetime.date.today()
import csv
#----------------------------------------------------------------------------------------------------------------classes
class Pessoa():
    def __init__(self, nome, idade, peso, altura, sexo, meta_peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.meta_peso = meta_peso
    def imc_pessoa(self):
        imc = (self.peso/self.altura)/2
        status = ""
        if imc < 18.5:
            status = "ABAIXO DO PESO"
        if imc >= 18.5 <= 24.9:
            status = "PESO NORMAL"
        if imc >= 25.0 <= 29.9:
            status = "EXCESSO DE  PESO"
        if imc >= 30.0 <= 34.9:
            status = "OBESIDADE CLASSE 1"
        if imc >= 35.0 >= 39.0:
            status = "OBESIDADE CLASSE 2"
        if imc > 40:
            status = "OBESIDADE CLASSE 3"
            return imc, status

    def peso_ideal(self):
            imc = self.imc_pessoa()
            p = self.altura * self.altura
            pi = imc * p
            return pi

def novas_medidas():
    class Captador_medidas():
        def __init__(self, bicepes_d, bicepes_e, perna_d, perna_e, abdomen):
            self.bicepes_d = bicepes_d
            self.bicepes_e = bicepes_e
            self.perna_d = perna_d
            self.perna_e = perna_e
            self.abdomen = abdomen

        def salva_dados_medidas(self):

            with open(f"{hoje}.csv",  "w") as Medidas:
                cabecalho = ["Bicepes Direito", "Bicepes Esquerdo", "Perna Direita", "Perna Esquerda ","Abdomen"]
                escrever = csv.DictWriter(Medidas, cabecalho)
                escrever.writeheader()
                lista_nome_arquivos_medidas.append(hoje)
                escrever.writerow({"Bicepes Esquerdo": self.bicepes_e,
                                   "Bicepes Direito": self.bicepes_d,
                                   "Perna Esquerda": self.perna_d,
                                   "Perna Direita": self.perna_e,
                                   "Abdomen": self.abdomen})



#___________________________________________________________________________________________________________________POO

#--------------------------------------------------------------------------------------------------------------Colecoes
lista_nome_arquivos_medidas = []





#--------------------------------------------------------------------------------------------------------------Funcoes
def parametros_medidas(b_d,b_e,p_d,p_e,abd):
    b_d = float(input("Medida Braco direito:"))
    b_e = float(input("Medida Braco esquerdo:"))
    p_d = float(input("Medida Perna direira"))
    p_e = float(input("Mediada Pena esquerda"))
    abd = float(input("Medida Abdomen:"))
    return  b_d,b_e,p_d,p_e,abd



def usuario(nome, idade, peso, altura, sexo,meta):
    nome = str(input("Nome:"))
    idade = int(input("Idade:"))
    peso = float(input("Peso:"))
    altura = float(input("Altura:"))
    meta = float(input("Qual meta de peso voce deseja chegar:"))
    print("A qual genero voce pertence:")
    sexo = int(input("[0] Homem      [1] Mulher:"))

    return nome, idade, peso, altura, sexo, meta


def menu ():
    while True:
        print(25*"=", "MENU", "="*25)
        print("""
            [1] Atualizar medidadas
            [2] Relatar pontuacao
            [3] Ranking
        
         """)

        choice = int(input(" => :"))
        return choice






escolha = 0
while escolha == 0:
    escolha = menu()

#-------------------------------------------------------------------------------------------- Botao  1
    while escolha == 1 :
        print(25*"=", "ATUALIZAR MEDIDAS")
        print("""
        [1] Atualizar Medidas de todos os competidores 
        [2] Atualizar  do competidor individual 
        [0] Voltar
        """)
        choice_atulizar = int(input(" => :"))
        if choice_atulizar == 1:
            print(25*"=", "ATULIZA MEDIDA DE TODOS COMPETIDORES:", "="*25)
            """
            * - abrir funcao que capta  dados 
            * - salvar dados atulizado 
             """
            novas_medidas()




        if choice_atulizar == 2:
                """
                       * - Mostrar  qual usuario eu desjo altualizar medidada
                       * - acessar lista com os nomes dos arquvo do usario escolhido
                       * - abrir a ultima medida e subescrevela
                       * - abrir funcao que capta  dados 
                       * - salvar dados atulizado 
                       """
        if choice_atulizar == 3:
            print(25 * "=", "ATULIZAR COMPETIDOR:", "=" * 25)
            """
            * - printar os competidores que tenho disponivel para atualizar 
            * - acessar lista com o nome do arquivosque contem os  dados do usario escolhido
            * - subescrever informacoes e salvar 

            """

        if choice_atulizar == 0:
            escolha = 0

#______________________________________________________________________________________ Botao2
    while escolha == 2:
        print(25 * "=", "ATULIZAR COMPETIDOR:", "=" * 25)
        """
        * - abrir lista com o nome da ultima atulizacao que teve 
        * - Abrir funcao que capt criterios a de pontuacao
        * - salvar no 
        
        """
#_______________________________________________________________________________________Botao3
    while escolha == 3 :
        print(25 * "=", " Ranking", "=" * 25)
        """
        * - juntar todos os arquivos diarios de  cada competior 
        * - criar um novo arquivo com a colocacao de cada competidor 
        """