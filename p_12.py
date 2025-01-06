'''
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9
'''

for row in range(10):
    num=0
    for col in range(5):
        if row%2==0:
            num=num+2
            print(num+0,end=" ")
        else:
            print(num+1,end=" ")
            num=num+2
    print()

