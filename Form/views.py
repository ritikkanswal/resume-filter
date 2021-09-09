from django.shortcuts import render
from django.http import HttpResponse
import requests
from json import dumps
import json
# from .forms import ResumeData
# Create your views here.
def showformdata(request):
    if request.method =='POST':
        data=request.FILES
        print(data)
        uploaded_file=data['document']
        url ='http://127.0.0.1:8080/studentapi/'
        data={'name':"Riitik"}
        files = {'file': uploaded_file}
        r = requests.post(url,data=data,files=files)
        # r=r.json()
        
        # Json_Dictionary=json.loads(r.json())
        # for x in Json_Dictionary:
        #     print(x)
        # print(r.json())
        # dump data
        dataJSON = dumps(r.json())
        print(type(r.json()))
        flag=0 # Check There is any match or NOT
        for x in r.json().items():
            if(x[1]!=0):
                flag=1
        # print(r.json())
        if(flag==0):
            return render(request, 'graphs_error.html')
        return render(request, 'graphs.html',{'data':dataJSON})
    return render(request, 'index.html')


def home(request):
    return render(request,'index.html')

def add(request):
    val1=int(request.GET["num1"])
    val2=int(request.GET["num2"])
    res=val1*val2
    return render(request,'res.html',{"result":res})