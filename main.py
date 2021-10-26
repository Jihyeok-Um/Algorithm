import re
string = input()
p = re.compile('(100+1+|01)+')
m = p.match(string)
if (m != None and m[0] == string):
    print(m[0])
    print("SUBMARINE")
else:
    print(m[0])
    print("NOISE")