'''
1	2	3	4	5
5	4	3	2	1	
1	2	3	4	5
5	4	3	2	1
1	2	3	4	5
'''
n=0
for row in range(5):
    for col in range(5):
        if row%2==0:
            n=n+1
            print(n,end="   ")
        else:
            print(n,end="   ")
            n=n-1
    print()