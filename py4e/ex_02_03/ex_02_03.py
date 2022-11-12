hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
print("Pay:", pay)

# 1주차 미션 : 다른 값을 입력했을 때의 예외처리
# while True:
#     try:
#         age = int(input('한국 나이: '))
#         if age < 1:
#             print('잘못 입력하셨습니다')
#         else:
#             birth = int(input('생일이 지났습니까? 맞으면 0 아니면 -1: '))
#             if birth != 0 and birth != -1:
#                 print('0 이나 -1만 입력하세요')
#             else:
#                 x = age + birth - 1
#                 print('미국 나이:', x)
#                 break
#     except ValueError:
#         print('숫자만 입력하세요')
