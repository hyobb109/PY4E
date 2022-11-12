def check_id(x):
    # 길이가 14가 아니면 잘못된 번호
    if len(x) != 14 :
        return (False)
    # -로 구분되지 않으면 잘못된 번호
    if x[6] != '-' :
        return (False)
    month = int(x[2:4])
    # 출생월이 잘못되었을 때 
    # 날짜는 어차피 출력되지 않아서 따로 처리하지 않았습니다
    if month < 1 or month > 12 :
        return (False)
    year = int(x[:2])
    # 00 ~ 21 년생 이면 질문
    if year >= 0 and year <= 21 :
        birth = input('2000년 이후 출생자입니까? 맞으면 o 아니면 x: ')
        # 2000년 이전 출생 뒷자리는 1 또는 2
        if birth == 'x' and not (x[7] == '1' or x[7] == '2'):
            return (False)
        # 2000년 이후 출생자 뒷자리는 3 또는 4
        if birth == 'o' and not (x[7] == '3' or x[7] == '4'):
            return (False)
    if x[7] == '1' or x[7] == '3':
        gender = '남자'
    elif x[7] == '2' or x[7] == '4':
        gender = '여자'
    # 숫자 앞에 0까지 출력하기 위해 변수 새로 저장
    year = x[:2]
    month = x[2:4]
    print('%s년 %s월 %s'%(year, month, gender))

def main():
    x = input("주민등록번호를 입력해주세요: ")
    id = check_id(x)
    if id == False :
        print("잘못된 번호입니다.")
    
if __name__ == "__main__" :
    main()