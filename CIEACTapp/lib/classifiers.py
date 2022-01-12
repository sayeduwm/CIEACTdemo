import csv
import string
import nltk
from collections import Counter




#U_list = {rows[0]:rows[1] for rows in r3}
def unigramClassifier(text_string,U_list,thrs):
    text_string = text_string.lower()
    exclude = set(string.punctuation)
    text_string = ''.join(ch for ch in text_string if ch not in exclude)
    unigrams = text_string.split()
    WordProbMult = 1
    Positive_Unigams = []
    for unigram in unigrams:
        if unigram in U_list.keys():            
            pr = float(U_list[unigram]) 
            if pr >= thrs:
                WordProbMult = WordProbMult * (1 - pr)
                Positive_Unigams.append(unigram)
    NoisyOR = 1 - WordProbMult
    return NoisyOR,Positive_Unigams
	
#B_list = {rows[0]:rows[1] for rows in r1}	
def bigramClassifier(text_string,B_list,thrs):
    text_string = text_string.lower()
    exclude = set(string.punctuation)
    text_string = ''.join(ch for ch in text_string if ch not in exclude)
    bigrams = []
    bigms = list(nltk.bigrams(text_string .split()))
    bigmC = Counter(bigms)
    for key in bigmC.keys():
        text_string_b = str(key)
        text_string_b = ''.join(ch for ch in text_string_b if ch not in exclude)
        bigrams.append(text_string_b)	
	
    WordProbMult = 1
    Positive_Bigams = []
    for bigram in bigrams:
        if bigram in B_list.keys():
             #(1-p1)^n1*(1-p2)^n2*(1-p3)^n3*(1-p4)^n4 ..... 
            pr = float(B_list[bigram])
            if pr >= thrs:
                WordProbMult = WordProbMult * (1 - pr)
                Positive_Bigams.append(bigram)
			
    NoisyOR = 1 - WordProbMult
    return NoisyOR,Positive_Bigams
	
	
#T_list = {rows[0]:rows[1] for rows in r1}	
def TrigramClassifier(text_string,T_list,thrs):
    text_string = text_string.lower()
    exclude = set(string.punctuation)
    text_string = ''.join(ch for ch in text_string if ch not in exclude)
	
    trigrams = []
    trigms = list(nltk.trigrams(text_string .split()))
    trigmC = Counter(trigms)
            
    for key in trigmC.keys():
        text_string_t = str(key)
        text_string_t = ''.join(ch for ch in text_string_t if ch not in exclude)
        trigrams.append(text_string_t)
	
    WordProbMult = 1
    Positive_Trigams = []
    
    for trigram in trigrams:
        if trigram in T_list.keys():
            #(1-p1)^n1*(1-p2)^n2*(1-p3)^n3*(1-p4)^n4 ..... 
            pr = float(T_list[trigram])
            if pr >= thrs:
                WordProbMult = WordProbMult * (1 - pr)
                Positive_Trigams.append(trigram)
			
    NoisyOR = 1 - WordProbMult
    return NoisyOR	


#U_list = {rows[0]:rows[1] for rows in r3}
#B_list = {rows[0]:rows[1] for rows in r1}
def uniBigramClassifier(text_string,U_list,B_list,thrs):
    text_string = text_string.lower()
    exclude = set(string.punctuation)
    text_string = ''.join(ch for ch in text_string if ch not in exclude)
    unigrams = text_string.split()    
    bigrams = []
    bigms = list(nltk.bigrams(text_string .split()))
    bigmC = Counter(bigms)
    for key in bigmC.keys():
        text_string_b = str(key)
        text_string_b = ''.join(ch for ch in text_string_b if ch not in exclude)
        bigrams.append(text_string_b)
    
    WordProbMult = 1
    Positive_Unigams = []
    Positive_Bigams = []
    for unigram in unigrams:
        if unigram in U_list.keys():            
            pr = float(U_list[unigram]) 
            if pr >= thrs:
                WordProbMult = WordProbMult * (1 - pr)
                Positive_Unigams.append(unigram)
    for bigram in bigrams:
        if bigram in B_list.keys():
             #(1-p1)^n1*(1-p2)^n2*(1-p3)^n3*(1-p4)^n4 ..... 
            pr = float(B_list[bigram])
            if pr >= thrs:
                WordProbMult = WordProbMult * (1 - pr)
                Positive_Bigams.append(bigram)
                
    NoisyOR = 1 - WordProbMult
    return NoisyOR,Positive_Unigams,Positive_Bigams 
    
    
