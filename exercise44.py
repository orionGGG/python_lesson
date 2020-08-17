class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")

    def test(self):
        print("TEST")


class ooo(object):

    def test1(self):
        print("ooo")


class Child(Parent, ooo):
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


'''
    super(子类名，self)这个函数可以得到父类
    java中在子类用super.就直接等效于父类，然后就可以调用父类
    这句话可以读作：用Child和self这两个参数调用super，在此返回的基础上调用altered方法
    super出现在继承了父类的子类中。有三种存在方式：
    1、获取父类中的名字为xxx的变量引用
    2、直接访问并调用父类中的方法
    3、调用父类的初始化构造函数
    你可以不知道原来父类的初始化构造函数是怎么写的，但是却可以轻易封装它。
'''

'''如果将函数放进父类中，那么所有的子类(也就是Child这样的类)将会自动获得这些函数功能'''
'''如果子类和父类都定义同一个函数，则子类中的会覆盖父类中的'''
dad = Parent()
son = Child()
dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()
dad.test()
son.test()
son.test1()
