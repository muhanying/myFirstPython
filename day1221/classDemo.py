class Person:
    name = 'defaule'
    age = 0
    gender = '男'
    high = 170

    def __init__(self,name,age,gender,high):
        self.name=name
        self.age=age
        self.gender=gender
        self.high=high


    @classmethod
    def eat(self):
        print(self.name+" chi")

    def run(self):
        print(self.name+" running")
#类变量
print(Person.name)
#类方法不能直接调用方法，需要在方法里加装载器 @classmethod
print(Person.eat())
#类实例化
p = Person('zs',10,'女',167)
print(p.name)
#实例化对象可以调方法
print(p.eat)

# zs = Person('zhangsan',10,'女',175)
# print(zs.__dict__)