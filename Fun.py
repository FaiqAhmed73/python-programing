def this_function(*man):
    for m in man:
        print("hello" + m)
        
this_function("nice", "good", "young")


numbers = ["1,", "2","3","4" ]


for i in numbers:
    print("These are the numbers" + " " +i)


num = [10, 11, 12, 13, 14, 15, 16, 17]

if num[0] == 10:
    for i in num:
        print(i)
else:
    print("this is not true") 




run = True
current = 10

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 10