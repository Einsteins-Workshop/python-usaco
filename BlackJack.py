#Black Jack Game

import time
import random

cash=100

while cash>0:
    bet=0
    print('You have:$',cash)
    bet=int(input('How much will you bet?:'))
    print('You bet:',bet)
    time.sleep(0.3)
    print('Starting game...')
    game='yes'
    time.sleep(0.3)
    aceC=4
    twoC=4
    threeC=4
    fourC=4
    fiveC=4
    sixC=4
    sevenC=4
    eightC=4
    nineC=4
    tenC=4
    jackC=4
    queenC=4
    kingC=4
