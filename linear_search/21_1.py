# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/rest-in-peace-21-1/description/

y="The streak lives still in our heart!"
no="The streak is broken!"
for _ in range(int(input())):
    n=int(input())
    if n%21==0:
        print(no)
    else:
        if '21' in str(n):
            print(no)
        else:
            print(y)
