# triple x game python

import random

def agent_geek(rand_sum,rand_prod):
    print("* agent geek *")
    print("* summation of security code is:",rand_sum,"*")
    print("* accumulated value of security code is:",rand_prod,"*")

def play_game():
    rand1 = random.randint(1,level * 4)
    rand2 = random.randint(1,level * 4)
    rand3 = random.randint(1,level * 4)

    rand_sum = rand1 + rand2 + rand3
    rand_prod = rand1 * rand2 * rand3

    agent_geek(rand_sum,rand_prod)
    # print(rand1,rand2,rand3)

    num1 = int(input("- code 1: "))
    num2 = int(input("- code 2: "))
    num3 = int(input("- code 3: "))

    user_sum = num1 + num2 + num3
    user_prod = num1 * num2 * num3

    if user_sum == rand_sum and rand_prod == user_prod:
        print("\n- security code accepted server security layer",level,"hacked successfully")
        return True
    else:
        print("\n- invalid security code",lives-1,"chances left")
        return False


lives = 4
level = 1
heading = "* server break *"
intro = """You are a Hacker you have to gain access to the Umbrella Inc. servers
you have to enter a 3 digit combination code. there are 3 levels of server 
security and you only 4 Lives after that the security protocol will activate 
our own 'Agent Geek' will be there to help you"""

print(heading)
print(intro.lower())

while lives > 0:
    print()
    if play_game():
        level += 1
        if level == 4:
            print("- server hacked thankyou agent")
            break
    else:
        lives -= 1
        if lives == 0:
            print("- you are compromised game over")