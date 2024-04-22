import random

streak = 0
list_coinFlips = []
check = 0
def coinFlip(my_list):
    flip = random.randint(0,1)
    match flip:
        case 0: my_list.append("H")
        case 1: my_list.append("T")
    

for i in range(1001):
    coinFlip(list_coinFlips)

for i in range(1000):
    
    if list_coinFlips[i] == list_coinFlips[i+1]:
        check +=1
        print(i)
        if check == 6:
            print("Streak")
            streak+=1
            check=0
    else:
        check = 0

print("AAAAAAA = " + str(streak))
print('Chance of streak: %s%%' % (streak / 1000))        