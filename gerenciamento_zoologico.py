# Classe base Animal
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print("O animal está fazendo um som.")

    def movimentar(self):
        print("O animal está se movimentando.")

# Subclasse Mamífero
class Mamifero(Animal):
    def __init__(self, nome, idade, tem_pelo):
        super().__init__(nome, idade)
        self.tem_pelo = tem_pelo

    def fazer_som(self):
        print("O mamífero está rugindo.")

    def movimentar(self):
        print("O mamífero está se movimentando.")

# Subclasse Ave
class Ave(Animal):
    def __init__(self, nome, idade, pode_voar):
        super().__init__(nome, idade)
        self.pode_voar = pode_voar

    def fazer_som(self):
        print("A ave está cantando.")

    def movimentar(self):
        if self.pode_voar:
            print("A ave está voando.")
        else:
            print("A ave está andando.")

# Subclasse Réptil
class Reptil(Animal):
    def __init__(self, nome, idade, tipo_de_pele):
        super().__init__(nome, idade)
        self.tipo_de_pele = tipo_de_pele

    def fazer_som(self):
        print("O réptil está sibilando.")

    def movimentar(self):
        print("O réptil está rastejando.")

# Exemplos de uso
# Criando instâncias de cada tipo de animal
leao = Mamifero("Leão", 5, True)
aguia = Ave("Águia", 3, True)
cobra = Reptil("Cobra", 2, "escamas")

# Usando métodos
leao.fazer_som()        # Saída: O mamífero está rugindo.
leao.movimentar()       # Saída: O mamífero está se movimentando.

aguia.fazer_som()       # Saída: A ave está cantando.
aguia.movimentar()      # Saída: A ave está voando.

cobra.fazer_som()       # Saída: O réptil está sibilando.
cobra.movimentar()      # Saída: O réptil está rastejando.
