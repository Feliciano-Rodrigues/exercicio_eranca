# exercicio_eranca
 utilizando o conceito de herança em Python

 Exercício

Você foi contratado para desenvolver um sistema simples para gerenciamento de um zoológico. Neste zoológico, existem diferentes tipos de animais, e você precisa implementar um sistema que capture as características comuns e específicas de cada tipo de animal, utilizando o conceito de herança em Python. 

Instruções:
Crie uma classe base chamada Animal que possui os seguintes atributos e métodos:
Atributos:
nome: O nome do animal.
idade: A idade do animal.
Métodos:
fazer_som(): Um método que imprime uma mensagem padrão, como "O animal está fazendo um som.".
movimentar(): Um método que imprime uma mensagem padrão, como "O animal está se movimentando.".
Crie três subclasses de Animal que representem tipos específicos de animais, como Mamífero, Ave e Réptil. Cada subclasse deve herdar de Animal e ter características adicionais:
Mamífero:
Atributo adicional: tem_pelo: Indica se o mamífero tem pelo ou não.
Sobrescreva o método fazer_som() para imprimir um som específico, como "O mamífero está rugindo.".
Ave:
Atributo adicional: pode_voar: Indica se a ave pode voar ou não.
Sobrescreva o método movimentar() para indicar que a ave está voando, caso possa voar, ou andando, caso contrário.
Reptil:
Atributo adicional: tipo_de_pele: Descreve o tipo de pele do réptil (por exemplo, "escamas").
Sobrescreva o método movimentar() para indicar que o réptil está rastejando.

