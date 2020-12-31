#section02-1
#파이썬 기초 코딩
#print 구문의 이해
print("hello python")
print('''hello''')

#separator 옵션 사용
print("T","E","S","T",sep="")
print('niceman','google.com',sep='@')

#end 옵션 사용
print('welcome to',end='\n')
print('the black paradise',end='\n')

#format 사용
print('{0} and {1}'.format('You','Me'))

#format말고 c언어처럼
print("%s's favorite number is %d" % ('haein',7))

print('test1:%5d, price: %4.2f' %(776,6534.776))
print('test1:{0:5d}, price: {1:4.2f}'.format(776,6534.345))
print('test1:{a:5d}, price: {b:4.2f}'.format(a=77666, b=6534.3333))

#escape 코드
print("'you'")
print('\'you\'')
print("""'you'""")
print('\t\t\ttest')