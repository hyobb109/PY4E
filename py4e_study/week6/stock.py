
def stock_profit(stocks, sells) :
    tmp = list()
    # sells 인덱스
    i = 0 
    for s in stocks :
        # 종목별 수익률 계산
        rate = (sells[i] - stocks[s]['p']) / stocks[s]['p'] * 100
        # 소숫점 둘째짜리까지만
        rate = f"{rate:.3}"
        # 튜플에 수익률, 종목 저장
        res  = (rate, s)
        # 리스트에 튜플 저장
        tmp.append(res)
        # sells 인덱스 한칸씩 증가
        i = i + 1
    
    print('정렬 전:', tmp)
    # 수익률 큰 순서대로 리스트 정렬 

    tmp = sorted(tmp, key = lambda x : x[0], reverse = True)
    # print('정렬 후:', tmp)
    for rate, stock in tmp :
        print(stock, '수익률:', rate)
    

def main() :
    # 종목별 구매 수량, 매수가 중첩 딕셔너리로 저장
    stocks = {
        '삼성전자': {
            'q' : 10, 
            'p' : 85000
            }, 
        '카카오':{
            'q': 15,
            'p': 130000
        },
        'LG화학': {
            'q': 3,
            'p': 820000
        },
        'NAVER': {
            'q': 5,
            'p': 420000
        },
    }
    # 판매가는 리스트에 저장
    sells = [82000, 160000, 835000, 410000]
    stock_profit(stocks, sells)


if __name__ == "__main__" :
    main()