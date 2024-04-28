class Animal:
    def __init__(self,owner="animal",age=5):
        self.owner=owner
        self.age=age
    def print_info(self):
        print("我是一只%s"%self.owner)
        print("我今年%d岁了"%self.age)

class Bird(Animal):
    def print_info(self):
        print("我是一只美丽的%s"%self.owner)
        print("我今年%d岁了"%self.age)
class Fish(Animal):
    def print_info(self):
        print("我是一条红色的%s"%self.owner)
        print("我今年%d岁了"%self.age)
bird=Bird("鸟",8)
bird.print_info()
fish=Fish("鱼",10)
fish.print_info()