import time

#手机
class Oldphone:
    __brand = ""

    def setbrand(self, brand):
        self.__brand = brand

    def getbrand(self):
        return self.__brand

    def call(self, number):
        print("正在给", number, "打电话")

class Newphone(Oldphone):
    def call(self, number):
        for i in range(3):
            print(".", end="")
            time.sleep(1)
        print("语音拨号中...")
        super().call(number)

    def introduce(self, brand):

        print("品牌为:", brand, "的手机很好用")

phone = Newphone()

phone.call(110)
phone.introduce("小米")



#工人，学生
class Person:
    age = 0
    sex = ""
    name = ""

class Worker(Person):
    pass

    def present(self, working):
        print("这个工人叫", self.name,"，今年已经",self.age, "岁了,是位", self.sex, "性，正在", working)

work = Worker()
work.name = "王二"
work.age = 28
work.sex = "男"
work.present("搬砖")


class Student(Person):
    number = 0

    def learn(self, study, sing):
        print("这个学生叫", self.name, "，今年已经", self.age, "岁了,是位", self.sex, "性，正在学习", study, "学习完，准备去大礼堂参加", sing)


student = Student()
student.name = "小明"
student.sex = "女"
student.age = 16
student.learn("数学", "黄河大合唱")