def solution(participant, completion):
    participant.sort()
    completion.sort()
    result = ""
    for i in range(len(completion)):
        if (completion[i] != participant[i]):
            result = participant[i]
            break

    if (result == ""):
        return participant[len(participant) - 1]
    else:
        return result