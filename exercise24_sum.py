print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:', end=" ")
print('\n newlines and \t tabs.')

poem = '''
床前明月光
疑是地上霜
举头望明月
低头思故乡
'''

print("---------------")
print(poem)
print("---------------")

five = 10 + 3 - 2 - 6
print(f"This should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)
# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formual = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formual))
