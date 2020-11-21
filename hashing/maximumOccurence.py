# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/maximum-occurrence-9/description/

s=input()
#s="".join(s.split())
d=dict()
n=len(s)
for i in range(n):
    if ord(s[i]) in d:
        d[ord(s[i])]+=1
    else:
        d[ord(s[i])]=1
a=127
b=0
for items, values in d.items():
    if values>b:
        a=items
        b=values
    if values==b and items<a:
        a=items
        b=values
        
print(chr(a),b,sep=" ")
