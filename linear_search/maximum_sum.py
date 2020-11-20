# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/maximum-sum-4-f8d12458/description/

N=int(input())
l=list(map(int, input().split()))
m=[]
ans=0
for i in l:
    if i>=0:
        m.append(i)
for i in m:
    ans+=i
if ans==0:
        print(max(l),1,sep=" ")
else: 
        print(ans,len(m),sep=" ")
