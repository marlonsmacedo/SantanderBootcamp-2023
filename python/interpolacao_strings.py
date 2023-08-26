''' Tipos de Interpolação de Strings:

Existem 3 modos de interpolação que funcionam no na versão 3+ do python:

 - Usando o método da classe string .format()
   Exemplo:
      

    Utilizar parâmetros posicionais, mas utilizá-los em ordem sorteada;

    >>> '{1}, {0}'.format('john', 'doe')
    doe, john

    Definir espaçamento na string substituindo o caractere a ser exibido: no estilo antigo, sempre é exibido um espaço em branco;

    >>> '{:_<10}'.format('john')
    john______

    Centralizar o conteúdo com referência ao espaço disponível;

    >>> '{:_^10}'.format('john')
    +++john+++

    Ao utilizar números sinalizados, é possível controlar a posição do sinal;

    >>> '{:=5d}'.format(-3)
    -   3
    >>> '{:=+5d}'.format(3)
    +   3

    O método format aceita parâmetros nomeados para definir os valores, não dependendo mais de dicionários ou tuplas;

    >>> '{first} {last}'.format(first='john', last='doe')
    john doe

    O que permite utilizar tuple deconstructing ou dict deconstructing:

    >>> name = ('john', 'doe')
    >>> '{0} {1}'.format(*name)
    john doe

    >>> name = {'first': 'john', 'last': 'doe'}
    >>> '{first} {last}'.format(**name)
    john doe

    É possível acessar valores diretamente da string;

    >>> john = {'first': 'john', 'last': 'doe'}
    >>> '{name[first]} {name[last]}'.format(name=john)
    john doe

    De igual forma, é possível acessar atributos do objeto;

    >>> 'Nome do arquivo: {0.name}'.format(open('arquivo.txt'))
    Nome do arquivo: arquivo.txt

    É possível que objetos assumam o controle de sua própria formatação, assim como acontece com o objeto datetime.datetime;

    >>> from datetime import datetime
    >>> '{:%Y-%m-%d %H:%M}'.format(datetime.now())
    2017-12-11 20:52

    Isso é possível pois o método format buscará pelo método __format__ do objeto;

    É possível parametrizar o próprio formato com seus valores;

    >>> '{:_{align}{width}}'.format('john', align='^', width='10')
    ___john___
    >>> '{:_{align}{width}}'.format('john', align='>', width='10')
    ______john


 -  f-strings (PEP 498)

 -- Interpolação com 


Exemplo:


Existem 3 f
'''