#-*- coding: utf8 -*-
import itertools
def flatten(*args):
    for x in args:
        if hasattr(x, '__iter__'):
            for y in flatten(*x):
                yield y
        else:
            yield x
# "flatten" toma la "list of list of
# lists" y la "aplana" en una lista simple
# la cual se usará como oración base.

########### LA FUNCIÓN MERGE ######
def merge (x,y):
	R =[]
	R.append(x)
	R.append(y)
	fusion = R
	return fusion

#### fin de la FUNCIÓN MERGE ######


# A manera de SConc, se le dice a 
# Merge qué unir con qué cosa
D = merge("&d","&N")
V = merge("&V",D)
v = merge(D, V)
T = merge("T", v)
F = merge("F", T)
C = merge("C", F)

print C #Muestra la oración base 
sentence = list(flatten(C))
#"Aplana" la estructura base
print sentence

# Invocamos el lexicón
from lex import *

########
# A continuación, ubicamos cada uno de los items
# léxicos en dónde deben de ir, "mapeando" la
# estructura generada por Merge  

print "La oración base es: "
print C
sentence = [w.replace('F', '&d &N', 1) for w in sentence]
for x in range(3):
    sentence.pop()
sentence = [w.replace('&N', X(Sustantivo), 1) for w in sentence]
sentence = [w.replace('&d', X(Determinante), 1) for w in sentence]
sentence = [w.replace('T', X(VerboTR), 1) for w in sentence]
sentence = list(flatten(sentence))
print sentence
ag = sentence[1]
secondterm = sentence[3:5]
oracion = ' '.join(sentence)
obj = ' '.join(secondterm)
print "---------"
print ">>> " + oracion