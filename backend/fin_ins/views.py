# from collections import Counter
# from django.shortcuts import get_object_or_404
# from django.contrib.auth import get_user_model
# from django.http import HttpResponse, JsonResponse
# from django.conf import settings
# from django.db.models import Q
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes 
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# # from accounts.models import User
# import requests
# from .serializers import *
# from .models import *
# from accounts.serializers import *


# @api_view(['GET'])
# def make_financial_data(request):
#     DEPOSIT_API_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={settings.API_KEY}&topFinGrpNo=020000&pageNo=1'
#     SAVING_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={settings.API_KEY}&topFinGrpNo=020000&pageNo=1'

#     # Deposit API 요청
#     deposit_res = requests.get(DEPOSIT_API_URL)
#     if deposit_res.status_code != 200:
#         return JsonResponse({"error": "Deposit API 요청 실패"}, status=deposit_res.status_code)

#     deposit_data = deposit_res.json().get('result')

#     # Saving API 요청
#     saving_res = requests.get(SAVING_API_URL)
#     if saving_res.status_code != 200:
#         return JsonResponse({"error": "Saving API 요청 실패"}, status=saving_res.status_code)

#     saving_data = saving_res.json().get('result')

#     # API에서 가져온 데이터를 JSON 형식으로 반환
#     return JsonResponse({
#         "deposit": deposit_data,
#         "saving": saving_data
#     })


# @api_view(['GET']) # id 순
# def deposit_list(request):
#     deposits = Deposit.objects.all()
#     serializer = DepositSerializer(deposits, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def deposit_detail(request, deposit_code):
#     deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
#     if request.method == 'GET':
#         serializer = DepositSerializer(deposit)
#         return Response(serializer.data)    
    

# @api_view(['GET'])
# def depositOption_list(request, deposit_code):
#     deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
#     deposit_options = DepositOption.objects.filter(deposit=deposit)

#     if request.method == 'GET':
#         serializer = DepositOptionSerializer(deposit_options, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# def depositOption_detail(request, deposit_code, depositOption_pk):
#     deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
#     deposit_option = get_object_or_404(DepositOption, pk=depositOption_pk, deposit=deposit)

#     if request.method == 'GET':
#         serializer = DepositOptionSerializer(deposit_option)
#         return Response(serializer.data)
    

# @api_view(['GET']) # id 순
# def saving_list(request):
#     savings = Saving.objects.all()
#     serializer = SavingSerializer(savings, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def saving_detail(request, saving_code):
#     saving = get_object_or_404(Saving, saving_code=saving_code)
#     if request.method == 'GET':
#         serializer = SavingSerializer(saving)
#         return Response(serializer.data)

    
# @api_view(['GET'])
# def savingOption_list(request, saving_code):
#     saving = get_object_or_404(Saving, saving_code=saving_code)
#     saving_options = SavingOption.objects.filter(saving=saving)

#     if request.method == 'GET':
#         serializer = SavingOptionSerializer(saving_options, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# def savingOption_detail(request, saving_code, savingOption_pk):
#     savingOption = get_object_or_404(SavingOption, pk=savingOption_pk)
#     if request.method == 'GET':
#         serializer = SavingOptionSerializer(savingOption)
#         return Response(serializer.data)
    

# # 6개월~36개월
# @api_view(['GET'])
# def get_deposits(request, save_trm):
#     deposits = Deposit.objects.filter(depositoption__save_trm=save_trm).order_by('depositoption__intr_rate')

#     serializer = DepositSerializer(deposits, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_savings(request, save_trm):
#     savings = Saving.objects.filter(savingoption__save_trm=save_trm).order_by('savingoption__intr_rate')

#     serializer = SavingSerializer(savings, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_reverse_deposits(request, save_trm):
#     deposits = Deposit.objects.filter(depositoption__save_trm=save_trm).order_by('-depositoption__intr_rate')

#     serializer = DepositSerializer(deposits, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_reverse_savings(request, save_trm):
#     savings = Saving.objects.filter(savingoption__save_trm=save_trm).order_by('-savingoption__intr_rate')

#     serializer = SavingSerializer(savings, many=True)
#     return Response(serializer.data)


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def contract_deposit(request, deposit_code):
#     deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
#     if request.user in deposit.contract_user.all():
#         deposit.contract_user.remove(request.user)
#     else:
#         deposit.contract_user.add(request.user)
#     serializer = ContractDepositSerializer(deposit)
#     return Response(serializer.data)


# @api_view(['GET','POST','DELETE'])
# @permission_classes([IsAuthenticated])
# def contract_deposit(request, deposit_code):
#     deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
#     if request.method == 'GET':
#         serializer = ContractDepositSerializer(deposit)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         if request.user in deposit.contract_user.all():
#             deposit.contract_user.remove(request.user)
#             return Response({ "detail": "삭제되었습니다." }, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({ "detail": "삭제할 항목이 없습니다." }, status=status.HTTP_404_NOT_FOUND)
        
