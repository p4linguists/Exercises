# -*- coding: utf-8 -*-
import codecs
corp=codecs.open('data\\sample.conll', 'r', 'utf-8').read()
sents=corp.split('\n\n')
D={}
for i in sents:
    words=i.split('\n')
    for j in words:
        wordf=j.split('\t')
        if wordf[3]=='IDEN':
            if wordf[2] not in D:
                D[wordf[2]]=1
            else:
                D[wordf[2]]+=1
for i in D:
    print(i+'\t'+str(D[i]))
