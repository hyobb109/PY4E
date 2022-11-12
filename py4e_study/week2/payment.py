def yearly_payment(m_pay) :
    # 세전 연봉
    pre_tax = m_pay * 12
    # 누진세율 적용하여 tax 구함
    if pre_tax <= 1200 :
        tax = pre_tax * 0.06
    elif pre_tax <= 4600 :
        tax = pre_tax * 0.15 - 108
    elif pre_tax <= 8800 :
        tax = pre_tax * 0.24 - 522
    elif pre_tax <= 15000 :
        tax = pre_tax * 0.35 - 1490
    elif pre_tax <= 30000 :
        tax = pre_tax * 0.38 - 1940
    elif pre_tax <= 50000 :
        tax = pre_tax * 0.4 - 2540
    else :
        tax = pre_tax * 0.42 - 3540
    # 세후 연봉 정수형으로 계산
    after_tax = int(pre_tax - tax)
    # 만원 앞에 공백 없이 출력하기 위해 % 사용
    print("세전 연봉: %d만원" %(pre_tax))
    print("세후 연봉: %d만원" %(after_tax))

try :
    monthly_payment = int(input("월급(만원): "))
    yearly_payment(monthly_payment)
# 숫자 아닌 값이 입력되었을 때 에러메시지
except ValueError:
    print("잘못 입력하셨습니다. 숫자만 입력해주세요.")