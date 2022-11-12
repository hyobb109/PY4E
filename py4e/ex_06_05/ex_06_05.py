str = 'X-DSPM-Confidence: 0.8475'

ipos = str.find(':')
# print(ipos)
piece = str[ipos+2:]
# print(piece)
# print(piece + 42.0)
value = float(piece)
print(value)
# print(value + 42.0)

# words = 'Connect Foundation'

# if 'F' in words:
#     words.lower()
#     words[7] = '&'

# TypeError: 'str' object does not support item assignment
# 문자열을 대체하려면 list 형태로 바꾸거나 replace() 사용해야함


# else:
#     print(words)
# print(words)