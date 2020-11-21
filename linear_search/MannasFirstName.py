# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/mannas-first-name-4/description/

for _ in range(int(input())):
    s=input()
    s1='SUVO'
    s2='SUVOJIT'
    m=s.count(s1)
    g=s.count(s2)
    print("SUVO = ",m-g,", SUVOJIT = ",g,sep="")
'''
Without using this way, problem can be done by checking every letter in this way-
a=0;
b=0;
l=strlen(arr);
for(i=0;i<=l-4;i++)
        {
            if(arr[i]=='S' && arr[i+1]=='U'&&arr[i+2]=='V'&&arr[i+3]=='O')
                a++;
        }

        for(i=0;i<=l-7;i++)
        {
            if(arr[i]=='S' && arr[i+1]=='U'&&arr[i+2]=='V'&&arr[i+3]=='O'&&arr[i+4]=='J'&& arr[i+5]=='I'&&arr[i+6]=='T')
                b++;
        }
part of C code taken from hackerrearth editorial
'''
