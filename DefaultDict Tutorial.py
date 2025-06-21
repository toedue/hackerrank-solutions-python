from collections import defaultdict

n,m = list(map(int, input().split()))
a_list =[]
b_list = []

for i in range(n):
    a_list.append(input())
for i in range(m):
    b_list.append(input())

for b in b_list:
    if b in a_list:
        x= [i+1 for i,v in enumerate(a_list) if v==b]
        ss = ' '.join(map(str,x))
        print (ss)
    else:
        print("-1")