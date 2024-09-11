from modelos.enums.setor import Setor
from modelos.enums.sexo import Sexo

class Funcionario:
    def __init__(self, id: str, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return f"Id: {self.id} \nNome: {self.nome} \nIdade: {self.idade} \nSalário: R${self.salario} \nSetor: {self.setor.value} \nSexo: {self.sexo.value}"
        