# 주소록 만들기

def print_menu () :
    print("*** 전화번호부 ***\n")
    print("1. 추가하기")
    print("2. 수정하기")
    print("3. 삭제하기")
    print("4. 목록보기")
    print("5. 종료하기")
    print("--------------")

def addBook () :
    name = input("추가하실 이름을 입력하세요. : ")
    number = input("추가하실 번호를(-포함) 입력하세요. : ")
    phoneBook[name] = number

def modiBook () :
    name = input("수정하실 이름을 입력하시오.")
    if name in phoneBook :
        modi_name = input("수정하려는 이름을 입력하시오.")
        modi_number = input("수정하려는 번호 입력하시오.")
        name = modi_name
        phoneBook[modi_name] = modi_number
    else :
        print("수정하실 이름이 없습니다.")

def delBook () :
    name = input("삭제하실 이름을 입력하시오.")
    if name in phoneBook :    
        del phoneBook[name]
    else :
        print("삭제하실 이름이 없습니다.")

def callBook () :
    if len(phoneBook) == 0 :
        print("전화번호부가 비었습니다.")
    else :
        for a in phoneBook : 
            print(f"{a} : {phoneBook[a]}")

print_menu()

phoneBook = {}

while True :

    n = int(input("메뉴를 선택하세요.(숫자를 입력)"))

    if n == 1 :
        addBook ()
        print_menu()

    elif n == 2:
        modiBook ()
        print_menu()

    elif n == 3 :
        delBook ()
        print_menu()

    elif n == 4 :
        callBook ()
        print_menu()

    elif n == 5 :
        print("전화번호부를 종료합니다.")
        break

    else :
        print("잘못된 번호를 입력하셨습니다.")
        print_menu()