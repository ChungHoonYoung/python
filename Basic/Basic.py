
# # 변수

# "사당", "신도림", "인천공항"
# station = "사당"
# print(f'{station}행 열차가 들어오고 있습니다.')



# # 랜덤함수

# from random import *
# print(random())
# print(int(random()*10+1))
# print(randrange(1,46))

# # 로또
# print(randint(1,45), randint(1,45), randint(1,45), randint(1,45), randint(1,45), randint(1,45))

# from random import *
# print('오프라인 스터디 모임 날짜는 매월', randint(4,28),'일로 선정되었습니다.')



# # 리스트 함수

# movieRank = ['닥터스트레인지', '어벤져스', '럭키']
# print(movieRank)
# movieRank.append('배트맨') #리스트 추가
# print(movieRank)
# movieRank.insert(1,'범죄도시') # 리스트 삽입
# print(movieRank)
# del movieRank[4] # 리스트 삭제
# print(movieRank)

# # 리스트 결합
# lang1 = ['C', 'C++', 'JAVA']
# lang2 = ['Python', 'Go', 'C#']
# langs = lang1 + lang2
# print(langs)

# # 리스트 함수 + max(), min()

# num = [ 1, 2, 3, 46, 8, 98 ]
# print('max :',max(num), 'min :',min(num))

# num = [ 'apple', 'gorilla', 'zoo', 'lang' ] #알파벳 역순으로 max ~ min
# print('max :',max(num), 'min :',min(num))

# num = [ 1, 'apple', 2, 3, 'gorilla', 46, 8, 'lang', 98 ]
# print(len(num)) # num의 리스트 갯수

# num = [ 1, 3, 5, 11, 34, 2, 52 ] #리스트의 평균
# print(round(sum(num)/len(num),2))
# avg = sum(num)/len(num)
# print(round(avg, 2))


# # 슬라이싱
# jumin = [9,9,0,1,2,0,1,2,3,4,5,6,7]
# print('성별 : ', jumin[6:7])
# print('연 : ', jumin[0:2])
# print('월 : ', jumin[2:4])
# print('일 : ', jumin[4:6])
# print('생년월일 : ', jumin[:6])
# print('뒤 7자리 : ', jumin[6:])
# print('뒤 7자리(뒤에서부터) : ', jumin[-7:])

# price = ['20180728', 100, 130, 140, 150, 160, 170 ]
# print(price[1:])

# num = [1,2,3,4,5,6,7,8,9,10]
# print(num[::2]) #홀수 출력
# print(num[1::2]) #짝수 출력
# print(num[::-1]) #역순 출력


# # join 메서드
# corp = ['KG', 'SAMSUNG', 'LG', 'SK', 'HYUNDAI']
# print(" / ".join(corp))
# print("\n".join(corp))


# # split 메서드
# string = 'KG / SAMSUNG / LG / SK / HYUNDAI'
# print(string.split(' / '))


# # 리스트 정렬
# num = [ 3, 4, 12, 1, 535, 123, 43, 241, 56 ]
# num.sort()
# print(num)
# a=sorted(num)
# print(a)


# # index 함수 사용해서 자리값 찾기
# my_str = "hello world"
# result = my_str.index("world")
# print(result) # 시작자리값

# # http://naver.com 의 비밀번호 만들어주기
# url = "http://naver.com"
# site = url.replace("http://","")
# sauce =site[:site.index(".")] 
# passward = sauce[:3]+str(len(sauce))+str(sauce.count('e'))+'!'
# print('생성된 비밀번호 :', passward)


# sub1 = 10
# sub2 = 20
# sub3 = 30
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
# subway.append("하하") #맨 뒤에 추가
# print(subway)
# subway.insert(1, "정형돈")#인덱스 1번에 추가
# print(subway)
# subway.pop() #맨 뒤에 삭제 / print에 넣을 경우 그 값을 반환하고 삭제
# print(subway)
# subway.pop()
# print(subway)
# subway.pop()
# print(subway)
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# mixList = ["조세호", 30, True]
# numList = [1, 2, 3, 4, 5]
# numList.extend(mixList)
# print(numList)


# #딕셔너리 앞이 key, 뒤가 값. key의 값만 출력 가능
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet.get(3))
# print(cabinet.get(5, "사용가능"))
# print(3 in cabinet)
# print(5 in cabinet)
# del cabinet[3]
# print(cabinet)
# cabinet[10] = "김종국"
# cabinet[5] = "송지효"
# print(cabinet)
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())
# cabinet.clear()
# print(cabinet)


# origin = {'orange':'USA', 'banana':'Mexico', 'grape':'Chille'}
# print(origin['orange'])


# # if문 
# result = 10 > 4
# if result :
#     print("this is true!")

# result = 10 - 4
# if result :
#     print("Hello World!")

# result1 = 10 > 4
# result2 = False

# result3 = result1 and result2
# if result3 :
#     print("this is AND")

# result3 = result1 or result2
# if result:
#     print("this is OR")

# num = int(input("숫자를 입력하세요. : "))
# result = num%2

# if result :
#     print("홀수 입니다.")
# else :
#     print("짝수 입니다.")


# # if문 터틀로 다각형 그리기
# import turtle

# num = int(input("3 이상의 숫자를  입력하세요. :"))

# t = turtle.Turtle()

# if 3<=num :
#     for i in range(num) :
#         t.speed(0)
#         t.forward(200/num)
#         t.left(360/num)
# else :
#     print("숫자를 잘못 입력했습니다.")
    

# # 날씨를 입력 받습니다. 비, 미세먼지
# # 비라면 우산을 챙기세요. 미세먼지라면 마스크를 챙기세요.
# # 날씨가 맑다면 준비물 필요없습니다.

# wether = input("오늘의 날씨는?(비, 미세먼지, 맑음 중에) :")

# if wether == "비" :
#     print("우산을 챙기세요.")
# elif wether == "미세먼지" :
#     print("마스크를 챙기세요.")
# elif wether == "맑음" :
#     print("준비물은 필요 없습니다.")
# else :
#     print("잘못입력하셨습니다.")




















