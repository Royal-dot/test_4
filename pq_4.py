'''
1	2	3	4	5	6
7	8	9	1	2
3	4	5	6
7	8	9	
1	2
3
'''
num=1
for row in range(6):
    for col in range(6):
        if num>9:
            num=1
        if row<=col:
            print(num,end=" ")
            num=num+1
    print()