#     elif request.method == 'POST':
#         if request.user not in deposit.contract_user.all():
#             deposit.contract_user.add(request.user)
#             serializer = ContractDepositSerializer(deposit, data=request.data, partial=True)

#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response({ "detail": "상품이 추가되었습니다." }, status=status.HTTP_200_OK)
#         else:
#             return Response({ "detail": "이미 상품이 존재합니다." }, status=status.HTTP_400_BAD_REQUEST)
    

from collections import Counter
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# from accounts.models import User
import requests
from .serializers import *
from .models import *
from accounts.serializers import *



@api_view(['GET'])
def make_financial_data(request):
    DEPOSIT_API_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={settings.API_KEY}&topFinGrpNo=020000&pageNo=1'
    SAVING_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={settings.API_KEY}&topFinGrpNo=020000&pageNo=1'

    # Deposit API 요청
    deposit_res = requests.get(DEPOSIT_API_URL)
    if deposit_res.status_code != 200:
        return JsonResponse({"error": "Deposit API 요청 실패"}, status=deposit_res.status_code)

    deposit_data = deposit_res.json().get('result')

    # Saving API 요청
    saving_res = requests.get(SAVING_API_URL)
    if saving_res.status_code != 200:
        return JsonResponse({"error": "Saving API 요청 실패"}, status=saving_res.status_code)

    saving_data = saving_res.json().get('result')

    # API에서 가져온 데이터를 JSON 형식으로 반환
    return JsonResponse({
        "deposit": deposit_data,
        "saving": saving_data
    })

@api_view(['GET']) # id 순
def deposit_list(request):
    deposits = Deposit.objects.all()
    serializer = DepositSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_detail(request, deposit_code):
    deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
    if request.method == 'GET':
        serializer = DepositSerializer(deposit)
        return Response(serializer.data)    
    

@api_view(['GET'])
def depositOption_list(request, deposit_code):
    deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
    deposit_options = DepositOption.objects.filter(deposit=deposit)

    if request.method == 'GET':
        serializer = DepositOptionSerializer(deposit_options, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def depositOption_detail(request, deposit_code, depositOption_pk):
    deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
    deposit_option = get_object_or_404(DepositOption, pk=depositOption_pk, deposit=deposit)

    if request.method == 'GET':
        serializer = DepositOptionSerializer(deposit_option)
        return Response(serializer.data)
    

@api_view(['GET']) # id 순
def saving_list(request):
    savings = Saving.objects.all()
    serializer = SavingSerializer(savings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def saving_detail(request, saving_code):
    saving = get_object_or_404(Saving, saving_code=saving_code)
    if request.method == 'GET':
        serializer = SavingSerializer(saving)
        return Response(serializer.data)

    
@api_view(['GET'])
def savingOption_list(request, saving_code):
    saving = get_object_or_404(Saving, saving_code=saving_code)
    saving_options = SavingOption.objects.filter(saving=saving)

    if request.method == 'GET':
        serializer = SavingOptionSerializer(saving_options, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def savingOption_detail(request, saving_code, savingOption_pk):
    savingOption = get_object_or_404(SavingOption, pk=savingOption_pk)
    if request.method == 'GET':
        serializer = SavingOptionSerializer(savingOption)
        return Response(serializer.data)
    

# 6개월~36개월
@api_view(['GET'])
def get_deposits(request, save_trm):
    deposits = Deposit.objects.filter(depositoption__save_trm=save_trm).order_by('depositoption__intr_rate')

    serializer = DepositSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_savings(request, save_trm):
    savings = Saving.objects.filter(savingoption__save_trm=save_trm).order_by('savingoption__intr_rate')

    serializer = SavingSerializer(savings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_reverse_deposits(request, save_trm):
    deposits = Deposit.objects.filter(depositoption__save_trm=save_trm).order_by('-depositoption__intr_rate')

    serializer = DepositSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_reverse_savings(request, save_trm):
    savings = Saving.objects.filter(savingoption__save_trm=save_trm).order_by('-savingoption__intr_rate')

    serializer = SavingSerializer(savings, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def contract_deposit(request, deposit_code):
    deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
    if request.user in deposit.contract_user.all():
        deposit.contract_user.remove(request.user)
    else:
        deposit.contract_user.add(request.user)
    serializer = ContractDepositSerializer(deposit)
    return Response(serializer.data)


@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def contract_deposit(request, deposit_code):
    deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
    if request.method == 'GET':
        serializer = ContractDepositSerializer(deposit)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user in deposit.contract_user.all():
            deposit.contract_user.remove(request.user)
            return Response({ "detail": "삭제되었습니다." }, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({ "detail": "삭제할 항목이 없습니다." }, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'POST':
        if request.user not in deposit.contract_user.all():
            deposit.contract_user.add(request.user)
            serializer = ContractDepositSerializer(deposit, data=request.data, partial=True)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({ "detail": "상품이 추가되었습니다." }, status=status.HTTP_200_OK)
        else:
            return Response({ "detail": "이미 상품이 존재합니다." }, status=status.HTTP_400_BAD_REQUEST)
