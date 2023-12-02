class heroi:
    def __init__(self, nome, idade, tipo):
      self.nome = nome
      self.idade = idade
      self.tipo = tipo

    
    def atacar(self):
        if self.tipo  ==  'mago':
            ataque = 'magia'
        elif self.tipo == 'guerreiro':
            ataque = 'espada'
        elif self.tipo == 'monge':
            ataque = 'artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'shiriken'
    
        mensagem = (f'O {self.tipo} {self.nome} atacou usando {ataque}')
        print(mensagem)

heroi1 = heroi('Fulano', 30, 'mago')
heroi2 = heroi('Ciclano', 28, 'guerreiro')
heroi3 = heroi('Beltrano', 25, 'monge')
heroi4 = heroi('Goku', 20, 'ninja')

heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()