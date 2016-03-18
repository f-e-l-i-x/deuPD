import io
import nltk
import re

class orthcount:
    def __init__(self,phone,lettercount):
        self.p=phone
        self.c=lettercount
    def __str__(self):
        return str(self.p)+', '+str(self.c)

vowels={u'a',u'e',u'i',u'o',u'u',u'\xe1',u'\xe9',u'\xed',u'\xf3',u'\xfa',u'\xfc'}

def bphone(word,before):
    if before==u'':
        return orthcount(u'B ',1)
    elif before in {u'm',u'n'}:
        return orthcount(u'B ',1)
    else:
        return orthcount(u'VF ',1)
def vphone(word,before):
    if before in {u'',u'm',u'n'}:
        return orthcount(u'B ',1)
    else:
        return orthcount(u'VF ',1)
def cphone(word):
    if len(word)==1:
        return orthcount(u'K ',1)
    elif len(word)==2:
        if word in {u'ce',u'ci'}:
            return orthcount(u'S ',1)
        elif word==u'ch':
            return orthcount(u'CH ',2)
        else:
            return orthcount(u'K ',1)
    else:
        if word[0:2] in {u'ce',u'ci'}:
            return orthcount(u'S ',1)
        elif word[0:2]==u'ch':
            return orthcount(u'CH ',2)
        else:
            return orthcount(u'K ',1)
def dphone(word,before):
    if before in {u'',u'l',u'n'}:
        return orthcount(u'D ',1)
    else:
        return orthcount(u'DH ',1)
def fphone(word):
    return orthcount(u'F ',1)
def gphone(word,before):
    if len(word)==1:
        if before in {u'e',u'i'}:
            return orthcount(u'X ',1)
        elif before in {u'',u'n'}:
            return orthcount(u'G ',1)
        else:
            return orthcount(u'VF ',1)
    elif len(word)==2:
        if word==u'gu':
            if before in {u'',u'n'}:
                return orthcount(u'G W ',2)
            else:
                return orthcount(u'',2)
        elif before in {u'e',u'i'}:
            return orthcount(u'X ',1)
        elif before in {u'',u'n'}:
            return orthcount(u'G ',1)
        else:
            return orthcount(u'VF ',1)
    else:
        if word[0:2]==u'gu':
            if word[2] in {u'a',u'o'} and before in {u'',u'n'}:
                return orthcount('G W ',2)
            elif word[2] in {u'a',u'o'}:
                return orthcount('VF W ',2)
            elif word[2] in {u'e',u'i'}:
                if before==u'':
                    return orthcount(u'G ',2)
                else:
                    return orthcount(u'VF ',2)
            else:
                return orthcount(u'VF ',2)
        elif word[0:2]==u'g\xfc':
            if word[2] in {u'e',u'i'}:
                return orthcount(u'G W ',2)
            else:
                return orthcount(u'VF W ',2)
        else:
            if before in {u'e',u'i'}:
                return orthcount(u'X ',1)
            elif before in {u'',u'n'}:
                return orthcount(u'G ',1)
            else:
                return orthcount(u'VF ',1)
def hphone(word):
    if len(word)<3:
        return orthcount(u'',1)
    else:
        if word[0:2]==u'hi' and word[2] in vowels:
            return orthcount(u'Y ',2)
        elif word[0:2]==u'hu' and word[2] in vowels:
            return orthcount(u'W ',2)
        else:
            return orthcount(u'',1)
def jphone(word):
    return orthcount(u'X ',1)
def kphone(word):
    return orthcount(u'K ',1)
def lphone(word):
    if len(word)==1:
        return orthcount(u'L ',1)
    elif len(word)==2:
        if word==u'll':
            return orthcount(u'LL ',2)
        else:
            return orthcount(u'L ',1)
    else:
        if word[0:2]==u'll':
            return orthcount(u'LL ',2)
        else:
            return orthcount(u'L ',1)
def mphone(word):
    if word==u'm':
        return orthcount(u'N ',1)
    else:
        return orthcount(u'M ',1)
def nphone(word):
    if len(word)==1:
        return orthcount(u'N ',1)
    elif len(word)==2:
        if word in {u'np',u'nt',u'nk'}:
            return orthcount(u'NG ',1)
        elif word=='ny':
            return orthcount(u'NY ',2)
        else:
            return orthcount(u'N ',1)
    else:
        if word[0:2]in {u'np',u'nt',u'nk'}:
            return orthcount(u'NG ',1)
        elif word[0:2]==u'ny':
            return orthcount(u'NY ',2)
        else:
            return orthcount(u'N ',1)
def ntildphone(word):
    return orthcount(u'NY ',1)
def pphone(word):
    return orthcount(u'P ',1)
def qphone(word):
    return orthcount(u'K ',2)
def rphone(word,before):
    if word==u'r':
        return orthcount(u'AT ',1)
    elif len(word)==2:
        if word==u'rr':
            return orthcount(u'RT ',2)
        elif before in {u'',u'l',u'n',u's'}:
            return orthcount(u'RT ',1)
        else:
            return orthcount(u'AT ',1)
    else:
        if word[0:2]==u'rr':
            return orthcount(u'RT ',2)
        elif before in {u'',u'l',u'n',u's'}:
            return orthcount(u'RT ',1)
        else:
            return orthcount(u'AT ',1)
