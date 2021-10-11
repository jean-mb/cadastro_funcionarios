import time                 
import random

# ============ OBJETOS ============
class Equipe:
  def __init__(self):
    self._equipe = []

  @property
  def equipe(self):
    return self._equipe

  def insere_funcionario(self, funcionário):
    self._equipe.append(funcionário)

  def completa(self):
    if len(self._equipe) == 10:
      return True
  
    if len(self._equipe) % 3 == 0:
      for funcionario in self.equipe:
        funcionario.salario = round(funcionario.salario + (funcionario.salario * .05), 2)
 
class Funcionario:
  def __init__(self, nome, salario):
    self._nome     = nome.capitalize()
    self._salario  = salario
  
  @property
  def nome(self):
    return self._nome

  @property
  def salario(self):
    return self._salario

  @salario.setter
  def salario(self, salario):
    self._salario = salario
# ============ CADASTRO ============
print('========================\nCADASTRO DE FUNCIONÁRIOS\n========================')

equipe = Equipe()
while not equipe.completa():
  try: 
    nome_func     = str(input(' - Digite o nome do funcionário --> '))
    salario_func  = float(input(' - Digite o salário do funcionário --> '))
    funcionario = Funcionario(nome_func, salario_func)
    equipe.insere_funcionario(funcionario)
    
    print(f'\nFuncionário cadastrado! ({len(equipe.equipe)}/10)\n')
    time.sleep(1)
  except ValueError:
      print('\n---------------------VALOR INVÁLIDO, DIGITE NOVAMENTE!!---------------------\n')
  

print('==============\nA EQUIPE ALCANÇOU A META DE FUNCIONÁRIOS\n==============')

for funcionario in equipe.equipe:
  print(' - Funcionário: {} | Salário: R${}'.format(funcionario.nome, funcionario.salario))
print('========================================================================')

# ============ SORTEIO AUMENTO DE SALÁRIO ============

funcionario_sorteado  = equipe.equipe[random.randrange(len( equipe.equipe ))]
aumento               =  funcionario_sorteado.salario *.1

funcionario_sorteado.salario =  round(funcionario_sorteado.salario + aumento, 2)

print ('O funcionário sorteado foi: {}'.format(funcionario_sorteado.nome))
print ('O salário de {} agora é R${}'.format(funcionario_sorteado.nome, funcionario_sorteado.salario))

