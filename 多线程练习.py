from threading import Thread
import time
egg = 0
eggmuch = 2
class Cook(Thread):
    name = ""
    count = 0

    def run(self) -> None:
        global egg
        while True:
            if egg == 50:
                    time.sleep(3)
                    print("篮子满了",self.name, "厨师，先等等")
                    break
            else:
                egg += 1
                time.sleep(0.1)
                print("还有", egg, "余量的蛋挞")

class User(Thread):
    money = 150
    name = ""
    count = 0

    def setName(self, name):
        self.name = name

    def run(self) -> None:
        global egg
        global eggmuch
        while True:
            if egg == 0:
                time.sleep(3)
            elif egg >= 0 and self.money >= eggmuch:
                egg = egg - 1
                self.money = self.money - eggmuch
                self.count = self.count + 1
                print(self.name, "抢到了一个蛋挞，还有", self.money, "的钱")
            elif self.money == eggmuch:
                print(self.name, "没钱了，当前你抢到了", self.count, "蛋挞")
                break
c = Cook()
c.name = "王二"
c.start()

u1 = User()
u1.setName("小李")
u2 = User()
u2.setName("小王")
u3 = User()
u3.setName("小刘")



u1.start()
u2.start()
u3.start()