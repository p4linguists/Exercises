# -*- coding: utf-8 -*-
import codecs
# sample.conll=1000 sentence sample of Persian Dependency Treebank (http://dadegan.ir/catalog/perdt)
corp=codecs.open('data\\sample.conll', 'r', 'utf-8').read()
sents=corp.split('\n\n')
L=[]
for i in sents:
    words=i.split('\n')
    for j in words:
        wordf=j.split('\t')
        if wordf[3]=='IDEN':
            if wordf[2] not in L:
                L.append(wordf[2])
for i in sorted(L):
    print(i)
