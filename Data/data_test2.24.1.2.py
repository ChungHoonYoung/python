'''

#숫자형int float

a = 5
b = 7
#a, b = 5, 7

#연산자
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

#몫//, 나머지%
print(a//b)
print(a%b)

# 연산 연습
x = -1
y = 3
print((-y)**3+(2*x**2*y))

a = 15
a+= 3
print(a)
a-=4
print(a)
a*=5
print(a)
a/=3
print(a)
a**=3
print(a)

#연산 _ 문자열
a = 'good'
b = 'morning'
print(a + b)
print(a*3)

x, y = 10, '20'
print(x, y)
# print(x + y) : 문자와 숫자는 더하기 안됨
# 형 변환 후에 가능
print(x + int(y))
print(x + float(y))
print(str(x) + y) #1020 문자

print('')
print('-------------------------------------------')
print('')

#입력 input()
name = input("이름을 입력해 주세요.")
age = input("나이를 입력해 주세요.")
print(f"당신의 이름은 {name}이고, 나이는 {age}세 입니다.")

print('')


# 두 수를 입력해서 더해주는 프로그램
num1 = int(input("첫 번째 수 : "))
num2 = int(input("두 번째 수 : "))
r = num1 + num2
print(num1, '+', num2, '=', r)
print(f"{num1} + {num2} = {r}")
'''
#국어, 영어, 수학 점수를 받아서 합계와 평균을 알려주는 프로그램

num1 = int(input("국어 점수 : "))
num2 = int(input("영어 점수 : "))
num3 = int(input("수학 점수 : "))
tot = num1 + num2 + num3
avg = tot/3
# avg = round(tot/3, 2)
print(f"합계 점수는 {tot}점 입니다.")
print(f"평균 점수는 {avg:.2f}점 입니다.")





















