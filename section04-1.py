# 데이터 타입

v_str1="niceman"
v_bool=True
v_str2="goodboy"
v_float=10.3
v_int=7
v_dict={"name":"kim",
        "age":25}
v_tuple=3,5,7
v_set={7,8,9}
v_list=[3,5,7]

print(type(v_tuple))
print(type(v_set))
print(type(v_dict))

i1 = 39
i2 = 939
big_int1 = 999999999999999999
big_int2 = 777777777777777777
f1 = 1.234
f2 = 3.789

print(i1+big_int2)
print(f1+f2)

a =5.
b = 4
result=a+b
print(result)

# 형변환
# int, float, complex(복소수)

print(int(result))
print(complex(False))

# 수치연산함수
print(abs(-7))
n, m = divmod(100 ,8)
print(n,m)

import math

print(math.ceil(5.1))
print(math.floor(3.874))