'''
print('파이썬 기본 문법 시작!')
print("큰따옴표, 작은따옴표 사용 가능")
print("""여러줄 출력하고 싶을때
따옴표 3개쓰면
가능합니다!""")

# '낮말'은 새가 듣고, '밤말'은 쥐가 듣는다.
# 작은 따옴표가 출력되려면 큰 따옴표 안에 넣으면 된다.
print("'낮말'은 새가 듣고, '밤말'은 쥐가 듣는다.")

print('')
print('-------------------------------------------')
print('')

print('print("hello")')
print(1,2,3)
print(1+2, 2+2, 2+3)
print('1+2=', 1+2)
print(1, '1')
print(1,2,3, sep='\t')
print(1,2,3, sep=':')
print('end 옵션 테스트', end='(')
print(1,2,3, end=')')
print('')

print('')
#자기소개
print('----------------변수 선언-----------------')
print('')

name = "정훈영"
age = 33
hobby = "책 읽기"

print(type(name))
print(type(age))
print(id(name))

print('안녕하세요.\n저의 이름은 ',name,'입니다. \n만나서 반갑습니다.')
print('저의 나이는 ',age,'입니다. \n저의 취미는 ',hobby,'입니다.')

#f스트링 출력
print(f'안녕하세요.\n저의 이름은 {name}입니다. \n만나서 반갑습니다.')
print(f'저의 나이는 {age}입니다. \n저의 취미는 {hobby}입니다.')

print('')
print('-------------------------------------------')
print('')


#문자열의 인덱싱, 슬라이싱
a = "Life is too short, You need Python"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[:4])
print(a[12:17])
print(a[28:])
print(a[-6:])
print('')

b = '20240102Sunny'
year = b[:4]
month = b[4:6]
day = b[6:8]
weather = b[-5:]
print(f'오늘 날짜:{year}년 {month}월 {day}일\n날씨:{weather}')

'''

#문자열 함수 count(), len(), upper(), lower(), lstrip()
a = "  Hobby  "
print(a.count('b')) #다음의 알파벳이 몇 개 포함되어 있는가
print(a.count('h'))
print(a.count('x'))

print(len(a)) # a의 문자열 안에 몇 개의 문자가 들어가 있는가

print(a.upper()) # 대문자로 변환
print(a.lower()) # 소문자로 변환

print(a.lstrip()) # 왼쪽 빈칸 없이 정렬
print(a.rstrip()) # 오른쪽 빈칸 없이 정렬
print(a.strip()) # 빈칸 없이 정렬

# replace()

b = "Life is too short" 
print(b)
c = b.replace("Life", "Your leg") # 자리값 교체
print(c)


#split()
print(b.split()) # 리스트형으로 변환
print(b.split(':'))
c = "a:b:c:d"
print(c.split(':'))















