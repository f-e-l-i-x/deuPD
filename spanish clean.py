import io
import re
import nltk

f=io.open('raw_spanish.txt',mode='r',encoding='utf8')
raw=f.read()
tokens=raw.split()
for i in range(len(tokens)):
    tokens[i]=tokens[i].lower()

g=io.open('clean_spanish.txt',mode='w',encoding='utf8')

for word in tokens:
    if u"'a" in word:
        word=re.sub(u"'a",u'\xE1',word)
    if u"'e" in word:
        word=re.sub(u"'e",u'\xE9',word)
    if u"'i" in word:
        word=re.sub(u"'i",u'\xed',word)
    if u"'o" in word:
        word=re.sub(u"'o",u'\xf3',word)
    if u"'u" in word:
        word=re.sub(u"'u",u'\xfa',word)
    if u'"u' in word:
        word=re.sub(u'"u',u'\xfc',word)
    if u"'n" in word:
        word=re.sub(u"'n",u'\xf1',word)
    g.write(word+'\n')

vowels={u'a',u'e',u'i',u'o',u'u',u'\xe1',u'\xe9',u'\xed',u'xf3',u'\xfa',u'\xfc'}