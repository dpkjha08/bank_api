from django.shortcuts import render
from django.http import HttpResponse
from api1.models import Banks,Branches
from . serializers import BranchesSerializer,BanksSerializer
from rest_framework.response import Response
import json
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    banks = Banks.objects.all()
    return render(request,"home.html",{"banks":banks})

############################## TO GET REST SERVICE USING FORM ##########################

@api_view(['POST'])
def branch(request):
    try:
        ifsc=request.POST['ifsc'].upper()
        branch = Branches.objects.get(ifsc=ifsc)
        get_bank_name = Banks.objects.get(id=branch.bank_id)
        serializer = BranchesSerializer(branch,many=False)
        json_data={
                "ok":True,
                "ifsc":ifsc,
                "bank_name":get_bank_name.name,
                "details":serializer.data
            }
    except(Branches.DoesNotExist):
        json_data={
            "ok":False,
            "ifsc":ifsc,
            "invalid":"IFSC CODE IS INVALID"
        }
        return Response(json_data)
    


@api_view(['POST'])
def bank(request):
    name = request.POST['bank_name'].upper()
    city = request.POST['bank_city'].upper()
    try:
        bank = Banks.objects.get(name=name)
    except(Banks.DoesNotExist):
        return HttpResponse("<h1>INVALID BANK NAME</h1>")

    details = Branches.objects.filter(city=city,bank_id=bank.id)
    json_data ={
        "ok":True,
        "bank_id":bank.id,
        "bank_name":bank.name,
        "city":city,
        "details":[],
    }
    for i in details:
        each_details={
            "branch":i.branch,
            "district":i.district,
            "state":i.state,
            "address":i.address,
        }
        json_data["details"].append(each_details)
    if len(json_data["details"])==0:
        json_data["details"]="Given Bank is not in this city"
        
    return Response(json_data)



############################## TO GET REST SERVICE USING DIRECT LINK ##########################

@api_view(['GET'])
def branch_ifsc(request,ifsc):
    try:
        branch = Branches.objects.get(ifsc=ifsc)
        get_bank_name = Banks.objects.get(id=branch.bank_id)
        serializer = BranchesSerializer(branch,many=False)
        json_data={
                "ok":True,
                "ifsc":ifsc,
                "bank_name":get_bank_name.name,
                "details":serializer.data
            }
    except(Branches.DoesNotExist):
        json_data={
            "ok":False,
            "ifsc":ifsc,
            "invalid":"IFSC CODE IS INVALID"
        }
    return Response(json_data)


@api_view(['GET'])
def bank_name_city(request,name,city):
    name = name.replace("_"," ").upper()
    city = city.upper()
    try:
        bank = Banks.objects.get(name=name)
    except(Banks.DoesNotExist):
        return HttpResponse("<h1>INVALID BANK NAME</h1>")

    details = Branches.objects.filter(city=city,bank_id=bank.id)
    json_data ={
        "ok":True,
        "bank_id":bank.id,
        "bank_name":bank.name,
        "city":city,
        "details":[],
    }
    for i in details:
        each_details={
            "branch":i.branch,
            "district":i.district,
            "state":i.state,
            "address":i.address,
        }
        json_data["details"].append(each_details)
        
    return Response(json_data)