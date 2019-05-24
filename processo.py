from recurso import Recurso


class Processo(object):
  def __init__(self):
    self.__titulo = ''
    self.__recursosAlocados = []
    self.__recursosMaximos = []
    self.__recursosNecessarios = []

  def init(self, tituloDosRecursos):
    print('\n\t\t=-=-=-=-=-=-=-=-=-=', end='')
    self.__titulo = input('\n\t\tTitulo do processo\n\t\t> ')
    print('\n\t\t=-=-=-=-=-=-=-=-=-=', end='')
    print('\n\n\t\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=', end='')
    for titulo in tituloDosRecursos:
      self.__recursosMaximos.append(Recurso())
      self.__recursosMaximos[-1].init(titulo, f'necessario para o processo {self.__titulo}')
    print('\n\t\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=', end='')
    print('\n\n\t\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=', end='')
    for titulo in tituloDosRecursos:
      self.__recursosAlocados.append(Recurso())
      self.__recursosAlocados[-1].init(titulo, f'alocado para o processo {self.__titulo}')
    print('\n\t\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n\n')
    for index in range(len(tituloDosRecursos)):
      self.__recursosNecessarios.append(Recurso())
      quantidade = self.__recursosMaximos[index].obterQuantidade()
      quantidade -= self.__recursosAlocados[index].obterQuantidade()
      self.__recursosNecessarios[index].init(tituloDosRecursos[index], quantidade=quantidade)

  def obterRecursos(self, tipoDeRecurso):
    if tipoDeRecurso == 'Alocados':
      return self.__recursosAlocados
    elif tipoDeRecurso == 'Maximos':
      return self.__recursosMaximos
    else:
      return self.__recursosNecessarios

  def obterTitulo(self):
    return self.__titulo
