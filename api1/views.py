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
        return Response(json_data)
    except(Branches.DoesNotExist):
        return HttpResponse("<h1>INVALID IFSC CODE</h1>")


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
        
    return Response(json_data)




