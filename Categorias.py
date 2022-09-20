>>> print("hello word")

>>> print 45+17
62
>>> print 45 / 5
9.0

>>> type(62)
int

>>> dir(62)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
 '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__',
 '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__',
 '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__',
 '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
 '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

>>> dir ("novo teste")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
 'translate', 'upper', 'zfill']

>>> help("New Test".upper)
 upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.


>>> help("New Test".upper())
 No Python documentation found for 'NEW TEST'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> a = 10
print (a)

>>> id (42)
11257376

>>> b = 42
>>> id(b)
11257376


#Tipos de variaveis
Int = inteiro = 42
float = ponto flutuante = 3.14
str = string = "texto" 

#Tipagem Dinamica
O pythonm permite que associe um valor a ele sem informar o tipo da variavel

#Tipo de Operadores
+ = Adição
- = Subtração
/ = Divisão
* = Multiplicação
** = Exponenciação
// = retorna a divisão com um número inteiro
% = modulo = retorna o resto de uma divisão
== = Igual
!= = Diferente
> = Maior
< = Menor 
>= = Maior igual
<= = Menor igual

>>> print ("imprimindo")
imprimindo
>>> print ("imprimir","com", "python")
imprimir com python
Sendo
>>> print ("imprimindo","com",5)
imprimindo com 5
onde
a = 10
>>> print ("imprimindo","com",a)
imprimindo com 10

Retornar video 4
>>> import randon

>>> dir randon
 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__',
 '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log',
 '_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate',
 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample',
 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate'] 


>>> random.random()
0.5853960370136738

>>> random.random()
0.07416142512228907

>>> random.random()
0.5618259651089217

>>> random.randint(10, 20)
14

>>> random.randint(10, 20)
17

>>> x = ["gol", "nivus", "saveiro", "taos", "virtus"]
>>> =
>>>random.choice(x)
"nivus"
>>>random.choice(x)
 "gol"
 
>>>random.shuffle(x)
 ["saveiro", "gol", "taos", "virtus", "nivus"]
 
>>>random.shuffle(x)
["virtus", "taos", "gol", "nivus", "saveiro"]

>>> import string
>>>
>>> string.punctuation
'!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'

>>> string.digits
'0123456789'

>>> string.hexdigits
'0123456789abcdefABCDEF'

>>> string.capwords('frase para inicar a letra maiuscula')
'Frase Para Inicar A Letra Maiuscula'

'''Texto'''
'Texto'

'''Texto
mult-linha
para
teste 
em python'''
Texto
mult-linha
para
teste 
em python

"Texto a ser Fatiado"[0:8]
'Texto a '

"Texto a ser Fatiado"[0:11]
'Texto a ser'

"Texto a ser Fatiado"[3:11]
'to a ser'

"Texto a ser Fatiado"[:11]
'Texto a ser'

"Texto a ser Fatiado"[0:]
'Texto a ser Fatiado'

"Texto a ser Fatiado"[3:11:3]
'tae'

"Texto a ser Fatiado negativamente"[3:-6]
'to a ser Fatiado negativ'

"Texto a ser Fatiado negativamente"[::-1]
'etnemavitagen odaitaF res a otxeT'


'PARA VERIFICAR SE A PALAVRA É A MESMA DE FRENTE PARA TRÁS'

Nome = "ana"
Nome == Nome[ ::-1]
True

Nome = "arara"
Nome == Nome[ ::-1]
True

'COMO CONCATENAR E ALTERAR UMA ISTRING'
Nome = 'Marcos'
Nome

Nome = 'Marcos'
Nome ='B' + Nome [1:]
Nome
'Barcos'

'PARA VERIFICAR SE A PRIMEIRA LETRA CORRESPONDE AO DESEJADO'
'CONTINUAÇÃO DO EXEMPLO ONDE'
'Nome = Barcos'
Nome.startswith('B')
True
Nome.startswith('b')
False

'PARA VERIFICAR SE A ÚLTIMA LETRA CORRESPONDE AO DESEJADO'
'CONTINUAÇÃO DO EXEMPLO ONDE'
'Nome = Barcos'
Nome.endswith('s')
True
Nome.endswith('r')
False

'PARA TROCAR A LETRA QUE DESEJA POR OUTRO CARACTERE'
'CONTINUAÇÃO DO EXEMPLO ONDE'
'Nome = Barcos'
Nome.replace('r','8')
'Ba8cos'

>>> IMPORTÂNTE >>> 'A STR NUNCA É ALTERADA'
'A ORIGEM NESTE EXEMPLO CONTINUA 'BARCOS' DEVIDO ALTERAÇÃO ANTERIOR'
'PARA ALTERAR REALMENTE A STR'
Nome = Nome.replace('r','8')
Nome
'Ba8cos'

'Função split tranforma o texto corrido em itens separados'
Texto = 'Testando a função split no python'
s= Texto.split()
s
['Testando', 'a', 'função', 'split', 'no', 'python']

Texto = 'Testando;o;split;no;python'
s= Texto.split(';')
s
['Testando', 'o', 'split', 'no', 'python']

'Fazendo essa transformação para um exemplo de data'
data = ['16','08','1982']
'/'.join(data)
'16/06/1982'

Estrutura de Dados
List
Tuples
Set
dictionary ( Dicionário )

'Estrutura de Dados'
lista =[1,2,3,4,5]
lista
[1, 2, 3, 4, 5]

