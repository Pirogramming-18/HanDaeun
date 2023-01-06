num = 0
start = 0

def brGame():
    while(True):
        try:
            numm = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if (not(1 <= numm <= 3)):
                raise Exception()        
        except ValueError:
            print('정수를 입력하세요')
        except Exception:
            print('1,2,3 중 하나를 입력하세요')
        else:
            break
    return numm
    
while(True):
    numm = brGame()
    
    for num in range(start, start+numm):
        print("playerA :", num+1)
        start += 1
        if (start >= 31):
            print('playerB win!')
            break
    if (start >= 31):
            break
        
    numm = brGame()

    for num in range(start, start+numm):
        print("playerB :", num+1)
        start += 1
        if (start >= 31):
            print('playerA win!')
            break
    if (start >= 31):
            break

