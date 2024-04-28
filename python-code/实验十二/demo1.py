class Student:
    def __init__(self, name, age, scores):
        self.__name = name
        self.__age = age
        self.__scores = scores
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_course(self):
        return max(self.__scores)
stu=Student('小丸子',18,[89,90,91,80,77])
print("姓名：%s"%stu.get_name())
print("年龄：%d"%stu.get_age())
print("最高分：%d"%stu.get_course())