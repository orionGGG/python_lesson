class Thing(object):
    def test(self, message):  # Method 'test' may be 'static' ,原因是该方法不涉及对该类属性bai的操作
        print(message)


a = Thing()
a.test("hello")

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')  # stuff 自动转化为列表
# split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # stuff数组的最后一个
print(stuff.pop())
# 前面用' '代表用来连接的东西
print(' '.join(stuff))  # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
print('--'.join(stuff[3:5]))  # [3:5]连接Index(3,5)
