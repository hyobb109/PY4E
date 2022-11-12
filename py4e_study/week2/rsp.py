import random

# 0, 1, 2 입력받으면 를 가위, 바위, 보로 바꿈
def change(n) :
    if n == 0 :
        return("가위")
    elif n == 1 :
        return("바위")
    elif n == 2 :
        return("보")
    
#rsp = rock scissors paper
def rsp(my) :
    # 가위, 바위, 보 입력 받으면 출력하고 숫자로 바꿈
    if my == '가위' :
        print("나: 가위")
        my = 0
    elif my == '바위' :
        print("나: 바위")
        my = 1
    elif my == '보' :
        print("나: 보")
        my = 2
    else :
        my = int(my)            
        print("나:",change(my))
    computer = random.randint(0, 2)
    print("컴퓨터:", change(computer))
    # 컴퓨터와 대소 비교
    if computer > my :
        print("컴퓨터 승리!")
    elif computer < my :
        print("나의 승리!")
    else :
        print("비겼습니다!")
    
try :
    my = input("가위(0) 바위(1) 보(2) ")
    rsp(my)
# 다른 값이 들어오면 에러 메시지 출력
except :
    print("가위(0), 바위(1), 보(2)로 입력하세요")