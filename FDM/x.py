
import nltk

import os

import re

from nltk.util import Index


def freq(str):
    
	# break the string into list of words
	str_list = str.split()
	# gives set of unique words
	unique_words = set(str_list)

	
	for words in unique_words :
		print('Frequency of ', words , 'is :', str_list.count(words))


term1='Shared Computer Resources'
term4='Computer Resources Shared Components'
words_in_term1=nltk.word_tokenize(term1)
words_in_term4=nltk.word_tokenize(term4)

#freq(term4)

def AND_operation(word_list1,word_list2): #define a function for and operator
    if ((word_list1) and (word_list2)):
        return set(word_list1).intersection(word_list2)
    else:
        return()

oper_AND=list(AND_operation(words_in_term1,words_in_term4)) #taken the common files for both two files
print('and val',oper_AND),print('\n')

freq(oper_AND)