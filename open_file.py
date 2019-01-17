# Trivia Game | Jackson Pike | January 2019
import sys


def open_file(file_name, mode):
    try:
        acc_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return acc_file

def read_line(file):
    line = file.readline()
    line = line.replace("/", "\n")
    return line

testfile = open_file('jack_pike', 'w')
testfile.write("this/ is a/ test")
testfile.close()
testfile = open_file("jack_pike", "r")
line = read_line(testfile)
print(line)

