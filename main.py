import sys
string = list(sys.stdin.readline().rstrip())
num = ""
num2 = ""
prec = ""
prec2 = ""
x = ""
i = 0
isTwo = False
while True:
    if (len(string) == i):
        break
    if string[i] == '-':
        prec = string[i]
    else:
        if string[i] != 'x':
            num += string[i]
        else:
            x = string[i]
            i += 1
            break
    i += 1
while len(string) != i:
    isTwo = True
    if string[i] == '+' or string[i] == '-':
        prec2 = string[i]
    else:
        num2 += string[i]
    i += 1

if (isTwo):
    num = int(int(num)/2)
    num2 = int(num2)
    if (num != 1 and num2 != 1 and num2 != 0):
        print(prec + str(num) + "xx" + prec2 + str(num2) + "x+W")
    elif (num2 != 1 and num == 1 and num2 != 0):
        print(prec + "xx" + prec2 + str(num2) + "x+W")
    elif (num != 1 and num2 == 1 and num2 != 0):
        print(prec + str(num) + "xx" + prec2 + "x+W")
    elif (num == 1 and num2 == 1 and num2 != 0):
        print(prec + "xx" + prec2 + "x+W")
    elif (num2 == 0 and num == 1):
        print(prec + "xx" + "+W")
    elif (num2 == 0 and num != 1):
        print(prec + str(num) + "xx" + prec2 + "W")
else:
    if (x == ""):
        num = int(num)
    else:
        num = int(int(num)/2)
    if (num != 1 and num != 0):
        print(prec + str(num) + x + "x" + "+W")
    elif (num == 1):
        print(prec + x + "x" + "+W")
    elif (num == 0):
        print("W")
