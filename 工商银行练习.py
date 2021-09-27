import random
from DBUtils import update
from DBUtils import select

print("==============================================")
print("|------------华夏人民银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")

# 银行字典
bank = {}   #相当于一个空的数据库
bank_name = "华夏全球银行"#全局变量
# 银行开户逻辑
'''
jason:{

    account:85563196
},
张三:{
} 
'''
def bank_adduser(account, username, password, country, province, street, door, money, registerDate, bank_name):
    sql = "select count(*) from function1"
    param = []
    data = select(sql, param, mode='one')[0]
    if data >= 100:
        return 3

    sql1 = "select * from function1 where account = %s"
    param1 = [account]
    data = select(sql1, param1)
    if len(data) > 0:#如果一个变量在容器内就运行代码
        return 2

    sql2 = "insert into function1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account, username, password, country, province, street, door, money, registerDate, bank_name]
    data = update(sql2, param2)
    return 1
# 银行开户操作逻辑
def useradd():
    username = input("请输入您的用户名：")#局部变量
    password = input("请输入密码：")
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account = random.randint(10000000, 99999999)
    money = 0
    registerDate = input("请输入时间:")
    bankadd = bank_adduser(account, username, password, country, province, street, door, money, registerDate, bank_name)
    if bankadd == 1:
        print("添加用户成功，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        # sql = 'select money from function1 where account = %s'
        # param = [account]
        # data = select(sql, param, mode='one')[0]
        # print(data)
        print(info % (account, username, country, province, street, door, money, bank_name))
    elif bankadd == 2:
        print("用户已存在，请勿重复添加！")
    elif bankadd == 3:
        print("数据库已满")
# 存钱逻辑
def bank_saveMoney(account_save,save_money):
    if account_save not in bank:
        return False
    else:
        bank[account_save]["money"] = bank[account_save]["money"] + save_money
        return True
#存钱操作代码
def saveMoeny():
    account_money = input("请输入您存钱的账号：")
    sql = "select * from function1 where account = %s"
    param = [account_money]
    data = select(sql, param)
    if len(data) > 0:
        money = int(input("请输入你要存入的金额："))
        sql1 = 'update function1 set money = money + %s where  account = %s'
        param1 = [money, account_money]
        update(sql1, param1)
        sql2 = 'select money from function1 where account = %s'
        param2 = [account_money]
        data1 = select(sql2, param2, mode="one")[0]
        print("存款成功！当前余额：", data1)
    else:
        print("该用户不存在")

#取钱逻辑
def outputMoney():
    n = 4
    m = 0
    account = int(input("请输入你的账号："))
    sql = "select * from function1 where account = %s"
    param = [account]
    data = select(sql, param)
    if len(data) > 0:
        while True:
            password = int(input("请输入您的密码"))
            sal1 = 'select password from function1 where account = %s'
            param1 = [account]
            data1 = select(sal1, param1, mode='one')[0]
            if password == data1:
                withdraw_money = int(input("请输入你要取款的金额："))
                sql2 = 'select money from function1 where account = %s'
                param2 = [account]
                data2 = select(sql2, param2, mode='one')[0]
                if withdraw_money > data2:
                    print("您的余额不足！余额：", data2)
                    break
                else:
                    sql3 = 'update function1 set money = money - %s  where  account = %s'
                    param3 = [withdraw_money, account]
                    update(sql3, param3)
                    sql4 = 'select money from function1  where  account = %s'
                    param4 = [account]
                    data3 = select(sql4, param4, mode="one")[0]
                    print("取钱成功！您的余额为：", data3)
                    break
            else:
                print("密码不正确!您还有", n - 1, "次机会")
                m += 1
                n -= 1
                if m == 4:
                    print("该账号今日已锁定，请明天再来。")
                    break
    else:
        print("您输入的账号不存在！")
#转账
def transfer():
    n = 4
    m = 0
    account = int(input("请输入您的账号"))
    sql = "select * from function1 where account = %s"
    param = [account]
    data = select(sql, param)
    if len(data) > 0:
        account2 = int(input("请输入您要转账的账号："))
        sql1 = "select * from function1 where account = %s"
        param1 = [account2]
        data1 = select(sql1, param1)
        if len(data1) > 0:
            password = int(input("请输入您的密码"))
            sql2 = 'select password from function1  where account = %s'
            param2 = [account]
            data2 = select(sql2, param2, mode='one')[0]
            while True:
                if password == data2:
                    money = int(input("请输入您要转账的金额："))
                    sql3 = 'select money from function1 where account = %s'
                    param3 = [account]
                    data3 = select(sql3, param3, mode='one')[0]
                    if money > data3:
                        print('您的余额不足，转账失败！')
                        break
                    else:
                        sql4 = 'update function1 set money = money - %s  where account  = %s'
                        param4 = [money,account]
                        update(sql4, param4)
                        sql5 = 'select money from function1  where account = %s'
                        param5 = [account]
                        data4 = select(sql5, param5,mode='one')[0]
                        print("转账成功！您的余额为：", data4)
                        sql6 = "update function1  set  money = money + %s  where account = %s"
                        param6 = [money,account2]
                        update(sql6,param6)
                        break
                else:

                    print("密码错误！您还有", n - 1, "次机会")
                    n -= 1
                    m += 1
                    if m == 4:
                        print("您的账号今天不能继续登录！")
                        break
        else:
            print("您输入的账号不存在")
    else:
        print("您输入的账号不正确！")
#查询
def search():
    n = 4
    m = 0
    account = int(input("请输入您要查询的账号"))
    sql = "select * from function1 where account = %s"
    param = [account]
    data = select(sql, param)
    if len(data) > 0:
        password = int(input("请输入密码"))
        sql2 = 'select password from function1 where account = %s'
        param2 = [account]
        data2 = select(sql2, param2, mode='one')[0]
        print(data2)
        while True:
            if password == data2:
                sql3 = 'select * from function1 where account = %s'
                param3 = [account]
                data3 = select(sql3, param3)
                print(data3)
                break
            else:

                print("密码错误，您还有", n - 1, "次机会！")
                n -= 1
                m += 1
                if m == 4:
                    print("您的账号以冻结，请明天再来！")
                    break
    else:
        print("该用户不存在")


while True:#永远循环
    begin = input("请选择业务")
    if begin == "1":
        useradd()
    elif begin == "2":
        # print("存钱")
        saveMoeny()
    elif begin == "3":
        # print("取钱")
        outputMoney()
    elif begin == "4":
        # print("转账")
        transfer()
    elif begin == "5":
        # print("查询")
        search()
    elif begin == "6":
        print("欢迎下次使用!")
        break
    else:
        print("你瞎输入什么东西！")
        break

