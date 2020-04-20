import math, random

def boardPrint(board):  #wyświetlanie planszy
    for x, y in board.items():
        row = y     #pobranie numeru wiersza
        counter = 0
        for z in row.values():  #wyświetlanie kolejnych pól w wierszu
            if counter<8:
                print(z, end = '')  #w jednym rzędzie, jeżeli licznik<8
                counter += 1
            else:
                print(z)    #zakończ wiersz

def firstPiece():   #wybór pierwszego gracza
    start = random.randint(1,100)   #l-ba losowa
    pieces = ['O', 'X'] #domyślna kolejność
    
    if start%2 == 1:    #zmień kolejność, jeżeli wylosowana wartość jest nieparzysta
        pieces[0] = 'X'
        pieces[1] = 'O'

    return pieces #zwraca wylosowaną kolejność pionków

def changeOrder(pieces):    #zmienia kolejność pionków
    newPieces = [' ', ' ']
    newPieces[0] = pieces[1]
    newPieces[1] = pieces[0]

    return newPieces

def movePiece(board, piece):   #funkcja ruchu pionków
    while True:
        print('Z: ')
        fromSquare = input()
        print('Do: ')
        toSquare = input()
        moveAbility = canItMove(board, fromSquare, toSquare, piece)

        if moveAbility[0] == True: #jeżeli ruch jest możliwy, wyjdź z pętli
            break

    board[fromSquare[1]][fromSquare[0]] = '  '   #usuń pionek z jego pola
    beatInfo = [False, False]    #informacja o biciu pionka

    if moveAbility[1] == True:
        beatInfo = beat(board, fromSquare, toSquare, piece)   #bij, jeśli to możliwe
    else:
        board[toSquare[1]][toSquare[0]] = piece+' '    #przesuń go na następne

    return beatInfo #zwróć info o biciu
            
def canItMove(board, start, finish, piece):   #sprawdza, czy można wykonać ruch
    letterDiff = ord(finish[0])-ord(start[0])  #różnica między literami pól
    numberDiff = ord(finish[1])-ord(start[1])   #różnica między cyframi pól
    condition = False    #wstępny warunek do ruchu
    move = [False, False]    #warunek ostateczny do wykonania ruchu
    letterRow = board['0']

    if start[0] in letterRow.keys() and finish[0] in letterRow.keys():  #czy istnieją litery obu pól
        if start[1] in chessBoard.keys() and finish[1] in chessBoard.keys():    #czy istnieją cyfry obu pól
            if board[start[1]][start[0]] != '# ' and board[start[1]][start[0]] != '  ' and board[start[1]][start[0]] == piece+' ':   #czy był start z właściwego pola
                if board[finish[1]][finish[0]] != piece+' ':    #czy nie ma ruchu na zajęte przez swój pionek miejsce
                    condition = True    #wstępny warunek spełniony

    if condition == True and abs(letterDiff) == 1:   #jeżeli wstępny warunek jest spełniony, sprawdź czy ruch będzie po skosie
        if (piece == 'O' and numberDiff == -1) or (piece == 'X' and numberDiff == 1): #w dół albo w górę, zależnie od znaku
            move[0] = True #ruch jest na razie możliwy
            if board[finish[1]][finish[0]] != '  ': #sprawdzenie, czy jest możliwe bicie, jeżeli wybrało się pole z pionkiem przeciwnika
                if finish[0] == 'A' or finish[0] == 'H' or finish[1] == '1' or finish[1] == '8':    #jeśli wybrało się pole na skraju planszy,
                    move[0] = False    #to ruch jest niemożliwy
                else:
                    nextLetterAscii = ord(finish[0])+letterDiff
                    nextNumberAscii = ord(finish[1])+numberDiff
                    nextLetter = chr(nextLetterAscii)
                    nextNumber = chr(nextNumberAscii)   #współrzędne pola za bitym pionkiem

                    if board[nextNumber][nextLetter] == '  ':
                        move[1] = True  #bicie możliwe, jeżeli za pionkiem jest puste pole

    return move     #odpowiedź czy można wykonać ruch i bicie

