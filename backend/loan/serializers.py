from rest_framework import serializers
from .models import LoanOptions,LoanProducts

class LoanProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProducts
        fields = "__all__"
        
class LoanOptionsSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = LoanOptions
        fields = "__all__"