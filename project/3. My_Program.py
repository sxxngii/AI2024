scissors = '''
    _______
---'    ____)____
            ______)
        __________)
        (____)
---.__(___)
'''

rock = '''
    _______
---'    ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
            ______)
            _______)
            _______)
---.__________)
'''
img_hands = [scissors, rock, paper]

import random
import qrcode

# 튜토리얼
print("\n어서 오세요! 인생은 한! 방! 로또 판매점입니다~!\n")
print("이번에 저희 매점에서 소소한 이벤트 진행 중인데 들어보시겠어요?\n")
print("우선 상품은 저번 회 차 1등 로또이고 저희가 준비한 세 단계를 연속으로 통과하셔야 합니다!\n")

"""
Purchases = (input("로또를 구매하시겠습니까? Y(1) or N(0): ")).upper()

if Purchases == 'Y':
    print("")
"""



# 이벤트 참여 여부
Purchases = int((input("이벤트에 참여하시겠어요? Y(1) or N(0): ")))

if Purchases > 1 or Purchases < 0: 
    print("\n잘못된 숫자를 입력했습니다!\n")
    quit()

elif Purchases == 1:
    print("")

else:
    print("\n다음에 또 방문해 주세요~!\n")
    quit()



# 첫 번쨰 단계
print("첫 번째 단계: 가위바위보 중에서 저와 같은 걸 내주시면 됩니다!\n")

User = int(input("선택해 주세요! 가위(0), 바위(1), 보(2): "))

if User >=3 or User < 0: 
    print("\n잘못된 숫자를 입력했습니다!\n")
    quit()
  
else:
    print(f"\n나의 선택은: ")
    print(img_hands[User])

    Lotto = random.randint(0, 2)
    print(f"\n컴퓨터의 선택은: ")
    print(img_hands[Lotto])



# 가위바위보 족보
if User > Lotto:
    print("\n이벤트 탈락하셨습니다!\n")
    quit()

elif User < Lotto:
    print("\n이벤트 탈락하셨습니다!\n")
    quit()

else:
    print("\n다음 단계로 넘어가주세요!\n")



# 두 번째 단계
print("두 번째 단계: 로또가 든 3개의 상자 중에서 한 상자를 선택해주세요!")

Sub_Choice = int(input("\n1, 2, 3번 중 번호 하나를 선택해주세요!: "))

Main_Choice = random.randint(1, 3)

if Sub_Choice > 3 or Sub_Choice < 0:
    print("\n잘못된 숫자를 입력했습니다!\n")
    quit()

elif Main_Choice == Sub_Choice:
    print("\n다음 단계로 넘어가주세요!\n")

else:
    print("\n꽝 입니다! 이벤트 탈락하셨습니다!\n")
    quit()



# 세 번째 단계
print("세 번째 단계: 3개의 열쇠 중에서 상자와 맞을거같은 열쇠를 하나 선택해주세요!\n")

Sub_Key = int(input("1, 2, 3번 중 번호 하나를 선택해주세요!: "))

Main_Key = random.randint(1, 3)

if Main_Key > 3 or Main_Key < 0:
    print("\n잘못된 숫자를 입력했습니다!\n")
    quit()

elif Sub_Key == Main_Key:
    print("")

else:
    print("\n꽝 입니다! 이벤트 탈락 하셨습니다!\n")
    quit()



# 복권 번호 생성
Number = random.sample(range(1, 47), 6)
Number.sort()

# 당첨 결과 출력
if Main_Choice == Sub_Choice and Main_Key == Sub_Key:
    print("축하합니다! 1등 복권에 당첨되셨습니다.\n")
    print("복권 번호는 QR 코드를 통해서 전달됩니다.")
    
    # qrcode 생성
    data = "오늘의 행운의 번호는" + str(Number) + "입니다!"

    img = qrcode.make(data)

    img.save("qrcode.png")

else: 
    print("꽝 입니다! 이벤트 탈락 하셨습니다!!\n") 
