from rest_framework import serializers
from api1.models import Banks,Branches


class BranchesSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Branches
        fields = [
            'bank_id',
            'branch',
            'city',
            'district',
            'state',
            'address',
        ]


class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = [
            'name',
            'id',
        ]