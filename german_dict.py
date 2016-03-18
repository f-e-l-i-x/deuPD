# Reads german.dic into a dictionary with upperplaceholder

import re
import nltk
import io

f=io.open('german.dic',mode='r',encoding='iso8859_15')
raw=f.read()
tokens=nltk.word_tokenize(raw)

# deutschSet=set(tokens)

# def prefixfinder(word): #for stress finding
#     prefixDict={}
#     if word in deutschSet:
#         return False
#     if word[:2]=='ge':
#         prefixDict['ge']=2
#         return prefixDict
#     elif word[:2]=='be':
#         prefixDict['be']=2
#         return prefixDict
#     elif word[:3]=='ver':
#         prefixDict['ver']=3
#         return prefixDict
#     elif word[:3]=='zer':
#         prefixDict['zer']=3
#         return prefixDict
#     elif word[:2]=='er':
#         prefixDict['er']=2
#         return prefixDict
#     elif word[:3]=='ent':
#         prefixDict['ent']=3
#         return prefixDict


class orthcount:
    def __init__(self,phone,lettercount):
        self.p=phone
        self.c=lettercount
    def __str__(self):
        return str(self.p)+', '+str(self.c)

def aphone(word):
    if len(word)<2:
        return orthcount(u'A ',1)
    elif len(word)==2:
        if word==u'au':
            return orthcount(u'AW ',2)
        elif word==u'ai':
            return orthcount(u'AY ',2)
        else:
            return orthcount(u'A ',1)
    else:
        if word[0:2]==u'au':
            return orthcount(u'AW ',2)
        elif word[0:2]==u'ai':
            return orthcount(u'AY ',2)
        else:
            return orthcount(u'A ',1)
def ephone(word):
    if len(word)<2:
        return orthcount(u'EH ',1)
    elif len(word)==2:
        if word==u'ei':
            return orthcount(u'EY ',2)
        elif word==u'ey':
            return orthcount(u'EY ',2)
        elif word==u'eu':
            return orthcount(u'OY ',2)
        else:
            return orthcount(u'EH ',1)
    else:
        if word[0:2]==u'ei':
            return orthcount(u'EY ',2)
        elif word[0:2]==u'ey':
            return orthcount(u'EY ',2)
        elif word[0:2]==u'eu':
            return orthcount(u'OY ',2)
        else:
            return orthcount(u'EH ',1)
def iphone(word):
    return orthcount(u'IH ',1)
def ophone(word):
    return orthcount(u'AO ',1)
def uphone(word):
    return orthcount(u'UH ',1)
def yphone(word):
    return orthcount(u'YO ',1)
def umaphone(word):
    if len(word)<2:
        return orthcount(u'EH ',1)
    elif len(word)==2:
        if word==u'\xe4u':
            return orthcount(u'OY ',2)
        else:
            return orthcount(u'EH ',1)
    else:
        if word[0:2]==u'\xe4u':
            return orthcount(u'OY ',2)
        else:
            return orthcount(u'EH ',1)
def umophone(word):
    return orthcount(u'OE ',1)
def umuphone(word):
    return orthcount(u'YO ',1)
def bphone(word):
    if len(word)==1:
        return orthcount(u'P ',1)
    else:
        return orthcount(u'B ',1)
def cphone(word):
    if len(word)==1:
        return orthcount(u'K ',1)
    elif len(word)==2:
        if word==u'ch':
            return orthcount(u'CX ',2)
        elif word in {u'c\xe4',u'ce',u'ci'}:
            return orthcount(u'T S ',1)
        else:
            return orthcount(u'K ',1)
    elif len(word)==3 and word==u'chs':
        return orthcount(u'CX ',3)
    elif len(word)==3 and word in {u'cha',u'cho',u'chu'}:
        return orthcount(u'X ',2)
    else:
        if word[0:3]==u'chs':
            return orthcount(u'CX ',3)
        elif word[0:3] in {u'cha',u'cho',u'chu'}:
            return orthcount(u'X ',2)
        elif word[0:2]==u'ch':
            return orthcount(u'CX ',2)
        elif word[0:2] in {u'c\xe4',u'ce',u'ci'}:
            return orthcount(u'T S ',1)
        else:
            return orthcount(u'K ',1)
