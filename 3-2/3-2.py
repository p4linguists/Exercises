# -*- coding: utf-8 -*-
import codecs

# File1
corp1=codecs.open('data\\text1.txt', 'r', 'utf-8').read()
scorp1=corp.split()
lexdiv1=len(set(scorp1))/len(scorp1)*100

# File2
corp2=codecs.open('data\\text2.txt', 'r', 'utf-8').read()
scorp2=corp2.split()
lexdiv2=len(set(scorp2))/len(scorp2)*100

# Compare
if lexdiv1>lexdiv2:
    print ('File1 more diverse.')
elif lexdiv2>lexdiv1:
    print ('File2 more diverse.')
else:
    print ('Equal Lexical Diversity')
