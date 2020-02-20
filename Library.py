class Library:

    bookValues = {}

    def __init__(self, signUpTime, booksPerDay, books):
        self.__signupTime = signUpTime
        self.__books = sorted(books, key=lambda x: Library.bookValues[x], reverse=True)
        self.__booksPerDay = booksPerDay
        self.__booksToSend = []

    def libraryScore(self, timeToEnd):
        maxNumBooks = (timeToEnd - self.__signupTime) * self.__booksPerDay
        i = 0
        sumScore = 0
        self.__booksToSend = []
        while len(self.__booksToSend) < maxNumBooks and i < len(self.__books):
            curScore = Library.bookValues[self.__books[i]]
            if curScore > 0:
                self.__booksToSend.append(self.__books[i])
                sumScore += curScore
            i += 1
        return sumScore

    def getSignupTime(self):
        return self.__signupTime

    def getBooks(self):
        return (self.__booksToSend,)


