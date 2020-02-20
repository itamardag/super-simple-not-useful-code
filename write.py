def write(lib_count, lib_d):

    with open('Output.txt', 'w') as out_file:
        out_file.write(str(lib_count))
        out_file.write("\n")
        for library in lib_d:
            first_line = library[0]
            second_line = library[1]
            out_file.write(" ".join(str(item) for item in first_line))
            out_file.write('\n')
            out_file.write(" ".join(str(bookID) for bookID in second_line))
            out_file.write('\n')