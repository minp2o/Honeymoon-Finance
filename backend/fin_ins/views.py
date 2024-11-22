from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .serializers import *
from .models import *
# from .settings import API_KEY

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
# 경로만 참조하는거

# save_deposit_products requests 모듈을 활용하여 정기예금 상품 목록 데이터를 가져와 정기예금
# 상품 목록과 옵션 목록을 DB에 저장 GET
@api_view(['GET'])
def save_deposit_products(request):
    # 예금 url
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    resp = requests.get(url).json()
    baselist = resp.get("result").get("baseList")
    optionlist = resp.get("result").get("optionList")
    
    # 예금 정보를 /compare 주소로 전송
    compare_url = 'http://localhost:5173/compare'  # /compare 주소로 변경
    requests.post(compare_url, json={'baseList': baselist, 'optionList': optionlist})  # 예금 정보 전송
    for base in baselist:
        save_data = {
            'dcls_month': base.get('dcls_month'), # '202
            'fin_prdt_cd': base.get('fin_prdt_cd'),
            'kor_co_nm': base.get('kor_co_nm'),
            'fin_prdt_nm': base.get('fin_prdt_nm'),
            'etc_note': base.get('etc_note'),
            'join_deny': int(base.get('join_deny')),
            'join_member': base.get('join_member'),
            'join_way': base.get('join_way'),
            'spcl_cnd': base.get('spcl_cnd'),
        }
        for elem in save_data:
            if not save_data[elem]:
                save_data[elem] = -1
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid():
            serializer.save()
    for option in optionlist:
        save_data = {
            'dcls_month': option.get('dcls_month'), # '202001
            'fin_prdt_cd': option.get('fin_prdt_cd'),
            'intr_rate_type_nm': option.get('intr_rate_type_nm'),
            'intr_rate': option.get('intr_rate'),
            'intr_rate2': option.get('intr_rate2'),
            'save_trm': int(option.get('save_trm')),   
        }
        for elem in save_data:
            if not save_data[elem]:
                save_data[elem] = -1
        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid():
            serializer.save(product=DepositProducts.objects.get(fin_prdt_cd=save_data.get('fin_prdt_cd')))
    return Response({"message": "okay "})


# deposit_products GET: 전체 정기예금 상품 목록 반환
# POST: 상품 데이터 저장 GET, POST
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message':'이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.'})


# deposit_product_options 특정 상품의 옵션 리스트 반환 GET
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    depositoptions = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(depositoptions, many=True)
    return Response(serializer.data)