import sys
import  time
print(sys.path)
print(time.gmtime())

#格式化
list_a = [1,'a','c']
dict_a = dict(key1='v1',key2='v2')
name = 'aaa'
age = 2
print(f"my name is {name} my age id {age} my list is {list_a} my dict is {dict_a}")
print(f"{(lambda x:x+2)(3)}")

f = open("data.txt","w")
f.write("test")
print(f.readlines())
f.close()