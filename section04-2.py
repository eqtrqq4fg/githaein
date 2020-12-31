# 문자열, 문자열 연산, 슬라이싱

str1='I am a girl'
str2='niceman'
str4=str()

print(len(str1),len(str2),len(str4))

escape_str1='hello world \'for you\''
print(escape_str1)

# raw string
raw_s1=r'C'
print(raw_s1)

# 멀티라인
multi=\
"""
hello

world
"""
print(multi)

# 문자열 연산
str_o1='*'
str_o2='abc'
str_o3='def'

print(str_o1*3)
print(str_o1+str_o2)
print('a' in str_o3) #a가 문자열 안에 포함되어있니?(불리언 값으로 나옴)

# 문자열 형 변환
print(str(77)+'a')

a='niceman'
b='orange'

print(a.islower())#소문자냐
print(b.endswith('e'))#e로 끝나냐
print(a.capitalize())#첫글자 대문자로
print(a.replace('nice','good'))#나이스를 굿으로
print(list(reversed(b)))#거꾸로 해서 리스트 형태로 반환

# 슬라이싱
print(a[0:3])
print(a[3:len(a)])
print(a[:4])
print(b[0:4:2])
print(b[1:-2])#역순으로 표시
print(b[::-1])#처음부터 끝까지 뒤에서부터 시작