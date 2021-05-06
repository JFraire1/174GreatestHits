import random

import time

finish = False

harePattern = ('sleep','sleep','bighop','bighop','bigslip','smallhop','smallhop','smallhop','smallslip','smallslip')

tortPattern = ('fastplod','fastplod','fastplod','fastplod','fastplod','slip','slip','slowplod','slowplod','slowplod')

harePos = 0

tortPos = 0

hareWin = False

tortWin = False

def hareMove(harePos):
    hareNext = random.choice(harePattern)
    if hareNext == 'bighop':
        harePos += 9
        statement = 'HOPPED'
    elif hareNext == 'bigslip':
        harePos -= 12
        statement = 'SLIPPED'
    elif hareNext == 'smallhop':
        harePos += 1
        statement = 'hopped'
    elif hareNext == 'smallslip':
        harePos -= 1
        statement = 'slipped'
    else:
        statement = 'slept'

    if harePos < 0:
        harePos = 0

    if harePos > 69:
        harePos = 69

    statement = "The hare has " + statement + ". It is now at " + str(harePos+1)

    return [statement, harePos]
    
def tortMove(tortPos):
    tortNext = random.choice(tortPattern)
    if tortNext == 'fastplod':
        tortPos += 3
        statement = 'PLODDED'
    elif tortNext == 'slowplod':
        tortPos += 1
        statement = 'plodded'
    elif tortNext == 'slip':
        tortPos -= 6
        statement = 'slipped'

    if tortPos < 0:
        tortPos = 0

    if tortPos > 69:
        tortPos = 69

    statement = "The tortoise has " + statement + ". It is now at " + str(tortPos+1)

    return [statement, tortPos]


while finish == False:
    time.sleep(3)


    hareTrack = []
    for x in range(70):
        hareTrack.append('-')
    tortTrack = []
    for x in range(70):
        tortTrack.append('-')
    
    
    hareData = hareMove(harePos)
    tortData = tortMove(tortPos)
    

    print(hareData[0])
    print(tortData[0])
    

    harePos = hareData[1]
    tortPos = tortData[1]
    hareTrack[harePos] = "H"
    tortTrack[tortPos] = "T"
    

    for x in hareTrack:
        print(x, end = '')
    print()
    for x in tortTrack:
        print(x, end = '')
    print()


    if harePos == 69:
        print("The Hare Has Finished!!")
        hareWin = True

    if tortPos == 69:
        print("The Tortoise Has Finished!!")
        tortWin = True

    if (tortWin == True) and (hareWin == True):
        print("It is a tie!!!!")
        finish = True

    elif (tortWin == True) and (hareWin == False):
        print("The Tortoise Has Won!!")
        finish = True

    elif (hareWin == True) and (tortWin == False):
        print("The Hare Has Won!!")
        finish = True
    
    
    

