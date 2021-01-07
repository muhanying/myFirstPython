tuple_demo = (1,2,3)
tuple_demo2 = 1,2,3
print(type(tuple_demo))
print(type(tuple_demo2))
#元祖有不可变特性
# tuple_demo[1] = 4
print(tuple_demo)

a = [1,2]
tuple_demo3 = (1,3,a)
tuple_demo3[2][0] = 3 #执行不通过，视频里可以
print(tuple_demo3)

b = [(1,2),(3,4)]
for index,item in enumerate(b):
    b[index] = item+5
print(b)