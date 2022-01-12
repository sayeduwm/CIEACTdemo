from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
   return render(request, "index.html", {})
   
def hellso(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)
   
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from .models import UserCrashData
import csv, io, json
import pandas as pd
# Create your views here.
def UploadView(request):
    # declaring template
    template_name = "index.html"
    data = UserCrashData.objects.all()
    # prompt is a context variable that can have different values         depending on their context
    prompt = {
        'order': 'Order of the CSV should be OFFRNARR,CRSCATGRYINT,CRSHDATE,CRASHTIME,CRSCATGRY,CRSHTYPE,CNTYNAME,MUNINAME,MUNITYPE,INJSVR,LATDECDG,LONDECDG',
        'profiles': data
            }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template_name, prompt)
    elif request.method == 'POST':
        csv_file = request.FILES['file']
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we   are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)
        UserCrashData.objects.all().delete()
        for column in csv.reader(io_string, delimiter=';',  quotechar="|"):
            _, created = UserCrashData.objects.update_or_create(
                OFFRNARR=column[0],
                CRSCATGRYINT=column[1],
                CRSHDATE=column[2],
                CRASHTIME=column[3],
                CRSCATGRY=column[4],
                CRSHTYPE=column[5],
                CNTYNAME=column[6],
                MUNINAME=column[7],
                MUNITYPE=column[8],
                INJSVR=column[9],
                LATDECDG=column[10],
                LONDECDG=column[11],
            )
        context = {}
        return render(request, template_name, context)