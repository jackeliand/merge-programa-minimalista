#-*- coding: utf8 -*-

import sys
reload(sys)
sys.setdefaultencoding("UTF-8")
# lo anterior es para que soporte los acentos
# y signos propios del español como "¿"
import itertools

# Esta función toma la "list of list of
# lists" y la "aplana" en una lista simple
# la cual se usará como oración base.

def flatten(*args):
    for x in args:
        if hasattr(x, '__iter__'):
            for y in flatten(*x):
                yield y
        else:
            yield x

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
#SV =merge("&V", "&ad")
N = merge("&N", "&A")
D = merge("&d",N)
V = merge("&V", D)
v = merge(D, V)
T = merge("$T", v)
F = merge("$F", T)
C = merge("$C", F)

print C #Muestra la oración base 
sentence = list(flatten(C))
#"Aplana" la estructura base
print sentence
sentence2 = sentence

# Invocamos el lexicón
from lex import *
from lex import X
########
# A continuación, ubicamos cada uno de los items
# léxicos en dónde deben de ir, "mapeando" la
# estructura generada por Merge


if Numero == "S":
    whConc = "Quién"
else:
    whConc = "Quiénes"    

from lex import Adjetivo
 
print "La oración base es: "
print C
print "-------"

#Simulemos la función Copy hacia la fase de Comp
sentence = [w.replace('$F', '&d &N &Aj', 1) for w in sentence]
sentence = [w.replace('&V', '', 1) for w in sentence]
sentence = [w.replace('$T', '&V &ad', 1) for w in sentence]
for x in range(3):
    sentence.pop()
sentence = [w.replace('&Aj', X(Adjetivo), 1) for w in sentence]
sentence = [w.replace('&N', X(Sustantivo), 1) for w in sentence]
sentence = [w.replace('&d', X(Determinante), 1) for w in sentence]
sentence = [w.replace('&A', (X(Intensif)+' '+X(Adjetivo)) , 1) for w in sentence]
sentence = [w.replace('&V', X(VerboTR), 1) for w in sentence]
sentence = [w.replace('&ad', X(Adverbio), 1) for w in sentence]

oracion = list(flatten(sentence))
ag = sentence[1]
secondterm = oracion[3:6]
o = ' '.join(oracion)
obj = ' '.join(secondterm)

print "---------"
print ">>> " + o

print "-----"
pregunta = list(flatten(oracion))
pregunta = [w.replace('$C', whConc, 1) for w in pregunta]
pregunta.insert(1, pregunta[2])
for x in range(2):
	pregunta.pop(2)
pregunta = ' '.join(pregunta)
print ">>> ¿" + pregunta + "?"
print ">>> " + ag

print "-----"
pregunta = list(flatten(sentence))
pregunta = [w.replace('$C', "Qué", 1) for w in pregunta]
pregunta.insert(1, pregunta[2])
for x in range(5):
    pregunta.pop()
pregunta = ' '.join(pregunta)
print ">>> ¿" + pregunta + "?"
print ">>> " + obj
print "-----"

repor = list(flatten(oracion))
repor = [w.replace('$C', "Dicen que", 1) for w in repor]
repor.insert(1, repor[2])
del repor[3]
repor.insert(3,'a')
repor = list(flatten(repor))
reportativo = ' '.join(repor)
print ">>> ¡" + reportativo + "!"
print "-----"

intr = list(flatten(oracion))
intr[2] = X(VerboINtr)
for x in range(4):
    intr.pop()
intr = list(flatten(intr))
intr = ' '.join(intr)
print ">>> " + intr
print "\n"



print "+++++++"

whConc = "Quién"
sentence = sentence2
print sentence
sentence = [w.replace('$F', '&N', 1) for w in sentence]
for x in range(3):
    sentence.pop()
sentence = [w.replace('&N', X(Propio), 1) for w in sentence]
sentence = [w.replace('&d', '', 1) for w in sentence]
sentence = [w.replace('$T', X(VtransSing), 1) for w in sentence]
sentence = list(flatten(sentence))
sentence =sentence[0:5]
ag = sentence[1]
secondterm = sentence[3:5]
oracion = ' '.join(sentence)
obj = ' '.join(secondterm)
print "---------"
print ">>> " + oracion
print "-----"
pregunta = list(flatten(sentence))
pregunta = [w.replace('$C', whConc, 1) for w in pregunta]
pregunta.insert(1, pregunta[2])
for x in range(2):
    pregunta.pop(2)
pregunta = ' '.join(pregunta)
print ">>> ¿" + pregunta + "?"
print ">>> " + ag
print "-----"
pregunta = list(flatten(sentence))
pregunta = [w.replace('$C', "A quién", 1) for w in pregunta]
pregunta.insert(1, pregunta[2])
for x in range(3):
    pregunta.pop()
pregunta = ' '.join(pregunta)
print ">>> ¿" + pregunta + "?"
print ">>> A " + obj
print "-----"
repor = list(flatten(sentence))
repor = [w.replace('$C', "Dicen que", 1) for w in repor]
repor.insert(1, repor[2])
del repor[3]
repor.insert(3,'a')
repor = list(flatten(repor))
reportativo = ' '.join(repor)
print ">>> ¡" + reportativo + "!"
print "-----"

cop = list(flatten(sentence2))
cop = [w.replace('$F', X(Propio), 1) for w in cop]
cop = [w.replace('$T', X(VCopulativoS), 1) for w in cop]
for x in range(4):
    cop.pop()
cop = [w.replace('&N', X(S_FS), 1) for w in cop]
cop = [w.replace('&d', X(Det_FS), 1) for w in cop]
cop = [w.replace('&A', X(Adj_FS), 1) for w in cop]
cop = list(flatten(cop))
cop = ' '.join(cop)
print ">>> " + cop
print "\n"
