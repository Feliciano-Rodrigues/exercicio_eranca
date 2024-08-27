# main.py
from mamifero import Mamifero
from ave import Ave
from reptil import Reptil

def main():
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

if __name__ == "__main__":
    main()
