import os
from modelos.funcionario import Funcionario
from modelos.enums.sexo import Sexo
from modelos.enums.setor import Setor

os.system("cls || clear")

funcionarios = Funcionario("678467-89", "Stive", 18, 6709.90, Setor.FINANCEIRO, Sexo.MASCULINO)
print(funcionarios)