def sphone(word):
    if word=='s':
        return orthcount(u'S ',1)
    elif len(word)==2:
        if word==u'sh':
            return orthcount(u'SH ',2)
        elif word[1] in {u'b',u'v',u'g',u'm',u'n',u'r',u'w'}:
            return orthcount(u'Z ',1)
        else:
            return orthcount(u'S ',1)
    elif len(word)==3:
        if word[0:2]==u'sh':
            return orthcount(u'SH ',2)
        elif word[1] in {u'b',u'v',u'g',u'm',u'n',u'r',u'w'}:
            return orthcount(u'Z ',1)
        elif word in {u'shi',u'shu',u'sll'}:
            return orthcount(u'Z ',1)
        else:
            return orthcount(u'S ',1)
    else:
        if word[0:2]==u'sh':
            return orthcount(u'SH ',2)
        elif word[1] in {u'b',u'v',u'g',u'm',u'n',u'r',u'w'}:
            return orthcount(u'Z ',1)
        elif word[0:3] in {u'shi',u'shu',u'sll'}:
            return orthcount(u'Z ',1)
        else:
            return orthcount(u'S ',1)
def tphone(word):
    if word==u't':
        return orthcount(u'T ',1)
    elif len(word)==2:
        if word==u'tl':
            return orthcount(u'T L ',2)
        elif word==u'tx':
            return orthcount(u'CH ',2)
        elif word==u'tz':
            return orthcount(u'T S ',2)
        else:
            return orthcount(u'T ',1)
    else:
        if word[0:2]==u'tl':
            return orthcount(u'T L ',2)
        elif word[0:2]==u'tx':
            return orthcount(u'CH ',2)
        elif word[0:2]==u'tz':
            return orthcount(u'T S ',2)
        else:
            return orthcount(u'T ',1)
def wphone(word):
    return orthcount('W ',1)
def xphone(word,before):
    if before==u'':
        return orthcount(u'S ',1)
    else:
        return orthcount(u'K S ',1)
def zphone():
    return orthcount('S ',1)
def mexphone():
    return orthcount('X ',1)

def isaccent(word):
    for i in word:
        if i in {u'\xe1',u'\xe9',u'\xed',u'\xf3',u'\xfa',u'\xfc'}:
            return True
    return False

def stressfinder(word):
    subword=u''
    for letter in word:
        if letter in vowels:
            subword+=letter
    count=0
    if isaccent(subword):
        for vowel in subword:
            if vowel in {u'\xe1',u'\xe9',u'\xed',u'\xf3',u'\xfa',u'\xfc'}:
                return count
            count+=1
    elif word[-1] in vowels or word[-1] in {u'n',u's'}:
        count=len(subword)-2
        return count
    else:
        count=len(subword)-1
        return count


def vowelphone(vowel,stress=False):
    if stress:
        num=u'1 '
    if not stress:
        num=u'0 '
    if vowel in {u'a',u'\xe1'}:
        return orthcount(u'A'+num,1)
    elif vowel in {u'e',u'\xe9'}:
        return orthcount(u'E'+num,1)
    elif vowel in {u'i',u'\xed'}:
        return orthcount(u'IY'+num,1)
    elif vowel in {u'o',u'\xf3'}:
        return orthcount(u'O'+num,1)
    elif vowel in {u'u',u'\xfa',u'\xfc'}:
        return orthcount(u'UW'+num,1)
    elif vowel==u'y':
        return orthcount(u'IY'+num,1)

def strip(string,n):
    if n<len(string):
        return string[n:]
    elif n==len(string):
        return u''
    else:
        return u"Something's wrong"

def graphtophoneSpan(word):
    word=word.lower()
    textentry=u''
    previous=u''
    savedword=word
    if u'm\xe9xic' in word:
        word=re.sub(u'\xe9x',u'\xe9\x10',word)
    stress=stressfinder(word)
    strcount=0
    while word!=u'':
        if word[0] in vowels:
            if strcount==stress:
                count=vowelphone(word[0],True)
                textentry+=count.p
                strcount+=1
                previous=word[0]
                word=strip(word,1)
            else:
                count=vowelphone(word[0])
                textentry+=count.p
                strcount+=1
                previous=word[0]
                word=strip(word,1)
        elif word[0]==u'b':
            counts=bphone(word,previous)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'v':
            counts=vphone(word,previous)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'c':
            counts=cphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'd':
            counts=dphone(word,previous)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'f':
            counts=fphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'g':
            counts=gphone(word,previous)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'h':
            counts=hphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'j':
            counts=jphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'k':
            counts=kphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'l':
            counts=lphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'm':
            counts=mphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'n':
            counts=nphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u"\xf1":
            counts=ntildphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'p':
            counts=pphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'q':
            counts=qphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'r':
            counts=rphone(word,previous)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u's':
            counts=sphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u't':
            counts=tphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'w':
            counts=wphone(word)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'x':
            counts=xphone(word,previous)
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'\x10':
            counts=mexphone()
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        elif word[0]==u'z':
            counts=zphone()
            textentry+=counts.p
            previous=word[0]
            word=strip(word,counts.c)
        else:
            word=strip(word,1)
    return savedword.upper()+' '+textentry[:-1]+'\n'










f=io.open('clean_spanish.txt',mode='r',encoding='utf8')
raw=f.read()
tokens=raw.split()

g=io.open('spanPD.txt',mode='w',encoding='utf8')
for word in tokens:
    g.write(graphtophoneSpan(word))