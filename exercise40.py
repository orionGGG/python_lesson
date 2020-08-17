import mystuff

# 调用模块
mystuff.apple()
print(mystuff.tangerine)
print(mystuff.stuff['apple'])
mystuff.apple()


class Mystuff(object):
    def __init__(self):
        # __init__就是构造函数
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


thing = Mystuff()
thing.apple()
# 可以在脚本中自由地给一个实例变量绑定属性，比如，给实例Mystuff绑定一个name属性：
Mystuff.name = "haha"
print(Mystuff.name)
print(thing.tangerine)
