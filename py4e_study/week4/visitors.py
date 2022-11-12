# 유효하지 않은 번호 확인하는 함수
def invalid(num):
    # 010으로 시작하지 않으면
    if num.startswith("010") == False :
        return (True)
    # 길이가 13이 아니면
    if len(num) != 13 :
        return (True)
    # '-'로 구분되지 않으면
    if num[3] != '-' and num[8] != '-' :
        return (True)
    
def wrong_guest_book(guest_book):
    # 방명록 텍스트 파일로 저장
    file = open('guests.txt', 'w')
    file.write(guest_book)
    file.close()
    file = open('guests.txt', 'r')
    for line in file :
        # 문자열 길이 제대로 구하기 위해 공백 지움
        line = line.rstrip()
        # 번호 시작 인덱스 구함
        num_pos = line.find(',') + 1
        num = line[num_pos:]
        # 쉼표 전까지는 이름
        name = line[:line.find(',')]
        if invalid(num) :
            print('잘못 쓴 사람:', name)
            print('잘못 쓴 번호:', num)
            print('')
    
def main():
    guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""
    wrong_guest_book(guest_book)


if __name__ == "__main__":
    main()
