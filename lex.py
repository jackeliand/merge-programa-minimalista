# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('UTF8')

import nltk
import spaghetti as spa
from nltk.corpus import stopwords
import re
import time
import random
import csv


global S_MS
S_MS = []
global S_MP
S_MP = []
global S_FS
S_FS = []
global S_FP
S_FP = []

global Pr
Pr = []

global Adj_MS
Adj_MS = []
global Adj_MP
Adj_MP = []
global Adj_FS
Adj_FS = []
global Adj_FP
Adj_FP = []

global Det_MS
Det_MS = []
global Det_MP
Det_MP = []
global Det_FS
Det_FS = []
global Det_FP
Det_FP = []

global Adv
Adv = []

NomPropio1 = []
NomPropio2 = []
VtransSing = []
VtransPl =[]
VintrSing = []
VintrPl = []
Intensif = ["muy", "poco", "bastante", "demasiado", "algo"]
VCopulativoS = ["es", "fue"]
VCopulativoP = [u"son", u"fueron"]

f = open('lexicon2.csv')
csv_f = csv.reader(f)

for row in csv_f:
    NomPropio1.append(row[0])
    NomPropio2.append(row[1])
    VtransPl.append(row[2])
    VtransSing.append(row[3])
    VintrSing.append(row[4])
    VintrPl.append(row[5])


class lexico:

    def twitter(busq, Ck, Cs, Ot, Ots):
        import twitter
        import json
        print """
        L E X I C O
        """
        print "Estableciendo comunicacion con Twitter..."
        CONSUMER_KEY = Ck
        CONSUMER_SECRET = Cs
        OAUTH_TOKEN = Ot
        OAUTH_TOKEN_SECRET = Ots

        auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                                   CONSUMER_KEY, CONSUMER_SECRET)

        twitter_api = twitter.Twitter(auth=auth)
        print "Conexion establecida: "
        print twitter_api
        print "Hoy es: "
        print time.strftime("%c")
        print "******"

        q = busq
        count = 20
        lang = 'es'
        locale = 'mx'

        search_results = twitter_api.search.tweets(q=q, count=count, lang=lang, locale=locale)

        statuses = search_results['statuses']

        print "Buscando..."
        for _ in range(5):
            print "Twits capturados:", len(statuses)
            try:
                next_results = search_results['search_metadata']['next_results']
            except KeyError, e:
                break

            kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])

            search_results = twitter_api.search.tweets(**kwargs)
            statuses += search_results['statuses']



        resultados = [ status['text']
                         for status in statuses ]

        text = ''.join(resultados)
        p = re.compile(r'@([\w.-]+.)|#([\w.-]+.)|(https:\W\Wt\Wco\W)\w{10}|RT')
        tw = p.sub( '', text)
        usoTwitter = 1
        return tw



    def limpiezaNone(entrada):
        lista =[]
        for x in entrada:
            if x[1] == None:
                pass
            else:
                lista.append(x)
        return lista


    def match(item, palabro):
        item = str(item)
        matchN = re.search(r'^nc', item)
        matchP = re.search(r'^s', item)
        matchAdj = re.search(r'^a', item)
        matchDet = re.search(r'^d', item)
        matchAdv = re.search(r'^r', item)

        if matchN:
            if item[2:4] == 'ms':
                S_MS.append(palabro)
            elif item[2:4] == 'mp':
                S_MP.append(palabro)
            elif item[2:4] == 'fs':
                S_FS.append(palabro)
            elif item[2:4] == 'fp':
                S_FP.append(palabro)
            else:
                pass
        elif matchP:
            Pr.append(palabro)
        elif matchAdj:
            if item[3:5] == 'ms':
                Adj_MS.append(palabro)
            elif item[3:5] == 'mp':
                Adj_MP.append(palabro)
            elif item[3:5] == 'fs':
                Adj_FS.append(palabro)
            elif item[3:5] == 'fp':
                Adj_FP.append(palabro)
            else:
                pass
        elif matchDet:
            if item[3:5] == 'ms':
                Det_MS.append(palabro)
            elif item[3:5] == 'mp':
                Det_MP.append(palabro)
            elif item[3:5] == 'fs':
                Det_FS.append(palabro)
            elif item[3:5] == 'fp':
                Det_FP.append(palabro)
            else:
                pass
        elif matchAdv:
            if item[1] == "n":
                pass
            else:
                Adv.append(palabro)
        else:
            return 0

# Aquí es necesario incluir tu propia clave API
    args = ('xxx', 'xxx', \
    'xxx', 'xxx')
    corpus = twitter("no", *args)
    tagging = spa.pos_tag(corpus.split())
    palabras = limpiezaNone(tagging)
    print "---------"
    for x in palabras:
        match(x[1], x[0])



def X(lis):
    longitud = len(lis)
    if longitud == 1:
        itemLex = lis[0]
    elif longitud == 0:
        itemLex = "______"
    else:
        itemLex = lis[random.randint(0, longitud - 1)]
    return itemLex


Genero = random.choice('MF')
Numero = random.choice('SP')
PREP = list(set(Pr))
if Numero == "S":
    if Genero == "M":
        Determinante = Det_MS
        Cuantif = [u"medio", u"solo un", u"tambien el"]
        Propio = NomPropio1 + NomPropio2
        Sustantivo = S_MS
        Adjetivo = Adj_MS
        Preposicion = PREP
        VerboTR = VtransSing
        VerboINtr = VintrSing
        VCopulativo = ["es", "fue"]
        Adverbio = Adv
    if Genero == "F":
        Determinante = Det_FS
        Cuantif = [u"media", u"solo una", u"tambien la"]
        Propio = NomPropio1 + NomPropio2
        Sustantivo = S_FS
        Adjetivo = Adj_FS
        Preposicion = PREP
        VerboTR = VtransSing
        VerboINtr = VintrSing
        Adverbio = Adv
elif Numero == "P":
    if Genero == "M":
        Determinante = Det_MP
        Cuantif = [u"dos", u"tres", u"muchos", u"pocos"]
        Propio = NomPropio1 + NomPropio2
        Sustantivo = S_MP
        Adjetivo = Adj_MP
        Preposicion = PREP
        VerboTR = VtransPl
        VerboINtr = VintrPl
        VCopulativo = [u"son", u"fueron"]
        Adverbio = Adv
    if Genero == "F":
        Determinante = Det_FP
        Cuantif = [u"dos", u"tres", u"muchas", u"pocas"]
        Propio = NomPropio1 + NomPropio2
        Sustantivo = S_FP
        Adjetivo = Adj_FP
        Preposicion = PREP
        VerboTR = VtransPl
        VerboINtr = VintrPl
        Adverbio = Adv
