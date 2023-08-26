# Tipos de Interpolação de Strings:

## Existem 3 modos de interpolação que funcionam no na versão 3+ do python:


 Usando `.format()` 

 Usando o método da classe string .format(), exemplos:


Utilizar parâmetros posicionais, mas utilizá-los em ordem sorteada;
```python
>>> '{1}, {0}'.format('john', 'doe')
>>> doe, john
```

Definir espaçamento na string substituindo o caractere a ser exibido: no estilo antigo, sempre é exibido um espaço em branco;

```python
>>> '{:_<10}'.format('john')
>>>    john______
```
Centralizar o conteúdo com referência ao espaço disponível;

```python
>>> '{:+^10}'.format('john')
>>> +++john+++
```

Ao utilizar números sinalizados, é possível controlar a posição do sinal;

```python
    >>> '{:=5d}'.format(-3)
    -   3
    >>> '{:=+5d}'.format(3)
    +   3
```

O método format aceita parâmetros nomeados para definir os valores, não dependendo mais de dicionários ou tuplas;

```python
    >>> '{first} {last}'.format(first='john', last='doe')
    john doe

    O que permite utilizar tuple deconstructing ou dict deconstructing:

    >>> name = ('john', 'doe')
    >>> '{0} {1}'.format(*name)
    john doe

    >>> name = {'first': 'john', 'last': 'doe'}
    >>> '{first} {last}'.format(**name)
    john doe
```

É possível acessar valores diretamente da string;

```python
>>> john = {'first': 'john', 'last': 'doe'}
>>> '{name[first]} {name[last]}'.format(name=john)
>>> john doe
```
   
De igual forma, é possível acessar atributos do objeto:

```python
>>> 'Nome do arquivo: {0.name}'.format(open('arquivo.txt'))
>>> Nome do arquivo: arquivo.txt
```

É possível que objetos assumam o controle de sua própria formatação, assim como acontece com o objeto datetime.datetime;

```python

 >>> from datetime import datetime
    >>> '{:%Y-%m-%d %H:%M}'.format(datetime.now())
    2017-12-11 20:52
```
Isso é possível pois o método format buscará pelo método __format__ do objeto;

É possível parametrizar o próprio formato com seus valores;

```python
    >>> '{:_{align}{width}}'.format('john', align='^', width='10')
    ___john___
    >>> '{:_{align}{width}}'.format('john', align='>', width='10')
    ______john
```



  ### -  f-strings (PEP 498)

 

