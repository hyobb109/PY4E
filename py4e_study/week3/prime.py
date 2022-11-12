# 소수 판별 함수
def is_prime(n):
    # 1은 소수가 아님
    if n < 2:
        return 0
    # 2 ~ (n-1)까지 나눴을 때 나머지가 0이면 소수
    for i in range (2, n):
        if n % i == 0:
            return 0
    return 1

def count_prime_numbers(n, m):
    numbers = [i for i in range(n, m + 1)]
    count = 0
    for i in numbers:
        if is_prime(i):
            #print(i,'는 소수')
            count += 1
    return count

def main():
    try:
        n = int(input('첫번째 수 입력: '))
        m = int(input('두번째 수 입력: '))
        print('소수 개수', count_prime_numbers(n, m))
    except:
        print('잘못입력했습니다')

if __name__== "__main__":
    main()