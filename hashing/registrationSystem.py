# https://codeforces.com/problemset/problem/4/C 

n=int(input())
l=dict()
for i in range(n):
    s=input()
    if s in l:
        print(s+str(l[s]))
        l[s]+=1
    else:
        print('OK')
        l[s]=1
