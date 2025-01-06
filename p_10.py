'''
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
'''

for row in range(10):
    num=1
    for col in range(10):
        if num>5:
            num=1
        if row<=10:
            print(num,end=" ")
            num=num+1
    print()