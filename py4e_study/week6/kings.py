def king(korea, chosun) :
    # 문자열을 , 기준으로 리스트로 변경
    korea = korea.split(",")
    chosun = chosun.split(",")
    
    di = dict()
    # 고려 왕 딕셔너리에 저장
    for king in korea :
        di[king] = di.get(king, 0) + 1
    
    # 조선 왕 딕셔너리에 저장
    for king in chosun :
        di[king] = di.get(king, 0) + 1
    
    cnt = 0
    for k, v in di.items():
        # value가 2 이상이면 출력하고 카운트
        if v > 1 :
            print('조선과 고려에 모두 있는 왕 이름:', k)
            cnt = cnt + 1
        
    print('조선과 고려에 모두 있는 왕 이름은 총 %i개 입니다'%(cnt))

def main() :
    korea = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
    chosun = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"
    king(korea, chosun)
    
if __name__ == "__main__" :
    main()