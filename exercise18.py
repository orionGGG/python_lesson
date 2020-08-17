# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1},arg2:{arg2}")


# *的功能是告诉python把函数的所有参数都接受进来，然后放到名为args的列表中去
# 和argv差不多意思，前者用在函数上，一般不会经常用到


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1:{arg1},arg2:{arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1:{arg1}")


# this one takes no arguments
def print_none():
    print("I got nothing.")


print_two("G", "jl")
print_two_again("g", "jl")
print_one("First!")
print_none()
