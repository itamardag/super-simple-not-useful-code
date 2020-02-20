import os
from Library import Library as Library

def Parsec(input_file):

    with open(input_file, 'r') as in_file:

        lines = [line.rstrip() for line in in_file.readlines()]
        lines = lines[:-1]
        print(lines)
        book_count, lib_count, scan_days = [int(n) for n in lines[0].split(' ')]
        book_scores = [int(n) for n in lines[1].split(' ')]
        libraries = []
        for i in range(2, len(lines)-1, 2):
            book_num, signup, shipping = [int(n) for n in lines[i].split(' ')]
            lib_books = [int(n) for n in lines[i+1].split(' ')]
            libraries.append((signup, shipping, lib_books))

    return scan_days, book_scores, libraries

def WriteResult(filename, lib_count, lib_d):

    with open(filename[0:-4] + "_result.txt", 'w') as out_file:
        out_file.write(str(lib_count))
        out_file.write("\n")
        for library in lib_d:
            first_line = library[0]
            second_line = library[1]
            out_file.write(" ".join(str(item) for item in first_line))
            out_file.write('\n')
            out_file.write(" ".join(str(bookID) for bookID in second_line))
            out_file.write('\n')

def Manage(filename):
    #construction code
    content = Parsec(filename)
    daysToLive = content[0]
    booksDictionary = content[1]
    Library.bookValues = booksDictionary
    libraries = []
    for i in range(len(content[2])):
        libraries.append(Library(content[2][i][0], content[2][i][1], content[2][i][2]))

    #iterating code
    day = 0
    libNum = 0
    libValues = []
    while day < daysToLive and libNum < len(libraries):
        maxLib = (0, 0)
        for i in range(len(libraries)):
            libScore = libraries[i].libraryScore(daysToLive)
            if libScore > maxLib[1]:
                maxLib = (i, libScore)
        sentBooks = libraries[maxLib[0]].getBooks()
        daysToLive += libraries[maxLib[0]].getSignupTime()
        libNum += 1
        for i in range(len(sentBooks[0])):
            Library.bookValues[sentBooks[0][i]] = 0
        libValues.append(([maxLib[0], len(sentBooks[0])], sentBooks[0]))
    WriteResult(filename, libNum, libValues)
    print(filename)

if __name__ == "__main__":
    folder = os.listdir("G:\My Documents\Documents\HashCode2020\super-simple-not-useful-code\DataSets")
    for i in range(len(folder)):
        Manage("G:\My Documents\Documents\HashCode2020\super-simple-not-useful-code\DataSets" + "\\" + folder[i])