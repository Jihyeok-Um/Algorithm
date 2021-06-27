def changecode(code):
    code = code.replace('C#', 'c')
    code = code.replace('D#', 'd')
    code = code.replace('F#', 'f')
    code = code.replace('G#', 'g')
    code = code.replace('A#', 'a')
    return code


def solution(m, musicinfos):
    m = changecode(m)
    names = []
    runningTime = []
    for i in range(len(musicinfos)):
        hours = int(musicinfos[i][6:8]) - int(musicinfos[i][:2])
        minutes = int(musicinfos[i][9:11]) - int(musicinfos[i][3:5])
        minutes += hours * 60
        j = len(musicinfos[i]) - 1
        while (musicinfos[i][j] != ','):
            j -= 1
        code = musicinfos[i][j + 1:len(musicinfos[i])]
        name = musicinfos[i][12:j]
        code = changecode(code)
        full = minutes // len(code)
        notFull = minutes % len(code)

        ans = ""
        for k in range(full):
            ans += code
        for k in range(notFull):
            ans += code[k]

        if (m in ans):
            names.append(name)
            runningTime.append(minutes)

    if (len(names) == 1):
        return names[0]
    elif (len(names) >= 1):
        return names[runningTime.index(max(runningTime))]
    else:
        return "(None)"