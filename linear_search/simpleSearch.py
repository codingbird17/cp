#  https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/simple-search-4/
n=int(input())
l=list(map(int, input().split()))
k=int(input())
for i in range(n):
    if l[i]==k:
        break
print(i)
