# class MyException(Exception):
#     def __init__(self,v1,v2):
#         self.v1=v1
#         self.v2=v2
# raise MyException(1,2)


try:
    num1 = int(input("please input a num "))
    num2 = int(input("please input a num "))
    print(num1 / num2)
except Exception as e:
    print(str(e))
finally:
    print("结束了")
