# section02-2

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('Hello World')

# 변수 선언
myname = 'Goodboy'

#조건문
if myname == 'Goodboy':
    print('ok')

#import pandas as pd 
#from pandas import DataFrame, Series
#df={'a':[1],'b':[2],'c':[3]}
#df2=pd.DataFrame(df)
#print(df2)

# 반복문
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = ' %(i,j),i*j)

# 변수 선언(한글)
이름 = "좋은사람"

# 출력
print(이름)

# 함수선언
def hi():
    print("hello world")
hi()

# class
class Cookie:
    pass

# 객체 생성
cookie = Cookie()
print(id(cookie))
print(dir(cookie))