def dphone(word):
    if len(word)==1:
        return orthcount(u"T ",1)
    elif (len(word)==4 and word==u'dsch') or (len(word)>4 and word[0:4]==u'dsch'):
        return orthcount(u'JH ',4)
    elif len(word)==2 and word==u'dt':
        return orthcount(u'T ',2)
    else:
        if word[0:2]==u'dt':
            return orthcount(u'T ',2)
        else:
            return orthcount(u'D ',1)
def fphone(word):
    return orthcount(u'F ',1)
def gphone(word,preceeding):
    if preceeding==u'i':
        return orthcount(u'K ',1)
    elif len(word)==1:
        return orthcount(u'K ',1)
    else:
        return orthcount(u'G ',1)
def hphone(word):
    return orthcount(u'H ',1)
def jphone(word):
    return orthcount(u'Y ',1)
def kphone(word):
    return orthcount(u'K ',1)
def lphone(word):
    return orthcount(u'L ',1)
def mphone(word):
    return orthcount(u'M ',1)
def nphone(word):
    if len(word)==1:
        return orthcount(u'N ',1)
    elif len(word)==2 and word==u'ng':
        return orthcount(u'NG ',2)
    elif len(word)==2 and word==u'nk':
        return orthcount(u'NG K ',2)
    else:
        if word[0:2]==u'ng':
            return orthcount(u'NG ',2)
        elif word[0:2]==u'nk':
            return orthcount(u'NG K ',2)
        else:
            return orthcount(u'N ',1)
def pphone(word):
    if len(word)==1:
        return orthcount(u'P ',1)
    elif len(word)==2:
        if word==u'pf':
            return orthcount(u'PF ',2)
        elif word==u'ph':
            return orthcount(u'F ',2)
        else:
            return orthcount(u'P ',1)
    else:
        if word[0:2]==u'pf':
            return orthcount(u'PF ',2)
        elif word[0:2]==u'ph':
            return orthcount(u'F ',2)
        else:
            return orthcount(u'P ',1)
def qphone(word):
    return orthcount(u'K V ',2)
def rphone(word):
    if len(word)==1:
        return orthcount(u'AR ',1)
    elif len(word)==2:
        if word in {u'ra',u're',u'ri',u'ro',u'ru',u'ry',u'r\xe4',u'r\xf6',u'r\xfc'}:
            return orthcount(u'R ',1)
        else:
            return orthcount(u'AR ',1)
    else:
        if word[0:2] in {u'ra',u're',u'ri',u'ro',u'ru',u'ry',u'r\xe4',u'r\xf6',u'r\xfc'}:
            return orthcount(u'R ',1)
        else:
            return orthcount(u'AR ',1)
def sphone(word):
    if len(word)==1:
        return orthcount(u'Z ',1)
    elif len(word)==2:
        if word==u'ss':
            return orthcount(u'S ',2)
        elif word==u'sp':
            return orthcount(u'SH ',2)
        elif word==u'st':
            return orthcount(u'SH ',2)
        else:
            return orthcount(u'Z ',1)
    elif len(word)==3 and word==u'sch':
        return orthcount(u'SH ',3)
    else:
        if word[0:3]==u'sch':
            return orthcount(u'SH ',3)
        elif word[0:2]==u'sp':
            return orthcount(u'SH ',2)
        elif word[0:2]==u'st':
            return orthcount(u'SH ',2)
        elif word[0:2]==u'ss':
            return orthcount(u'S ',2)
        else:
            return orthcount(u'Z ',1)
def stsetphone(word):
    return orthcount(u'S ',1)
