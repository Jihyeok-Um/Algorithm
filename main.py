def palindrome(length, s):
    check = s[0]
    count = 0
    for i in range(len(s)):
        if (s[i] == check):
            count += 1
    if (count == len(s)):
        print(-1)
        return
    if (len(s) % 2 == 0):
        str1 = s[len(s)//2:]
        str2 = s[:len(s)//2]
        if(str1 == str2[::-1]):
            print(len(s)-1)
            return
        else:
            print(length)
            return
    elif (len(s) % 2 == 1):
        str1 = s[:len(s)//2+1]
        str2 = s[len(s)//2:]
        if (str1 == str2[::-1]):
            print(len(s) - 1)
            return
        else:
            print(length)
            return

string = input()
palindrome(len(string),string)
