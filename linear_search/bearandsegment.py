# https://www.codechef.com/problems/SEGM01

for _ in range(int(input())):
    s=input()
    n=len(s)
    m=i=0
    ans=1
    
    while i<n:
        if s[i]=='1':
            if m==0:
                m=1
                while i+1<n and s[i+1]=='1':
                    i+=1
            elif m==1:
                ans=0
                break
        i+=1
    if '1' not in s:
        ans=0
    if ans:
        print("YES")
    else:
        print("NO")
