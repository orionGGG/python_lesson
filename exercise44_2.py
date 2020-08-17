class Other1(object):

    def implicit(self):
        print("o implicit()")

    def override(self):
        print("o override()")

    def altered(self):
        print("o altered()")

    def test_1(self):
        print("TEST")


class Child(object):

    def __init__(self):
        self.other = Other1()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.override()

    def altered(self):
        print("CHILD altered()")

    def test_2(self):
        self.other.test_1()


'''
    不用特地去写，任何类都是组合的关系，只需要用other就可以从一个类访问到另一个类
'''
son = Child()
son.implicit()
son.override()
son.altered()
son.test_2()
