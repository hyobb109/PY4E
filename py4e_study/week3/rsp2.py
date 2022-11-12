import random

# 0, 1, 2 입력받으면 를 가위, 바위, 보로 바꿈
def change(n):
    if n == 0:
        return("가위")
    elif n == 1:
        return("바위")
    elif n == 2:
        return("보")
    else:
        return(error)

def rsp(my):
    # 가위, 바위, 보 입력 받으면 출력하고 숫자로 바꿈
    if my == '가위':
        print("나: 가위")
        my = 0
    elif my == '바위':
        print("나: 바위")
        my = 1
    elif my == '보':
        print("나: 보")
        my = 2
    else:
        my = int(my)
        print("나:", change(my))
    computer = random.randint(0, 2)
    print("컴퓨터:", change(computer))
    return(my - computer)

def play_game():
    game = int(input("몇 판 진행하시겠습니까? 숫자만 입력해주세요. "))
    win = 0
    lose = 0
    draw = 0
    for i in range(game):
        my = input("가위(0) 바위(1) 보(2) ")
        print("-----", i+1, "번째 판-----")
        res = rsp(my)
        if res == 0:
            print("비겼습니다!")
            draw += 1
        elif res > 0:
            print("나의 승리!")
            win += 1
        else:
            print("컴퓨터의 승리!")
            lose += 1
    print("----- 게임 결과 -----")
    print("나의 전적 : %d승 %d무 %d패" % (win, draw, lose))
    print("컴퓨터의 전적 : %d승 %d무 %d패" % (lose, draw, win))

def main():
    while True:
        try:
            play_game()
            break
        except:
            print("잘못 입력하셨습니다. 처음부터 다시 입력해주세요.")
            
if __name__ == "__main__":
    main()