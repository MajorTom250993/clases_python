# Comentario 

strings = 'Este es un string'
strings2 "Este es otro string"
string3= """
  Esete es un string 
  multilinea
"""

floas = 1.124323
integrers = 1

tuplas = ("foo",)

lists = ["foo"]

dictionaries = {
  'foo': 'un tring',
  'foo2': 0,
  'foo3': r'^foo$'
}

tuplas[0]
lists[0]
dictionaries['foo']

# Iteraciones 

for item in tuplas:
  print(item)

# Funciones 
def my_function():
  print("I'm alive")

# Funciones con parámetros
def foo(x, y, *args):
  print("%s - %s" % (x, y))
  print(args[0])
  print(kwargs['foo'])
  
foo (3, 2, 1,2,3 foo="foo")
