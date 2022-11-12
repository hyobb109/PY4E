def vip(info) :
    # , 기준으로 리스트에 저장
    tmp = info.split(",")
    # 각 회원의 정보들 리스트로 저장
    id = [tmp[i * 6] for i in range(6)]
    age = [tmp[(i * 6) + 1] for i in range(6)]
    phone = [tmp[(i * 6) + 2] for i in range(6)]
    gender = [tmp[(i * 6) + 3] for i in range(6)]
    area = [tmp[(i * 6) + 4] for i in range(6)]
    purchases = [tmp[(i * 6) + 5] for i in range(6)]
    # 구매 횟수 정수로 변환
    purchases = list(map(int, purchases))
    
    # 전화번호가 없으면 임시 번호 넣음
    for i in range(6) :
        if phone[i] == 'x' :
            phone[i] = '000-0000-0000'
            
    # 회원정보를 딕셔너리로 저장하고 출력
    cus = {'아이디': id, '나이': age, '전화번호': phone, '성별': gender, '지역': area, '구매횟수' : purchases}
    print(cus)
    
    # VIP 회원 찾아서 출력
    for i in range(6) :
        if cus['구매횟수'][i] >= 8 and cus['전화번호'][i] != '000-0000-0000' :
            print('할인 쿠폰을 받을 회원정보 아이디:',
                  cus['아이디'][i], '나이:', cus['나이'][i], '전화번호:', cus['전화번호'][i], '성별:', cus['성별'][i], '지역:', cus['지역'][i], '구매횟수:', cus['구매횟수'][i])
    
    
def main() :
    # 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
    info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
    vip(info)
    
if __name__ == '__main__' :
    main()
