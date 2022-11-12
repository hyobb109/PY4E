def sales(names, records) :
    avg = list()
    # 실적 평균 계산
    for record in records :
        sum = 0
        cnt = 0
        for i in record :
            sum = sum + record[i] # 실적 합계
            cnt = cnt + 1 # 개수
        a_record = sum / cnt # 실적 평균 계산
        avg.append(a_record) # avg 리스트에 저장

    # 이름과 실적 평균 딕셔너리에 저장
    total = dict()
    i = 0
    for name in names:
        total[name] = total.get(name, avg[i])
        i = i + 1
        
    # 실적 큰 순서대로 딕셔너리 정렬
    res = sorted(total.items(), key = lambda x : x[1], reverse = True)
    
    # 등수 카운트 하기 위해 i 1로 초기화
    i = 1
    for k, v in res :
        # 보너스 대상자 조건
        if i <= 2 and v > 5 :
            print('보너스 대상자', k)
        # 면담 대상자 조건
        elif i >= 5 and v <= 3 :
            print('면담 대상자', k)
        i = i + 1
    
def main() :
    # 이름, 실적
    names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
    records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
    [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
    [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]
    sales(names, records)
    

if __name__ == '__main__' :
    main()