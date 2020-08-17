print(True and True)
print(False and True)
print(1 == 1 and 2 == 1)
print("test" == "test")
print(1 == 1 or 2 != 1)
print(True and 1 == 1)
print(False and 0 != 0)
print(True or 1 == 1)
print("test" == "testing")
print(1 != 0 and 2 == 1)
print("test" != "testing")
print("test" == 1)
print(not (True and False))
print(not (1 == 1 and 0 != 1))
print(not (10 == 1 or 1000 == 1000))
print(not (1 != 10 or 3 == 4))
print(not ("testing" == "testing" and "GJL" == "Cool guy"))
print(1 == 1 and not ("testing" == 1 or 1 == 0))
print("chunky" == "bacon" and not (3 == 4 or 3 == 3))
print(3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))
print("test" and "test")
print("test" and "testing")
print(0 and "test")
print("test" or "testing")
print("testing" or "test")
print(0 or "test")
'''
布尔表达式返回两个被操作对象中的一个，而非一定是Ture或False
这表示如果写的是False and 1得到的是第一个操作数False
如果写的是True and 1，得到的是第二个操作数1
第一个如果不是0就默认为True，and返回第一个

or也一样
True or 1返回第一个True
'''

'''
任何以False开头的and语句都会直接处理成False，不会继续检查后面的语句
任何包含True的or，只要处理到True，就不会继续向下推算，直接返回True
'''
