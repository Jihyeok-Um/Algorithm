import re
t = int(input())
for i in range(t):
    string = input()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(string)
    if (m != None and m[0] == string):
        print("YES")
    else:
        print("NO")