def beat(board, start, finish, piece):  #funkcja bicia pionka
    board[finish[1]][finish[0]] = '  '  #usuń zbity pionek
    letterDiff = ord(finish[0])-ord(start[0])  #różnica między literami pól
    numberDiff = ord(finish[1])-ord(start[1])   #różnica między cyframi pól
    letterDiff += letterDiff
    numberDiff += numberDiff    #zwiększ odpowiednio różnice
    newFinish = [' ', ' ']
    newFinish[0] = chr(ord(start[0])+letterDiff)
    newFinish[1] = chr(ord(start[1])+numberDiff)    #współrzędne pola za bitym pionkiem
    board[newFinish[1]][newFinish[0]] = piece+' '   #przesuń pionek na nowe miejsce
    beaten = [False, True]  #['O', 'X'], domyślnie bity jest X

    if piece == 'X':    #zmień, jeżeli bite jest O
        beaten[0] = True
        beaten[1] = False

    return beaten   #zwróć info o biciu
    

#szachownica
chessBoard = {'8':{'8': '8 ', 'A': '# ', 'B': 'O ', 'C': '# ', 'D': 'O ', 'E': '# ', 'F': 'O ', 'G': '# ', 'H': 'O '},
              '7':{'7': '7 ', 'A': 'O ', 'B': '# ', 'C': 'O ', 'D': '# ', 'E': 'O ', 'F': '# ', 'G': 'O ', 'H': '# '},
              '6':{'6': '6 ', 'A': '# ', 'B': 'O ', 'C': '# ', 'D': 'O ', 'E': '# ', 'F': 'O ', 'G': '# ', 'H': 'O '},
              '5':{'5': '5 ', 'A': '  ', 'B': '# ', 'C': '  ', 'D': '# ', 'E': '  ', 'F': '# ', 'G': '  ', 'H': '# '},
              '4':{'4': '4 ', 'A': '# ', 'B': '  ', 'C': '# ', 'D': '  ', 'E': '# ', 'F': '  ', 'G': '# ', 'H': '  '},
              '3':{'3': '3 ', 'A': 'X ', 'B': '# ', 'C': 'X ', 'D': '# ', 'E': 'X ', 'F': '# ', 'G': 'X ', 'H': '# '},
              '2':{'2': '2 ', 'A': '# ', 'B': 'X ', 'C': '# ', 'D': 'X ', 'E': '# ', 'F': 'X ', 'G': '# ', 'H': 'X '},
              '1':{'1': '1 ', 'A': 'X ', 'B': '# ', 'C': 'X ', 'D': '# ', 'E': 'X ', 'F': '# ', 'G': 'X ', 'H': '# '},
              '0':{'0': '  ', 'A': 'A ', 'B': 'B ', 'C': 'C ', 'D': 'D ', 'E': 'E ', 'F': 'F ', 'G': 'G ', 'H': 'H '}}

boardPrint(chessBoard)  #wyświetl planszę
oQuant = 12
xQuant = 12     #ilości pionków
beating = [False, False]    #informacja, który pionek bić 
tmpOrder = [' ', ' ']   #tablica do zmiany kolejności pionków
pieceOrder = firstPiece()   #kto zaczyna

while oQuant>0 or xQuant>0: #gra trwa, dopóki nie znikną pionki jednego z graczy 
    print('Teraz ' + pieceOrder[0] + '.')
    beating = movePiece(chessBoard, pieceOrder[0])    #ruch pionka
    tmpOrder = changeOrder(pieceOrder)
    pieceOrder = tmpOrder   #zmiana gracza

    if beating[0] == True:
        oQuant -= 1
    elif beating[1] == True:
        xQuant -= 1
    
    boardPrint(chessBoard)  #wyświetl planszę po ruchu
            
if oQuant>0:
    print('Wygrało O.')
elif xQuant>0:
    print('Wygrał X.')