lista =[1,2,3,4,5]
lista[1]
2

lista =[1,2,3,4,5]
lista
for x in lista: print (x)
1
2
3
4
5

'Estrutura de Dados'
lista =[1,'fernando',3,15,1,4,'true','false']
lista
[1, 'fernando', 3, 15, 1, 4, 'true', 'false']

'Estrutura de Dados'
lista =[1,'Fernando','3,14','1%',4,'true','false']
lista
for x in lista: print (x)
1
Fernando
3,14
1%
4
true
false

lista[1]
Fernando

lista[2] = 'PI'
lista
[1, 'Fernando', 'PI', '1%', 4, 'true', 'false']

lista =[1,'Fernando','3,14','1%',4,'true','false']
lista[2] = 'PI'
lista
[1, 'Fernando', 'PI', '1%', 4, 'true', 'false']

lista.append('Novo item')
lista
[1, 'Fernando', 'PI', '1%', 4, 'true', 'false', 'Novo item', 'Novo item']

lista.pop()
'Novo item'

lista.pop()
lista
[1, 'Fernando', 'PI', '1%', 4, 'true', 'false']

lista.remove('1%')
lista
[1, 'Fernando', 'PI', 4, 'true', 'false']

lista.insert(2,'Item Novo')
lista
[1, 'Fernando', 'Item Novo', 'PI', 4, 'true', 'false']

lista.insert(0,'Inicio')
lista
['Inicio', 1, 'Fernando', 'Item Novo', 'PI', 4, 'true', 'false']

lista.reverse()
lista
['false', 'true', 4, 'PI', 'Item Novo', 'Fernando', 1, 'Inicio']

'a função sort lista com ordem alfabetica e devido o exemplo conter um número inteiro ele não consegue realizar a a descrição'
' tem que ter somente inteiro ou caractere de texto'
'lista exemplo 1,2,3,4,5 ou abc, acb, abg, asw'
lista.sort()
lista
TypeError                                 Traceback (most recent call last)
<ipython-input-33-149e0ec151e4> in <module>()
----> 1 lista.sort()
      2 lista

TypeError: '<' not supported between instances of 'int' and 'str'

listinha =[21,95,23,14,75,61]
listinha
[21, 95, 23, 14, 75, 61]
listinha.sort()
listinha
[14, 21, 23, 61, 75, 95]
listinha.sort(reverse=True)
listinha
[95, 75, 61, 23, 21, 14]

tupla = (1,2,3,4)
tupla
(1, 2, 3, 4)

tupla=(1,2,'Nome','Sobrenome')
tupla 
(1, 2, 'Nome', 'Sobrenome')

s = set ()
s.add(1)
s.add(21)
s.add(32)
s.add(15)
s.add(41)
s.add(29)
s
{1, 15, 21, 29, 32, 41}

s.remove(21)
s
{1, 15, 29, 32, 41}

s.pop()
s
{1, 15, 29, 41}

d= {}
type(d)
dict

d['Nome'] ='Fernando'
d['Sobrenome'] ='Cruz'
d
{'Nome': 'Fernando', 'Sobrenome': 'Cruz'}

d['data de nascimento'] = '16/08/1982'
d['número de telefone'] = '11952349487'
d
{'Nome': 'Fernando',
 'Sobrenome': 'Cruz',
 'data de nascimento': '16/08/1982',
 'número de telefone': '11952349487'}

d.pop('número de telefone')
'11952349487'

d.popitem()
d
{'Nome': 'Fernando', 'Sobrenome': 'Cruz'}

d.values()
dict_values(['Fernando', 'Cruz'])
d.keys()
dict_keys(['Nome', 'Sobrenome'])


>>>BANCO DE DADOS>>>

import sqlite3
conn = sqlite3.connect("galeria.db")
cursor = conn.cursor()
def criar_tabela():
  sql = """
  CREATE TABLE albuns(titulo text, artista text, data_lancamento text, data_publicacao text, midia text)
  """
  cursor.execute(sql)
  conn.commit()

>>>SALVAR O ARQUIVO >>> Banco_de_Dados

def grava_album():
sql: "INSERT INTO albuns VALUES ('Glow', 'Andy Hunter', '24/07/2010','Xplore Records','MP3')"
cursor.execute(sql)
conn.commit()

import Banco_dados
Banco_dados.grava_album()

def grava_muitos():
albuns = [('Exodus', 'Andys Hunter', '08/07/2002', 'Sparrow Records', 'CD'),
('Until We Have', 'red', '01/02/2003', 'Essential Records', 'CD')
cursor.execurmany("INSERT INTO albuns VALUES(?,?,?,?,?), albuns)
>>>O PONTO DE INTERROGAÇÃO TEM QUE TER A MESMA QUANTIDADE DE ELEMENTOS PRESENTES NAS COLUNAS>>>
conn.commit()

import Banco_dados as db
db.grava_muitos

def atualiza():
sql= """
UPDATE albuns  SET artista  = 'John Doe'      
WHERE artista =  'Andy Hunter'
"""
cursor.execute(sql)
conn.commit()

def excluir():
sql= """
DELETE FROM albuns where artista = 'John Doe'
"""
cursor.execute(sql)
conn.commit()

import Banco_dados as db
db.excluir

def listar():
sql="""
SELECT rowid, * FROM albuns ORDER BY artista
"""
cursor.execute(sql)
for row in cursor.fetchall():
print(row) 

import Banco_dados as db
db.listar()


