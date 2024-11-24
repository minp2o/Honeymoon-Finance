from django.db import models

class LoanProducts(models.Model):
    dcls_month = models.CharField(max_length=6)  # 공시 제공월 (YYYYMM 형식)
    fin_co_no = models.CharField(max_length=10)  # 금융회사 코드
    fin_prdt_cd = models.CharField(max_length=10)  # 금융 상품 코드
    kor_co_nm = models.CharField(max_length=100)  # 금융회사 명
    fin_prdt_nm = models.CharField(max_length=100)  # 금융상품 명
    join_way = models.TextField()  # 가입 방법
    loan_inci_expn = models.TextField()  # 대출 부대 비용
    erly_rpay_fee = models.TextField()  # 중도 상환 수수료
    dly_rate = models.DecimalField(max_digits=5, decimal_places=2)  # 연체 이자율 (퍼센트)
    loan_lmt = models.DecimalField(max_digits=20, decimal_places=2)  # 대출 한도
    dcls_strt_day = models.DateField(null=True, blank=True)  # 공시 시작일
    dcls_end_day = models.DateField(null=True, blank=True)  # 공시 종료일 (공시 종료일이 없을 수 있음)
    fin_co_subm_day = models.DateField()  # 금융회사 제출일

    def __str__(self):
        return f"{self.kor_co_nm} - {self.fin_prdt_nm}"


class LoanOptions(models.Model):
    loan_product = models.ForeignKey(LoanProducts, related_name='options', on_delete=models.CASCADE)
    rpay_typ = models.CharField(max_length=50)  # 상환 방식 코드
    rpay_type_nm = models.CharField(max_length=100)  # 상환 방식 명
    lend_rate_type = models.CharField(max_length=50)  # 금리 유형 코드
    lend_rate_type_nm = models.CharField(max_length=100)  # 금리 유형 명
    lend_rate_min = models.DecimalField(max_digits=5, decimal_places=2)  # 최소 금리
    lend_rate_max = models.DecimalField(max_digits=5, decimal_places=2)  # 최대 금리
    lend_rate_avg = models.DecimalField(max_digits=5, decimal_places=2)  # 평균 금리

    def __str__(self):
        return f"{self.loan_product.fin_prdt_nm} - {self.rpay_type_nm} - {self.lend_rate_type_nm}"
