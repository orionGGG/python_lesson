from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)
    # f.seek(0)回到了文件开始的位置


def print_a_line(line_count, f):
    print(line_count, f.readline())
    # readline()函数返回内容包含文件本来就有的\n，print函数默认以\n结尾，所以有两个\n


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