def ClassifierUthrs(text_string,U_list,B_list,T_list,Uthrs,Tthrs):
    text_string = text_string.lower()
    exclude = set(string.punctuation)
    text_string = ''.join(ch for ch in text_string if ch not in exclude)
    unigrams=[]
    bigrams = []
    trigrams = []
    
    if U_list is not None:    
        unigrams = text_string.split()
        WordProbMult = 1
        Positive_Unigams = []
        for unigram in unigrams:
            if unigram in U_list.keys():            
                pr = float(U_list[unigram]) 
                if pr >= Uthrs:
                    WordProbMult = WordProbMult * (1 - pr)
                    Positive_Unigams.append(unigram)
        NoisyORU = 1 - WordProbMult
        
    if B_list is not None:        
        bigms = list(nltk.bigrams(text_string .split()))
        bigmC = Counter(bigms)
        for key in bigmC.keys():
            text_string_b = str(key)
            text_string_b = ''.join(ch for ch in text_string_b if ch not in exclude)
            bigrams.append(text_string_b)
        WordProbMult = 1
        for bigram in bigrams:
            if bigram in B_list.keys():             
                pr = float(B_list[bigram])
                if pr >= Bthrs:
                    WordProbMult = WordProbMult * (1 - pr)
                    Positive_Bigams.append(bigram)
                    
        NoisyORB = 1 - WordProbMult
        
    if T_list is not None:        
        trigms = list(nltk.trigrams(text_string .split()))
        trigmC = Counter(trigms)                
        for key in trigmC.keys():
            text_string_t = str(key)
            text_string_t = ''.join(ch for ch in text_string_t if ch not in exclude)
            trigrams.append(text_string_t)
        
        WordProbMult = 1
        Positive_Trigams = []
        for trigram in trigrams:
            if trigram in T_list.keys():                
                if pr >= Tthrs:
                    WordProbMult = WordProbMult * (1 - pr)
                    Positive_Trigams.append(trigram)
                
        NoisyORT = 1 - WordProbMult

    
    if hybirdModel=="UB": 
        if len(unigrams)==0:
            unigrams = text_string.split()       
    
        if len(bigrams)==0:            
            bigms = list(nltk.bigrams(text_string .split()))
            bigmC = Counter(bigms)
            for key in bigmC.keys():
                text_string_b = str(key)
                text_string_b = ''.join(ch for ch in text_string_b if ch not in exclude)
                bigrams.append(text_string_b)        
            WordProbMult=1
            Positive_Unigams = []
            Positive_Bigams = []
            for unigram in unigrams:
                if unigram in U_list.keys():            
                    pr = float(U_list[unigram]) 
                    if pr >= Uthrs:
                        WordProbMult = WordProbMult * (1 - pr)
                        Positive_Unigams.append(unigram)
            for bigram in bigrams:
                if bigram in B_list.keys():             
                    pr = float(B_list[bigram])
                    if pr >= Bthrs:
                        WordProbMult = WordProbMult * (1 - pr)
                        Positive_Bigams.append(bigram)
                        
            NoisyORUB = 1 - WordProbMult
        else:
            NoisyORUB=NoisyORU*NoisyORB
        
    return NoisyORU,NoisyORB,NoisyORT,NoisyORUB,Positive_Unigams,Positive_Bigams,Positive_Trigams