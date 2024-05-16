import random

count = 0
point = 0
tryagain = True

def game():
    att = int(input("how many exampls do you want?: "))
    for i in range(0, att):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        sign = random.choice(["+", "-", "*", "/"])
        if sign == "+":
            answer = num1 + num2
        elif sign == "-":
            answer = num1 - num2
        elif sign == "*":
            answer = num1 * num2
        else:
            answer = num1 / num2
        print(num1, sign, num2, "=?")
        answer2 = int(input("what does this equal?: "))
        if answer2 == answer:
            print("right, +1 point")
            count = point + 1
        else:
            print("incorrect")
    print("the game is over, you have a", count, "points for", att, "attempts")
    print()

while tryagain == True:
    print("1) math game")
    print("2) quit")
    print()
    print("welcome to the math game from W4vING2")
    ans = int(input("choose the number: "))
    if ans == 1:
        game()
    elif ans == 2:
        tryagain = False
    else:
        print("incorrect number")
        

