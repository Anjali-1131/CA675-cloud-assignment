# #!/usr/bin/python

# import sys
# import os
# import math

# #input: (word, (word, doc_id), (count, total_count))
# #output: ((word, doc_id), tfidf)
# lines = []
# df_t = {}
# docs = []

# # df_t = number of times a word appears in the docs
# for line in sys.stdin:
# 	line = line.strip()
# 	lines.append(line)
# 	word, values = line.split('\t', 1)
# 	key, value = values.split('\t', 1)
# 	word, doc = key.split(' ', 1)
# 	count, total = value.split(' ', 1)
# 	if word not in df_t:
# 		df_t[word] = 1
# 	else:
# 		df_t[word] += 1
# 	if doc not in docs:
# 		docs.append(doc)
# # n_docs = total number of documents
# n_docs = len(docs)
# for line in lines:
# 	word, values = line.split('\t', 1)
# 	key, value = values.split('\t', 1)
# 	word, doc = key.split(' ', 1)
# 	count, total = value.split(' ', 1)
# 	# tf_t_d = number of times a word appears in a doc
# 	tf_t_d = float(count)
# 	# n_d = number of words in a doc
# 	n_d = float(total)
# 	tf = tf_t_d/n_d
# 	idf = math.log10(n_docs/df_t[word])
# 	tfidf = tf*idf
# 	key = str(word) + ' ' + str(doc)
# 	print('%10.10f\t%s' % (key, tfidf))


#!/usr/bin/env python3 

from operator import itemgetter
import sys

prev_word = None
count = 1 
word = None
df={}
l1=[]
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    w,z= line.split('\t', 1)
    f,nNc = z.split(' ',1)
    n,Nc=nNc.split(' ',1)
    N,c=Nc.split(' ',1)
    if prev_word == w:
        count = count+int(c)
    else:
        if prev_word != None:
            q=n+' '+N+' '+str(count)
            df[prev_word]=q
            j=prev_word+' '+f
            l1.append(j)
        count=1
        prev_word = w

       
q=n+' '+N+' '+str(count)
df[prev_word]=q
j=prev_word+' '+f
l1.append(j)

for h in l1:
   w,f=h.split(' ',1)
   for d in df:
       if w == d:
          print ('%s\t%s' % (h,df[d]))
