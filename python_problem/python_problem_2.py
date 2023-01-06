#함수 이름은 변경 가능합니다.

##############  menu 1
def Menu1(name, score1, score2) :
    #사전에 학생 정보 저장하는 코딩
    List.append([name, score1, score2])

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    for i in range(len(List)) :
        if len(List[i]) != 4 :
            a = (List[i][1] + List[i][2]) / 2
            if a >= 90 :
                grade = "A"
            elif a >= 80 :
                grade = "B"
            elif a >= 70 :
                grade = "C"
            else :
                grade = "D"
            List[i].append(grade)

##############  menu 3
def Menu3() :
    #출력 코딩
    print("")
    print("-------------------------------")
    print("name    mid    final    grade  ")
    print("-------------------------------")
    for i in range(len(List)) :
        print("{:<5}   {:>4}   {:>4}   {:>4}".format(List[i][0], List[i][1], List[i][2], List[i][3]))

##############  menu 4
def Menu4(Name) :
    #학생 정보 삭제하는 코딩
    for i in range(len(List)) :
        if Name == List[i][0] :
            del List[i]
            print(Name,"student information is deleted")
            break

#학생 정보를 저장할 변수 초기화
List = []
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1" :
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출
        try:
            name, score1, score2 = map(str, input("Enter name mid-score final-score : ").split())
            if not (score1.isdigit() and score2.isdigit()) :
                raise Exception("Score is not positive integer!")
            for i in range(len(List)) :
              if List[i][0] == name :
                raise Exception("Already exist name!")
        except ValueError :
            print("Num of data is not 3!")
        except Exception as e :
            print(e)
        else :
            score1 = int(score1)
            score2 = int(score2)
            Menu1(name, score1, score2)

    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
        if len(List) == 0 :
                print("No student data!")
        else:
            Menu2()
            print("Grading to all students")

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출
        try:
            if len(List) == 0 :
                raise Exception("No student data!")
            for i in range(len(List)) :
                if len(List[i]) != 4 :
                  raise Exception("There is a student who didn't get grade")
        except Exception as e :
            print(e)       
        else :
            Menu3()
            
    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

        try :
            if len(List) == 0 :
                raise Exception("No Student data!")
            Name = input("Enter the name to delete : ")
            for i in range(len(List)) :
                if Name != List[i][0] :
                    raise Exception("Not exist name!")
                Menu4(Name)
                break
        except Exception as e :
            print(e)
  
    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print("Exit Program!")
        break
        
    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")
