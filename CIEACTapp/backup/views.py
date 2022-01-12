from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from datetime import datetime
from django.contrib import messages
from .models import UserDatabase,AdminDatabase,UserQuery
from .models import DistractedUnigram,DistractedBigram,DistractedTrigram
from .models import InattentiveUnigram,InattentiveBigram,InattentiveTrigram
from .models import WorkzoneUnigram,WorkzoneBigram,WorkzoneTrigram
import csv, io
from .classifiers import ClassifierWthrs
from .modelNameQuery import pullWordProbability
from asgiref.sync import sync_to_async,async_to_sync
import time,asyncio
from django.template import loader
# Create your views here.

    
def UploadView(request):

    # declaring template
    template_name = "index.html"
    data = UserDatabase.objects.all()
    
    # prompt is a context variable that can have different values         depending on their context
    prompt = {
        'order': 'Order of the CSV should be OFFRNARR,CRSCATGRYINT,CRSHDATE,CRASHTIME,CRSCATGRY,CRSHTYPE,CNTYNAME,MUNINAME,MUNITYPE,INJSVR,LATDECDG,LONDECDG',
        'profiles': data
            }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template_name, prompt)
    elif request.method == 'POST':
        print(request.POST.get('modelname'))
        print (request.POST.get('email'))
        emailId=request.POST.get('email')
        dataId=request.POST.get('dataID')       
        #ret=DistractedUnigram.objects.raw('select * FROM "CIEACTapp_distractedunigram"')
        U_list,B_list,T_list,hybrid=pullWordProbability(request.POST.getlist('modelname')) 
        print(request.POST.getlist('modelname'))
       
        
        csv_file = request.FILES['file']        
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
            return redirect(reverse('fileupload'))
        data_set = csv_file.read().decode('UTF-8')
        lines = data_set.split("\n")
        #print (lines)
        lines.pop(0)
                
        # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)
        UserDatabase.objects.all().delete()        
        for line in lines:
            if line:
                
                           
                column = line.split(',')
                narrative=','.join(i for i in column[14:]) 
                
                NoisyORU,NoisyORB,NoisyORT,NoisyORUB,Positive_Unigams,Positive_Bigams,Positive_Trigams=ClassifierWthrs( narrative, U_list,B_list,T_list,hybrid,0.3,0.3,0.3)              
                date=column[1]
                print(Positive_Unigams,Positive_Bigams,Positive_Trigams)                
                                
                _, created = UserDatabase.objects.update_or_create(
                        EMAIL=emailId,
                        DATAID=dataId,
                        CRSHNMBR=column[0],                                                
                        CRSHDATE=datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d'),
                        #CRSCATGRYINT=column[3],
                        #CRSCATGRY=column[4],
                        #CRSHTYPE=column[5],
                        INJSVR=column[2],                
                        CRASHTIME=column[3],
                        ONHWY=column[4],
                        ONSTR=column[5],
                        ATHWY=column[6],
                        ATSTR=column[7],
                        HWYCLASS=column[8],
                        CNTYNAME=column[9],
                        MUNINAME=column[10],
                        MUNITYPE=column[11],
                        LATDECDG=column[12],
                        LONDECDG=column[13],
                        OFFRNARR=narrative,                        
                        NOISYORU=NoisyORU,
                        NOISYORB=NoisyORB,
                        NOISYORT=NoisyORT,
                        NOISYORUB=NoisyORUB,
                        POSUNIGRAM=Positive_Unigams,
                        POSBIGRAM=Positive_Bigams,
                        POSTRIGRAM=Positive_Trigams
                        
                        
                )
        read_output=UserDatabase.objects.all()
        print(read_output)
        context = {'m':read_output,}
        messages.success(request, 'CSV file updated.') 
        template = loader.get_template('models.html')        

        return HttpResponse(template.render(context, request))


    
