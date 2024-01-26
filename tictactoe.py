import os
import sys
def table():
    print(grid[0][0]+'|'+grid[0][1]+'|'+grid[0][2]+'\n-+-+-')
    print(grid[1][0]+'|'+grid[1][1]+'|'+grid[1][2]+'\n-+-+-')
    print(grid[2][0]+'|'+grid[2][1]+'|'+grid[2][2])
def p1():
    x = 0

    choice = int(input(n1+', enter position: '))

    os.system('cls')

    if(choice>0 and choice<4):
        while x<4:
            if(choice == x):
                if(grid[0][x-1] != 'X' and grid[0][x-1] != 'O'):
                    grid[0][x-1] = 'X'
                    xgrid[0][x-1] = 'X'
                    table()
                else:
                    sys.exit('invalid input')
            x+=1
    elif(choice>3 and choice<7):
        while x<7:
            if(choice == x):
                if(grid[1][x-4] != 'X' and grid[1][x-4] != 'O'):
                    grid[1][x-4] = 'X'
                    xgrid[1][x-4] = 'X'
                    table()
                else:
                    sys.exit('invalid input')
            x+=1
    elif(choice>6 and choice<10):
        while x<10:
            if(choice == x):
                if(grid[2][x-7] != 'X' and grid[2][x-7] != 'O'):
                    grid[2][x-7] = 'X'
                    xgrid[2][x-7] = 'X'
                    table()
                else:
                    sys.exit('invalid input')
            x+=1
    else:
        sys.exit('invalid input')
def p2():
    x = 0

    choice = int(input(n2+', enter position: '))

    os.system('cls')

    if(choice>0 and choice<4):
        while x<4:
            if(choice == x):
                if(grid[0][x-1] != 'X' and grid[0][x-1] != 'O'):
                    grid[0][x-1] = 'O'
                    ygrid[0][x-1] = 'O'
                    table()
                else:
                    sys.exit('invalid input')
            x+=1
    elif(choice>3 and choice<7):
        while x<7:
            if(choice == x):
                if(grid[1][x-4] != 'X' and grid[1][x-4] != 'O'):
                    grid[1][x-4] = 'O'
                    ygrid[1][x-4] = 'O'
                    table()
                else:
                    sys.exit('invalid input')
            x+=1
    elif(choice>6 and choice<10):
        while x<10:
            if(choice == x):
                if(grid[2][x-7] != 'X' and grid[2][x-7] != 'O'):
                    grid[2][x-7] = 'O'
                    ygrid[2][x-7] = 'O'
                    table()
                else:
                    sys.exit('invalid input')
            x+=1
    else:
        sys.exit('invalid input')
def checkp1():
    if (xgrid[0][0] == xgrid[0][1] and xgrid[0][0] == xgrid[0][2]):
        sys.exit(n1+' has won')
    elif (xgrid[1][0] == xgrid[1][1] and xgrid[1][0] == xgrid[1][2]):
        sys.exit(n1+' has won')
    elif (xgrid[2][0] == xgrid[2][1] and xgrid[2][0] == xgrid[2][2]):
        sys.exit(n1+' has won')
    elif (xgrid[0][0] == xgrid[1][0] and xgrid[0][0] == xgrid[2][0]):
        sys.exit(n1+' has won')
    elif (xgrid[0][1] == xgrid[1][1] and xgrid[0][1] == xgrid[2][1]):
        sys.exit(n1+' has won')
    elif (xgrid[0][2] == xgrid[1][2] and xgrid[0][2] == xgrid[2][2]):
        sys.exit(n1+' has won')
    elif (xgrid[0][0] == xgrid[1][1] and xgrid[0][0] == xgrid[2][2]):
        sys.exit(n1+' has won')
    elif (xgrid[0][2] == xgrid[1][1] and xgrid[0][2] == xgrid[2][0]):
        sys.exit(n1+' has won')
def checkp2():
    if (ygrid[0][0] == ygrid[0][1] and ygrid[0][0] == ygrid[0][2]):
        sys.exit(n2+' has won')
    elif (ygrid[1][0] == ygrid[1][1] and ygrid[1][0] == ygrid[1][2]):
        sys.exit(n2+' has won')
    elif (ygrid[2][0] == ygrid[2][1] and ygrid[2][0] == ygrid[2][2]):
        sys.exit(n2+' has won')
    elif (ygrid[0][0] == ygrid[1][0] and ygrid[0][0] == ygrid[2][0]):
        sys.exit(n2+' has won')
    elif (ygrid[0][1] == ygrid[1][1] and ygrid[0][1] == ygrid[2][1]):
        sys.exit(n2+' has won')
    elif (ygrid[0][2] == ygrid[1][2] and ygrid[0][2] == ygrid[2][2]):
        sys.exit(n2+' has won')
    elif (ygrid[0][0] == ygrid[1][1] and ygrid[0][0] == ygrid[2][2]):
        sys.exit(n2+' has won')
    elif (ygrid[0][2] == ygrid[1][1] and ygrid[0][2] == ygrid[2][0]):
        sys.exit(n2+' has won')
grid = [
    ['.','.','.'],
    ['.','.','.'],
    ['.','.','.'],
]
xgrid = [
    ['1','2','3'],
    ['4','5','6'],
    ['5','8','9'],
]
ygrid = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
]
os.system('cls')
i = 0
n1 = input('Player 1, enter your name: ')
n2 = input('Player 2, enter your name: ')
while(i<4):
    print('\n\n\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9')
    p1()
    checkp1()

    print('\n\n\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9')
    p2()
    checkp2()

    i+=1
print('\n\n\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9')
p1()
checkp1()

print('its a draw')