class Pessoa(object):

    def __init__(self, nome: str, idade: int, cpf: int):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def Falar(self, texto: int) -> None:
        self.texto = texto
        print(texto)
        
    def __str__(self) -> str:
        return f'O {self.nome} tem {self.idade} de idade e o numero do seu cpf é {self.cpf}'

alex = Pessoa(nome='Alex Martins', idade=33, cpf=123)

print(alex)