num = int(input())
start = 100
min_ = 10000000
channelList = []
brokenNum = int(input())
if (brokenNum != 0):
    broken = list(map(int, input().split()))
else:
    broken = []
count_ = 0
value_ = 0

def makeChannel(broken):
    global channelList
    for i in range(1000001):
        if (isBroken(i,broken)):
            channelList.append(i)

def isBroken(channel, broken):
    if (channel == 0):
        if (broken.count(0) != 0):
            return False

    while(channel != 0):
        if (broken.count(int(channel % 10)) != 0):
            return False
        channel = int(channel / 10)
    return True

temp = abs(num - start)
makeChannel(broken)
for i in range(0, len(channelList)):
    count_ = 0
    if (channelList[i] == 0):
        count_ = 1
    value_ = abs(num - channelList[i])
    while(channelList[i] != 0):
        channelList[i] = int(channelList[i] / 10)
        count_ += 1

    min_ = min(min_, min(count_+value_, temp))
if (len(channelList) == 0):
    print(temp)
else:
    print(min_)

