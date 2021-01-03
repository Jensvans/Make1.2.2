#!/usr/bin/env python
"""
Info: Je kunt het raster[x][y] zien als het karakter op de x- en y-coördinaten van een
"plaatje" dat met tekstkarakters is getekend. De (0, 0) oorsprong zal in de linkerbovenhoek liggen,
de x-coördinaten nemen toe naar rechts, en de y-coördinaten nemen toe naar beneden.
Neem bovenstaande lijst mee over en zorg voor de volgende output:
"""

__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"



lijst = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

angel = input('Enter up or down: ')         #asks for heart pointing upwards or downwards

if angel =='up':                            #activates when you have chosen up
    for y in range(0,6):                    #sets the y coordinate
        for x in range(0,9):                #sets the x coordinate
            if x==8:
                print(lijst[x][y])          #print the code
                break
            print(lijst[x][y],end='')       #print the code


if angel =='down':                          #activates when you have chosen down
    for y in range(0,6):                    #sets the y coordinate
        for x in range(0,9):                #sets the x coordinate
            if x==8:
                print(lijst[x][y])          #print the code
                break
            print(lijst[x][-y-1],end='')    #print the code


if __name__ == '__main__':                  # code to execute if called from command-line
    main()