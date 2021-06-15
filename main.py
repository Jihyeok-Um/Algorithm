def solution(brown, yellow):
    garoYellow = yellow
    seroYellow = 1
    while (garoYellow >= seroYellow):
        if (yellow == garoYellow * seroYellow):
            garoBrown = garoYellow
            seroBrown = seroYellow + 2
            if (brown == (garoBrown * 2) + (seroBrown * 2)):
                return [garoBrown + 2, seroBrown]

        if (yellow > garoYellow * seroYellow):
            seroYellow += 1
            garoYellow += 1
        garoYellow -= 1
