# 자릿수 구분해주기 위해서 f"{1000:,}" 사용 가능
# 정답 예시 코드 참고함
def make_comma(num) :
    num = str(num)
    # 몇자리 수인지 계산
    digits = len(num)
    # 3자리 수 이하면 바로 리턴
    if digits <= 3:
        return (num)
    # 필요한 쉼표 수 계산
    commas = digits // 3
    if digits % 3 == 0 :
        commas -= 1
    # 결과 담을 변수 선언
    res = ""
    # num[-1]은 뒤에서 첫 번째 인덱스 가리킴
    n = -1
    #print(num[n])
    while commas > 0 :
        res = num[n] + res
        # 3자리마다 쉼표 찍고 쉼표 수 줄임
        if n % 3 == 0 :
            res = ',' + res
            commas -= 1
        n -= 1
    # 남은 앞의 숫자 더해줌
    res = num[:n+1] + res
    return (res)    
    
def main() :
    try :
        num = int(input("숫자를 입력하세요: "))
    except:
        print("잘못 입력하셨습니다")
        quit()
    res = make_comma(num)
    print(res)

    
if __name__ == "__main__" :
    main()

