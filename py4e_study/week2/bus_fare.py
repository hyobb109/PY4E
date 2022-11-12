def bus_fare(age, payment_method) :
    if age < 8 or age >= 75 :
        return("무료")
    elif 8 <= age and age < 14 :
        return("450원")
    elif 14 <= age and age < 20 :
        if payment_method == "카드" :
            return("720원")
        elif payment_method == "현금" :
            return("1000원")
    elif age >= 20 :
        if payment_method == "카드":
            return("1200원")
        elif payment_method == "현금":
            return("1300원")
    else :
        return(Error)
try :
    #공백을 기준으로 나이와 지불유형 입력 받음
    age, payment_method = input("나이와 지불 방식을 입력해주세요(현금 or 카드). 예시) 30 현금\n").split()
    age = int(age)
    print("나이: %d세" %(age))
    # 지불 유형 입력값이 카드나 현금이 아니면 잘못된 값이므로 에러메시지 출력
    if payment_method != "카드" and payment_method != "현금" :
        quit()
    print("지불유형:", payment_method)
    print("버스요금:", bus_fare(age, payment_method))
# input 잘못되었을 때 예외처리
except :
    print("잘못 입력하셨습니다. 예시대로 입력해주세요.")