#!  python3

import os, PyPDF2, re, sys, warnings

warnings.filterwarnings("ignore")

def ispdf(fileName):
    if fileName.endswith('.pdf'):
        return True
    else:
        return False

def pressToExit():
    press = None
    print('\nAby wyjść z programu, naciśnij dowolny przycisk.')

    while press == None:
        press = input()

    sys.exit()
        
welcomeHeading = 'PROGRAM DO ŁĄCZENIA PLIKÓW PDF'
welcomeLine = '='*len(welcomeHeading)

print(welcomeLine)
print(welcomeHeading)
print(welcomeLine)

os.chdir('C:\\Users\\Olek\\Desktop\\Łączenie PDF')
print("Przenieś pliki do połączenia do folderu 'Łączenie PDF' na pulpicie.")
print("Gdy przeniesiesz wszystkie pliki, naciśnij dowolny przycisk.")
start = False
pdfFiles = []

while start == False:
    ready = None
    
    while ready == None:
        ready = input()

    folderContent = os.listdir('.')
    pdfNum = 0

    for names in folderContent:
        if ispdf(names) == True:
            pdfFiles.append(names)
            pdfNum += 1

    if pdfNum < 2:
        pdfFiles = []
        print('Należy umieścić w folderze przynajmniej 2 pliki pdf.')
        print("Gdy przeniesiesz wszystkie pliki, naciśnij dowolny przycisk.")
    else:
        start = True

pdfNamesLens = []
pdfListLen = len(pdfFiles)

for i in range(pdfListLen):
    pdfNamesLens.append(len(pdfFiles[i]))

maxLen = max(pdfNamesLens)
leftJust = 0
shift = 5
print('Pliki do złączenia:\n')

if len('Nazwa pliku') >= maxLen:
    leftJust = len('Nazwa pliku')+shift
else:
    leftJust = maxLen+shift

print('Nazwa pliku'.ljust(leftJust)+'Nr pliku\n')

for j in range(pdfListLen):
    print(pdfFiles[j].ljust(leftJust)+str(j+1))

print("\nCzy chcesz zmienić kolejność plików, w jakiej będą łączone (odpowiedz: 'tak' lub 'nie')?\n")

while True:
    answer = None

    while answer == None:
        answer = input()
        
    yesNoRegex = re.compile(r'(tak)|(nie)', re.I)
    yesNo = yesNoRegex.search(answer)

    if yesNo != None and len(answer) == 3:
        break

if (yesNo.group()).lower() == 'tak':
    print('\nWpisz pliki wg ich numerów na pierwszej liście w żądanej kolejności:\n')
    newOrder = []

    while len(newOrder) < pdfListLen:
        newNumber = None

        while newNumber == None:
            newNumber = input()

        newOrder.append(newNumber)
        lastIndex = len(newOrder)-1

        if newOrder[lastIndex].isdecimal() == False or int(newOrder[lastIndex]) > pdfListLen or int(newOrder[lastIndex]) < 0:
            del newOrder[lastIndex]
        elif lastIndex > 0:
            for k in range(lastIndex):
                if newOrder[k] == newOrder[lastIndex]:
                    del newOrder[lastIndex]

    tmpPdfFiles = []

    for l in range(pdfListLen):
        tmpPdfFiles.append(pdfFiles[int(newOrder[l])-1])

    print('\nLista plików w nowej kolejności:\n')
    print('Nazwa pliku'.ljust(leftJust)+'Nr pliku\n')
    pdfFiles = []

    for m in range(pdfListLen):
        pdfFiles.append(tmpPdfFiles[m])

    for n in range(pdfListLen):
        print(pdfFiles[n].ljust(leftJust)+str(n+1))

pdfWriter = PyPDF2.PdfFileWriter()

for pdfName in range(pdfListLen):
    currentPdf = pdfFiles[pdfName]
    pdfOpen = open(currentPdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(currentPdf)

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    pdfOpen.close()

os.chdir('.\\Złączone')
print('\nPodaj nazwę połączonego pliku PDF:\n')
mergedPdfBaseName = input()
mergedPdfName = mergedPdfBaseName+'.pdf'
pdfOutputFile = open(mergedPdfName, 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

print("\nPliki PDF zostały złączone w plik '{}' w podfolderze 'Złączone'.".format(mergedPdfName))
warnings.filterwarnings("default", category = FutureWarning)
pressToExit()
        
