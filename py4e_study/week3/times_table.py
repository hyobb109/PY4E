#구구단
def gugudan(n):
    for i in range(10) :
        # 값이 50 넘어가면 반복문 탈출
        if n * i > 50 :
            break
        # 홀수번째만 출력
        if i % 2 == 1 :
            print(n, 'X', i, '=', n * i)
# 메인함수
def main():
    try:
        number = int(input("몇 단?: "))
        if number >= 1 and number <= 9 :
            print(number, '단')
            gugudan(number)
        else :
            print('1 ~ 9 사이의 숫자만 입력해주세요.')
    except:
        print('잘못 입력하셨습니다.')
        
if __name__ == "__main__":
    main()
