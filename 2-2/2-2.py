# -*- coding: utf-8 -*-
import codecs
corp=codecs.open('data\\text.txt', 'r', 'utf-8').read()
scorp=corp.split()
# len(set(scorp))=types, len(scorp)=tokens
lexdiv=len(set(scorp))/len(scorp)*100
print ('The lexical diversity of the text is: '+str(round(lexdiv,2))+'%')
