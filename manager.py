import os
import something as parsei
import somethingElse as Library

def Manage(filename):
    #construction code
    content = parsei.parse(filename);
    daysToLive = content[0];
    booksDictionary = set;
    for i in range(len(content[1])):
        booksDictionary[i] = content[1][i];
    #TODO: library's book dict
    libraries = [];
    for i in range(len(content[1])):
        libraries[i] = Library(content[2][i][0], content[2][i][1], content[2][i][2]);

    #iterating code
    day = 0;
    while day < daysToLive:
        maxLib = (0, 0);
        for i in range(len(libraries)):
            libScore = libraries[i].libraryScore(daysToLive);
            if libScore > maxLib[1]:
                maxLib = (i, libScore);
        SentBooks = libraries[maxLib[0]].getBooks();
        daysToLive += libraries[maxLib[0]].getSignupTime();










































if __name__ == "__main__":
    folder = os.listdir("G:\My Documents\Documents\HashCode2020\super-simple-not-useful-code\DataSets");
    for i in range(len(folder)):
        manage("G:\My Documents\Documents\HashCode2020\super-simple-not-useful-code\DataSets" + "\\" + folder[i]);