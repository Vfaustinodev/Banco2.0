class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self, nome):
        return self.nome
    
p1 = Pessoa('virginio', 'vinte e três')
print(p1.nome, p1.idade)