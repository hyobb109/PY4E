def count_word(text, word) :
    # text변수 내용을 텍스트 파일로 저장
    file = open("sample.txt", "w")
    file.write(text)
    file.close()
    # 개수 카운트하는 함수 사용
    count = text.count(word)
    return (count)
    
def main():
    # 쌍따옴표 3개 쓰면 개행문자 포함 모두 다 문자로 취급
    text = """왜들 그리 다운돼있어?
뭐가 문제야 Say something
분위기가 겁나 싸해
요새는 이런 게 유행인가
왜들 그리 재미없어?
아 그건 나도 마찬가지
Tell me what I got to do
급한 대로 블루투스 켜
아무 노래나 일단 틀어
아무거나 신나는 걸로
아무렇게나 춤춰
아무렇지 않아 보이게
아무 생각 하기 싫어
아무개로 살래 잠시
I'm sick and tired of my everyday"""
    word = input("찾을 문자를 입력하세요: ")
    res = count_word(text, word)
    print(res)
    
if __name__ == "__main__" :
    main()