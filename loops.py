import random

for x in range(0, 10):
    print(x, '  ', end="")
    print('\n')

grocery_list = ['juice', 'grapes']
for y in grocery_list:
    print(y)
num_list = [[1,2,3],[10,11,12],[99,88,77]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])
#when no idea how long to loop
#while
random_num = random.randrange(0,25)
while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,30)
i = 0;
while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break
    else :
        i += 1
        continue

    i += 1
