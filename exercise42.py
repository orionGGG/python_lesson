# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


'''在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行'''

'''python中的属性不用提前声明，想定义的时候直接定义就是了'''


# pass 不做任何事情，一般用做占位语句

# Dog是Animal的子类
class Dog(Animal):

    def __init__(self, name):  # __init__()相当于构造函数
        self.name = name  # 类的绑定属性


# Cat是Animal的子类
class Cat(object):

    def __init__(self, name):
        self.name = name


'''如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）'''


class Person(object):
    def __init__(self, name):  # 在__init__()中定义可以确保类有这个属性并且有一个默认值
        self.__name = name
        # Person has a pet of some kind
        self.pet = None
        # 确保类的self.pet属性被设置为默认None

    def get_name(self):
        return self.__name


class Employee(Person):  # employee雇员

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        # super是将父类的__init__()方法运行起来的方法，调用父类的构造方法
        self.salary = salary


class Fish(object):
    pass


# 三文鱼类是鱼类的子类
class Salmon(Fish):
    pass


class Caoyu(Fish):
    pass


tom = Cat("Tom")
daHuang = Dog("DaHuang")
mary = Person("Mary")
mary.pet = tom
mary.__name = "1";  # 错误写法
'''表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
内部的__name变量已经被Python解释器自动改成了_类名__name(不同版本的Python解释器可能会把__name改成不同的变量名。)
而外部代码给bart新增了一个__name变量'''
print(mary.__name)
print(mary.get_name())
print(mary)
frank = Employee("Frank", 12)
frank.pet = daHuang
flipper = Fish()
cwy = Salmon()
cy = Caoyu()
