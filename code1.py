import random

num_1 = random.randint(1,46)

num_2 = random.randint(1,46)

num_3 = random.randint(1,46)

num_4 = random.randint(1,46)

num_5 = random.randint(1,46)

num_6 = random.randint(1,46)

total_num = num_1, num_2, num_3, num_4, num_5, num_6

if num_1 != num_2:
    print("")
    if num_2 != num_3:
        print("")
        if num_3 != num_4:
            print("")
            if num_4 != num_5:
                print("")
                if num_5 != num_6:
                    print(f"오늘의 행운의 번호는 {total_num} 입니다!")

else: 
    print(f"오늘의 행운의 번호는 {total_num} 입니다!")
    print("번호가 중복되었습니다. 다시 생성해주세요!")















