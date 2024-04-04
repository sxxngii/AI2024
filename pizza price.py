print("어서오세요 주문 도와드릴게요!")

print("어서오세요")
size = input("피자 사이즈를 선택해주세요! S, M, L :")

if size == "S":
    price = 15000
    print("15000원입니다!")

elif size == "M":
    price = 20000
    print("20000원입니다!")

else:
    price = 30000
    print("30000원입니다!")

toping_1 = input("치즈 추가하시겠어요? (추가비용: 3000원) Y/N: ")

if toping_1 == "Y":
    price += 3000
    print("감사합니다!")

else:
    print("알겠습니다")

toping_2 = input("페퍼로니 추가하시겠어요? (추가비용: 2000원) Y/N: ")

if toping_2 == "Y":
    price += 2000
    print("감사합니다!")

else:
    print("알겠습니다")

print(f"지불하실 총 금액은 {price}원 입니다")