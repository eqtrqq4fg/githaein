# 리스트(순서있음, 중복허용, 수정가능, 삭제가능)
a = []
b= list()
c = [1,2,3,4]
d=[10,100,'pen','banana','ornage']
e=[10,100,[10,100]]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])

#슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c+d)
print(c*3)
print(str(c[0])+'hi')

# 리스트 수정, 삭제
c[0]=77
print(c)
c[1:2]=[100,1000,10000]#슬라이스 처리를 하면 원소들이 들어감
print(c)
c[1]=['a','b','c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()

# 리스트 함수
y=[5,2,3,1,4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.insert(2,7)
print(y)
y.remove(2)
#del은 인덱스를 지우지만 remove는 값을 지움
print(y)
y.pop()
print(y)#맨 나중의 원소를 지움
ex=[88,77]
y.extend(ex)#append는 리스트 자체를 원소로 넣음
print(y)

# 튜플(순서있음, 중복허용, 수정/삭제 불가능)
# 콤마로 끝내기도 함

tuple=(10,100,('a','b','c'))

print(tuple[2])
print(tuple[2][1])
print(tuple[2][0:2])

print(tuple*2)

# 튜플 함수
z=(5,2,1,3,4)
print(3 in z)
print(z.index(3))#3에 있는 인덱스값 반환
print(z.count(1))#1이 몇개 있나요


