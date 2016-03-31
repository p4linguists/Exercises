# -*- coding: utf-8 -*-
import codecs
corp=codecs.open('data\\sample.conll', 'r', 'utf-8').read()
sents=corp.split('\n\n')
L=[]
C=[]
for i in sents:
    words=i.split('\n')
    for j in words:
        wordf=j.split('\t')
        if wordf[3]=='IDEN':
            if wordf[2] not in L:
                L.append(wordf[2])
                C.append(1)
            else:
                C[L.index(wordf[2])]+=1
for i in range(len(L)):
    print(L[i]+'\t'+str(C[i]))
