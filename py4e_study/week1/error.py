# SyntaxError
# 1) unexpected EOF while parsing
# print('hello'
print('hello')

# 2) invalid syntax
# 123x = 5
# print(123x)
x123 = 5
print(x123)


# ValueError
# 1) invalid literal for int() with base 10: 'number1'
# 숫자 외 다른 문자 포함하고 있으면 정수 변환 안 됨
# print(int('number5'))
print(int(5))

# 2) invalid literal for int() with base 10: '5살'
# age = int(input('현재 나이를 입력하세요: '))
# print('내년엔', age + 1, '살 입니다')

while True:
    try:
        age = int(input('현재 나이를 입력하세요: '))
        print('내년엔', age + 1, '살 입니다')
        break
    except ValueError:
        print('숫자만 입력하세요')

# TypeError
# 1) can only concatenate str (not "int") to str
x = '5'
# print(x + 1)
# Debugging
print(int(x) + 1)


# 2) unsupported operand type(s) for -: 'str' and 'int'
# input() 함수는 '문자열'타입 반환하기 때문에 type error 발생
# age = input('현재 나이를 입력하세요: ')
# Debugging
age = int(input('현재 나이를 입력하세요: '))
print('내년엔', age + 1, '살 입니다')

# NameError: name 'hello' is not defined
# 문자열 출력 시 따옴표 사용해야 함
# print(hello)
print("hello")

# IndentationError: expected an indented block after 'if' statement
# if True:
# print('True')
if True:
	print('True')

# ZeroDivisionError: division by zero
#x = 5 / 0
# Debugging (0이 아닌 값으로 나눔)
x = 5 / 1
print(x)
