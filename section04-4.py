# 딕셔너리(순서없음, 중복안됨, 수정 가능, 삭제 가능)

a={'name':'kim','phone':'010-7777-7777','birth':870214}
print(a)
b={0:'python'}
c={'arr':[1,2,3,4,5]}

print(a['name'])
print(a.get('name'))
print(a.get('address'))#값이 있는지 조회하는 용도

# 딕셔너리 추가
a['address']='Seoul'
print(a)
a['rank']=(1,2,3)
print(a)

# item = key+value
print(a.keys())
temp=list(a.keys())
print(temp[1:3])

print(a.items())

# 집합(sets)(순서없음, 중복안됨)
a=set()
b=set([1,2,3,4])
c=set([1,4,5,6,6])
print(c)
t=tuple(b)
print(t)
l=list(b)
print(l)

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
print(s1.intersection(s2))#교집합
print(s1|s2)#합집합
print(s1.union(s2))
print(s1-s2)#차집합
print(s1.difference(s2))

#추가&제거
s3=set([7,8,10,15])
s3.add(18)
print(s3)

s3.remove(15)
print(s3)

