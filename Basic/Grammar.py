# # for문 (반복문)
# marks = [90, 25, 67, 45, 80]

# number = 0 
# for mark in marks :
#     number = number +1 
#     if mark >= 60 :
#         print("%d번 학생은 합격입니다." %number)
#     else :
#         print("%d번 학생은 불합격입니다."%number)

# number = 0 
# for mark in marks :
#     number = number +1 
#     if mark < 60 :
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." %number)

# # range
# add = 0 
# for i in range(1, 11) :
#     add = add + i
# print(add)

# # 369게임 만들기
# ending = int(input("마지막 숫자 : "))

# for i in range(1, ending+1) :
#     if (i%10 == 3) or (i%10 == 6) or (i%10 == 9) :
#         print("짝")
#     else :
#         print(i)

# #반복문 사용해서 그림 그리기
# floor = int(input("몇층짜리로 만들까요? :"))
# for i in range(1, floor+1) :
#     for j in range(i) :
#         print('*', end='')
#     print()

# # 역순으로 그리기
# floor = int(input("몇층짜리로 만들까요? :"))
# for i in range(1, floor+1) :
#     for j in range(floor - i + 1) :
#         print('*', end='')
#     print()

# # 우측 정렬
# floor = int(input("몇층짜리로 만들까요? :"))
# for i in range(1, floor+1) :
#     for j in range(floor+1 - i) :
#         print(' ', end = '')
#     for j in range(i) :
#         print('*', end = '')
#     print()

# # 가운데로 그리기
# floor = int(input("몇층짜리로 만들까요? :"))
# for i in range(1, floor+1) :
#     for j in range(floor+1 - i) :
#         print(' ', end = '')
#     for j in range(i*2-1) :
#         print('*', end='')
#     print()

# # 다이아몬드 그리기
# floor = int(input("몇층짜리로 만들까요? :"))
# for i in range(1, floor+1) :
#     for j in range(floor+1 - i) :
#         print(' ', end = '')
#     for j in range(i*2-1) :
#         print('*', end='')
#     print()
# for i in range(1, floor+1) :
#     for j in range(i+1) :
#         print(' ', end = '')
#     for j in range((floor - i - 1)*2 + 1) :
#         print('*', end='')
#     print()

# # while문 (무한반복문)


# from random import *

# answer = randint(1,100)

# while answer :
#     userAnswer = int(input("1부터 100 중에서 정답은 ? :"))
#     if userAnswer > answer :
#         print("down")
#         print(userAnswer)
#     elif userAnswer < answer :
#         print("up")
#         print(userAnswer)
#     elif userAnswer == answer :
#         print("correct!")
#         break
        

# # try :, except :
# try:
#     number = int(input("10을 나눌 숫자를 입력하세요: "))
#     result = 10 / number
#     print("Result:", result)
# except ZeroDivisionError:
#     print("오류: 0으로 나눌 수 없습니다.")
# except ValueError:
#     print("오류: 유효한 정수를 입력하십시오.")

# try :
#     while True :
#         print("hello")
# except KeyboardInterrupt :
#     print("프로그램을 빠져나갑니다.")

# #미션: 타이머 작성하기
# #아두이노의 세븐세그먼트 프로그램과 연관되는 내용
# #time 모듈 사용
# #while 반복문, 숫자연산 사용
# #Ipython 설치해야함(pip install Ipython)
# #sevenSegment 모듈 같은 경로로 옮겨야 함

# import time
# from IPython.display import clear_output
# from sevenSegment import getSevSegStr

# # (!) Change this to any number of seconds:
# secondsLeft = 25

# try:
#     while secondsLeft >= 0:
#         # Clear the output cell
#         clear_output(wait=True)

#         # 남은 시간/분/초 형식으로 기록하기
#         hours = str(secondsLeft // 3600)
#         minutes = str((secondsLeft % 3600) // 60)
#         seconds = str(secondsLeft % 60)

#         # sevenSegments 모듈 사용하기
#         hDigits = getSevSegStr(hours, 2)
#         hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

#         mDigits = getSevSegStr(minutes, 2)
#         mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

#         sDigits = getSevSegStr(seconds, 2)
#         sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

#         # 남은 시간 표시하기
#         print(hTopRow + '     ' + mTopRow + '     ' + sTopRow)
#         print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
#         print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

#         if secondsLeft == 0:
#             print()
#             print('    * * * * 완료! * * * *')
#             break

#         print('\nPress Ctrl-C to quit.')

#         time.sleep(1)  # 1초 단위로 카운트 다운하기
#         secondsLeft -= 1
# except KeyboardInterrupt:
#     pass  # Ctrl-C 를 누르면 끝내기