def tphone(word):
    if len(word)==1:
        return orthcount(u'T ',1)
    elif len(word)==2:
        if word==u'th':
            return orthcount(u'T ',2)
        elif word==u'ti':
            return orthcount(u'T IY ',2)
        else:
            return orthcount(u'T ',1)
    elif word==u'tsch':
        return orthcount(u'T SH ',4)
    elif len(word)==3:
        if word[0:2]==u'th':
            return orthcount(u'T ',2)
        elif word[0:2]==u'ti':
            return orthcount(u'T IY ',2)
        else:
            return orthcount(u'T ',1)
    elif len(word)==4:
        if word in {u'tion',u'ti\xe4r',u'tial'}:
            return orthcount(u'T S IH ',2)
        elif word[0:2]==u'th':
            return orthcount(u'T ',2)
        elif word[0:2]==u'ti':
            return orthcount(u'T IY ',2)
        else:
            return orthcount(u'T ',1)
    elif word==u'tiell':
        return orthcount(u'T S IH ',2)
    else:
        if word[0:4]==u'tsch':
            return orthcount(u'T SH ',4)
        elif word[0:5]==u'tiell':
            return orthcount(u'T S IH ',2)
        elif word[0:4] in {u'tion',u'ti\xe4r',u'tial'}:
            return orthcount(u'T S IH ',2)
        elif word[0:2]==u'ti':
            return orthcount(u'T IY ',2)
        elif word[0:2]==u'th':
            return orthcount(u'T ',2)
        else:
            return orthcount(u'T ',1)
def vphone(word):
    return orthcount(u'F ',1)
def wphone(word):
    return orthcount(u'V ',1)
def xphone(word):
    return orthcount(u'K S ',1)
def zphone(word):
    if len(word)<4:
        return orthcount(u'T S ',1)
    elif len(word)==4:
        if word==u'zsch':
            return orthcount(u'T SH ',4)
        else:
            return orthcount(u'T S ',1)
    else:
        if word[0:4]==u'zsch':
            return orthcount(u'T SH ',4)
        else:
            return orthcount(u'T S ',1)







def graphtophonDeu(worte):
    def strip(string,n):
        if n<len(string):
            return string[n:]
        elif n==len(string):
            return u''
        else:
            return u"Something's wrong"

    savedworte=unicode(worte)
    worte=unicode(worte.lower())
    doublecons={u'bb',u'cc',u'dd',u'ff',u'gg',u'hh',u'jj',u'kk',u'll',u'mm',u'nn',u'pp',u'qq',u'rr',u'tt',u'vv',u'ww',u'xx',u'zz'}
    vowels={u'a',u'e',u'i',u'o',u'u',u'y',u'\xe4',u'\xf6',u'\xfc'}
    for i in doublecons:
        if i in worte:
            worte=worte.replace(i,i[0])
    textentry=u''
    previous=u''
    if worte[-4:]==u'chen':
        diminutive=True
        savedworte=savedworte[:-4]
        worte=savedworte
    else:
        diminutive=False
    while worte!='':
        if worte[0]==u'a':
            counts=aphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'\xe4':
            counts=umaphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'b':
            counts=bphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'c':
            counts=cphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'd':
            counts=dphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'e':
            counts=ephone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'f':
            counts=fphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'g':
            counts=gphone(worte,previous)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'h':
            counts=hphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'i':
            counts=iphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'j':
            counts=jphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'k':
            counts=kphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'l':
            counts=lphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'm':
            counts=mphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'n':
            counts=nphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'o':
            counts=ophone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'\xf6':
            counts=umophone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'p':
            counts=pphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'q':
            counts=qphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'r':
            counts=rphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u's':
            counts=sphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'\xdf':
            counts=stsetphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u't':
            counts=tphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'u':
            counts=uphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'\xfc':
            counts=umuphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'v':
            counts=vphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'w':
            counts=wphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'x':
            counts=xphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'y':
            counts=yphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        elif worte[0]==u'z':
            counts=zphone(worte)
            textentry+=counts.p
            previous=worte[0]
            worte=strip(worte,counts.c)
        else:
            return u'non-alpha character encountered'
    if diminutive==True:
        out=savedworte.upper()+" "+textentry+u'CX EH N\n'
        return out
    else:
        out=savedworte.upper() + ' ' +textentry[:-1]+'\n'
        return out

g=io.open('deuPD.txt',mode='w',encoding='utf8')

for i in range(len(tokens)):
    g.write(graphtophonDeu(tokens[i]))