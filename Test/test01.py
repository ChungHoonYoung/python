
# #실습문제 n+nn+nnn 만들기
# n = input("정수 값 입력 : ")
# tot = int(n) + int(n*2) + int(n*3)
# print(tot)

# #실습문제 동전으로 교환할 급액을 입력하세요.
# userInput = int(input("동전으로 교환할 금액을 입력 :"))
# coin500 = userInput//500
# coin100 = (userInput-coin500*500)//100
# coin50 = (userInput-coin500*500 - coin100*100)//50
# coin10 = (userInput-coin500*500 - coin100*100 - coin50*50)//10
# coin1 = (userInput-coin500*500 - coin100*100 - coin50*50 - coin10*10)//1
# print("오백원짜리 =>", coin500, "개")
# print("백원짜리   =>", coin100, "개")
# print("오십원짜리 =>", coin50, "개")
# print("십원짜리   =>", coin10, "개")
# print("일원짜리   =>", coin1, "개")

# #실습문제 앱의 평점을 출력하고, 평점의 평균을 구하시오.
# #문제코드
# # app1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
# # app2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
# # app3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.0]
# # rating_sum = 0
# # #코드작성하기-------------
# # #------------------------
# # print("rating average:", rating_avg)

# app1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
# app2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
# app3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.0]
# rating_avg = (app1[4]+app2[4]+app3[4])/3
# print(app1[0], 'rating :', app1[4])
# print(app2[0], 'rating :', app2[4])
# print(app3[0], 'rating :', app3[4])
# print("rating average : ", rating_avg)

# #실습문제 나이가 10살 이상이고, 키가 110cm이상이면 놀이기구 탑승 가능
# #        사용자의 나이와 키를 입력 받아 탑승 가능 여부 확인 

# age = int(input("나이 : "))
# height = int(input("키 : "))
# if age >= 10 and height >= 110 :
#     print("놀이기구를 탈 수 있습니다.")
# else :
#     print("놀이기구를 탈 수 없습니다.")

# #실습문제 국립공원입장권 발급 프로그램
# # 기본 입장료 3,000원
# # 65세 이상 7세 이하는 무료
# # 8~18세는 청소년 요금 1,000원
# # 나이를 입력받아 입장료 출력

# age = int(input("나이를 입력 :"))

# if age <= 7 or age >= 65 :
#     print("입장료는 무료입니다.")
# elif 8 <= age <= 18 :
#     print("입장료는 1,000원입니다.")
# else :
#     print("입장료는 6,000원입니다.")


# #실습문제 금액에 따른 할인율 계산
# # 물건 구매가를 입력 받고, 금액에 따른 할인율을 계산하여, 구매가, 할인율, 할인금액, 지불금액을 출력
# # 1만원 이상 5만원 미만 5% 할인
# # 5만원 이상 10만원 미만 7.5% 할인
# # 10만원 이상 10% 할인

# price = int(input("구매가를 입력 :"))
# if 10000 <= price < 50000 :
#     sale = 5
# elif 50000 <= price < 100000 :
#     sale = 7.5
# elif 100000 <= price :
#     sale = 10
# salePrice = price*sale/100
# payment = price - salePrice
# print("구매가 : ", price, '원')
# print("할인율 : ", sale, '%')
# print("할인 금액 : ", salePrice, '원')
# print("지불 금액 : ", payment, '원')



# #실습문제 비만도 구하기
# # 사용자의 이름, 키 몸무게를 입력 받아 BMI를 계산한 후 출력
# # 18.5 미만 저체중, 18.5~22.9 정상, 23.0~24.9 과체중, 25.0~29.9 비만1단계, 30.0~39.9 비만2단계, 40.0이상 비만 3단계
# # BMI = 몸무게 / 키  ///  적정체중 = 21 * 키
# name = input("이름을 입력 : ")
# height = int(input("키를 입력 : "))
# weight  = int(input("몸무게를 입력 : "))
# bmi = weight/(height/100)**2
# normalWeight = 21*(height/100)**2

# if bmi < 18.5 :
#     fat = "저체중"
# elif 18.5 <= bmi < 22.9 :
#     fat = "정상"
# elif 23.0 <= bmi < 24.9 :
#     fat = "과체중"
# elif 25.0 <= bmi < 29.9 :
#     fat = "비만1단계"
# elif 30.0 <= bmi < 39.9 :
#     fat = "비만2단계"
# elif 40.0 <= bmi :
#     fat = "비만3단계"

# print("{}님의 BMI는 {:.2f}% 이며, {}입니다.".format(name, bmi, fat))
# print("{}님의 적정체중은 {:.2f}kg 입니다.".format(name, normalWeight))
