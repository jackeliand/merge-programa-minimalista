# -*- coding: utf8 -*-

import nltk
from nltk import CFG
from nltk.parse.generate import generate
from lex import * 
from lex import X 
# "lex" para simular un lexicon y "X" es una
# funcion que permite tomar tokens léxicos al azar
import codecs

import sys
reload(sys)
sys.setdefaultencoding('UTF8')


# Gramática generativa de reglas de reescritura

grammar = CFG.fromstring('''
O -> SN SV
SN -> Det N | Det N SA | Det N SP | Det N SA SP | '''+
'''Q N | Q N SA | Q N SP | Q N SA SP | Spropio
SA -> Adj | Int Adj
SP -> P SN
SV -> Vintr | Vintr SAdv | Vtrans SN | Vtrans SN SAdv | Vcop SN | Vcop SA
SAdv -> Adv | Int Adv
'''
"Det -> '" + X(Determinante) + "' | '" + X(Determinante) +
 "' | '" + X(Determinante) + "'\n"
"Q -> '" + X(Cuantif) + "' | '" + X(Cuantif) + "' | '" + X(Cuantif) + "'\n"
"Spropio -> '" + X(Propio) + "' | '" + X(Propio) + "' | '" + X(Propio) +"'\n"
"N -> '" + X(Sustantivo) + "' | '" + X(Sustantivo) + "' | '" +
 X(Sustantivo) + "' | '" + X(Sustantivo) + "' | '" + X(Sustantivo) + "'\n"
"Adj -> '" + X(Adjetivo) + "' | '" + X(Adjetivo) + "' | '" + X(Adjetivo) +
 "' | '" + X(Adjetivo) + "' | '" + X(Adjetivo) + "'\n"
"P -> '" + X(Preposicion) + "' | '" +
 X(Preposicion) + "' | '" + X(Preposicion) + "'\n"
"Int -> '" + X(Intensif) + "' | '" + X(Intensif) + "'\n"
"Vtrans -> '" + X(VerboTR) + "' | '" + X(VerboTR) + "' | '" +
 X(VerboTR) + "' | '" + X(VerboTR) + "' | '" + X(VerboTR) + "'\n"
"Vintr -> '" + X(VerboINtr) + "' | '" + X(VerboINtr) +
 "' | '" + X(VerboINtr) + "' | '" + X(VerboINtr) +
 "' | '" + X(VerboINtr) + "'\n"
"Vcop -> '" + X(VCopulativo) + "' | '" + X(VCopulativo) + "'\n"
"Adv -> '" + X(Adverbio) + "' | '" + X(Adverbio) + "'\n"
)

# Fin de gramática generativa

print grammar #Muestra la gramática con los items léxicos elegidos


# Si sólo se quiere ver el funcionamiento desde
# la consola, hay que usar:
#
for sentence in generate(grammar, depth=5, n=300):
    print(' '.join(sentence))
#
# lo cual solo generará 200 líneas (cambiar el valor
# de "n" para más. Después de eso
# eliminar el resto:


##########
# Esto genera un archivo de texto de más de
# 600000 oraciones (35mb aprox). Hay que tener
# paciencia en lo que termina el proceso.
'''
f = codecs.open('test.txt', mode='w', encoding='UTF8')

f.write(str(grammar))

for sentence in generate(grammar, depth=5):
    f.write(' '.join(sentence))
    f.write("\n")
     
f.close()

####'''
