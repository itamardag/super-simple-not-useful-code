import os
from Library import Library as Library

def Parse(self, input_file):

    with open(input_file, 'r') as in_file:

        lines = [line.rstrip() for line in in_file.readlines()]
        lines = lines[:-1]
        print(lines)
        book_count, lib_count, scan_days = [int(n) for n in lines[0].split(' ')]
        book_scores = [int(n) for n in lines[1].split(' ')]
        libraries = []
        for i in range(2, len(lines), 2):
            book_num, signup, shipping = [int(n) for n in lines[i].split(' ')]
            lib_books = [int(n) for n in lines[i+1].split(' ')]
            libraries.append((signup, shipping, lib_books))

    return scan_days, book_scores, libraries

def Manage(filename):
    #construction code
    content = Parse(filename);
    daysToLive = content[0];
    booksDictionary = set;
    for i in range(len(content[1])):
        booksDictionary[i] = content[1][i];
    Library.bookValues = booksDictionary;
    libraries = [];
    for i in range(len(content[1])):
        libraries[i] = Library(content[2][i][0], content[2][i][1], content[2][i][2]);

    #iterating code
    day = 0;
    libNum = 0;
    libValues = [];
    while day < daysToLive:

        maxLib = (0, 0);
        for i in range(len(libraries)):
            libScore = libraries[i].libraryScore(daysToLive);
            if libScore > maxLib[1]:
                maxLib = (i, libScore);
        sentBooks = libraries[maxLib[0]].getBooks();
        daysToLive += libraries[maxLib[0]].getSignupTime();
        libNum += 1;
        for i in range(len(sentBooks[0])):
            del Library.bookValues[sentBooks[0][i]];
        libValues[libNum] = ([maxLib[0], len(sentBooks)], sentBooks[0] + sentBooks[1]);
    write(libNum, libValues);

if __name__ == "__main__":
    folder = os.listdir("G:\My Documents\Documents\HashCode2020\super-simple-not-useful-code\DataSets");
    for i in range(len(folder)):
        Manage("G:\My Documents\Documents\HashCode2020\super-simple-not-useful-code\DataSets" + "\\" + folder[i]);