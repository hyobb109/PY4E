def find_even_number(n, m):
    numbers = [i for i in range(n, m + 1)]
    # 리스트 원소 개수 셈
    count = len(numbers)
    mid = int((n + m) / 2)
    for i in numbers:
        if i % 2 == 0:
            print(i, '짝수')
        # count가 홀수면 중앙값 존재
        if count % 2 == 1 and i == mid:
            print(mid, '중앙값')
        
def main():
    try:
        n = int(input("첫번째 수 입력: "))
        m = int(input("첫번째 수 입력: "))
        find_even_number(n, m)
    except:
        print("잘못 입력했습니다.")

if __name__ == "__main__":
    main()
