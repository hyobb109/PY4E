def grader(score) :
    if 95 <= score and score <= 100 :
        return("A+")
    elif 90 <= score and score <= 94 :
        return("A")
    elif 85 <= score and score <= 89 :
        return("B+")
    elif 80 <= score and score <= 84 :
        return("B")
    elif 75 <= score and score <= 79 :
        return("C+")
    elif 70 <= score and score <= 74 :
        return("C")
    elif 65 <= score and score <= 69 :
        return("D+")
    elif 60 <= score and score <= 64 :
        return("D")
    elif 0 <= score and score < 60 :
        return("F")
    # 범위를 벗어나는 점수는 에러 메시지
    else :
        return("Error!")

try :
    #공백을 기준으로 이름과 점수 입력 받음
    name, score = input("학생 이름과 점수를 입력해주세요. 예시) 이호창 99\n").split()
    score = int(score)
    print("학생이름 :", name)
    print("점수 : %d점" %(score))
    print("학점 :", grader(score))
# input 잘못되었을 때 예외처리
except :
    print("잘못 입력하셨습니다. 예시대로 입력해주세요.")