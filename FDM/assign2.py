import nltk

import os

import re

from nltk.util import Index
from collections import defaultdict
import math



term1='Shared Computer Resources'
words_in_term1=nltk.word_tokenize(term1)
print(words_in_term1)

term2='Computer Services'
words_in_term2=nltk.word_tokenize(term2)
print(words_in_term2)

term3='Digital Shared Components'
words_in_term3=nltk.word_tokenize(term3)
print(words_in_term3)

term4='Computer Resources Shared Components'
words_in_term4=nltk.word_tokenize(term4)
print(words_in_term4)

index1=0

DF = defaultdict(term4) 
#if term1[0]==term2[0]:
#    index1+=1
#    if term[0]==ter

for a in range(term3):
    # if term1[0]==a:
    #     index1=index1+1
    a=a+1
print(a)

# for a1 in range(len(term3)):
#     if term1[0]==a1:
#         index1+=1

# for a2 in range(len(term4)):
#     if term1[0]==a2:
#         index1+=1

# print(index1)