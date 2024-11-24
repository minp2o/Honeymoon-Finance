from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from django.conf import settings

from .models import LoanProducts,LoanOptions
from .serializers import LoanProductsSerializer,LoanOptionsSerializer


@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    url = f"http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={api_key}&topFinGrpNo=050000&pageNo=1"

    response = requests.get(url).json()
    return Response(response)