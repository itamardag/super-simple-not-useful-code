class Parser:

    def __init__(self):
        pass

    def parse(self, input_file):

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

