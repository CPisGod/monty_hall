import random

n = int(input(">>"))
def game(switch, n):
    win = 0
    for _ in range(n):
        car = random.randint(0,2)
        choose = random.randint(0,2)
        chosen = [i for i in range(3) if i != car and i != choose]
        opens = random.choice(chosen)
        if switch:
            choose = next(i for i in range(3) if i != opens and i != choose)
        
        if choose == car:
            win += 1
    return win/n
yes = game(True, n)
no = game(False, n)

print(f'바꿀 때 승률 : {yes}')
print(f'바꾸지 않을 때 승률 : {no}')
