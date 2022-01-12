from .models import DistractedUnigram,DistractedBigram,DistractedTrigram
from .models import InattentiveUnigram,InattentiveBigram,InattentiveTrigram
from .models import WorkzoneUnigram,WorkzoneBigram,WorkzoneTrigram
    
    
def pullWordProbability(modelnamelist):
    U_list={}
    B_list={}
    T_list={}
    hybrid="None"
        
    for modelname in modelnamelist:
        
        if modelname=="NoisyOR_W_U":        
            U_list={i.Unigrams:float(i.Probability) for i in WorkzoneUnigram.objects.all()}
        if modelname=="NoisyOR_W_B":        
            B_list={i.Bigrams:float(i.Probability) for i in WorkzoneBigram.objects.all()} 
        if modelname=="NoisyOR_W_T":        
            T_list={i.Trigrams:float(i.Probability) for i in WorkzoneTrigram.objects.all()}
        if modelname=="NoisyOR_W_UB": 
            if not U_list:
                U_list={i.Unigrams:float(i.Probability) for i in WorkzoneUnigram.objects.all()}
            if not B_list:
                B_list={i.Bigrams:float(i.Probability) for i in WorkzoneBigram.objects.all()}
            hybrid="UB"
                
        # Distracted Driver                
        if modelname=="NoisyOR_DD_U":        
            U_list={i.Unigrams:float(i.Probability) for i in DistractedUnigram.objects.all()}
        if modelname=="NoisyOR_DD_B":        
            B_list={i.Bigrams:float(i.Probability) for i in DistractedBigram.objects.all()}
        if modelname=="NoisyOR_DD_T":        
            T_list={i.Trigrams:float(i.Probability) for i in DistractedTrigramigram.objects.all()}
        if modelname=="NoisyOR_DD_UB":        
            if not U_list:
                U_list={i.Unigrams:float(i.Probability) for i in DistractedUnigram.objects.all()}
            if not B_list:
                B_list={i.Bigrams:float(i.Probability) for i in DistractedBigram.objects.all()}
            hybrid="UB"
                
        # Inattentive Driver              
        if modelname=="NoisyOR_INAT_U":        
            U_list={i.Unigrams:float(i.Probability) for i in InattentiveUnigram.objects.all()}
        if modelname=="NoisyOR_INAT_B":        
            B_list={i.Bigrams:float(i.Probability) for i in InattentiveBigram.objects.all()}
        if modelname=="NoisyOR_INAT_T":        
            T_list={i.Trigrams:float(i.Probability) for i in InattentiveTrigram.objects.all()}
        if modelname=="NoisyOR_INAT_UB":        
            if not U_list:
                U_list={i.Unigrams:float(i.Probability) for i in InattentiveUnigram.objects.all()}
            if not B_list:
                B_list={i.Bigrams:float(i.Probability) for i in InattentiveBigram.objects.all()}
            hybrid="UB"   
    return U_list,B_list,T_list,hybrid

            
        