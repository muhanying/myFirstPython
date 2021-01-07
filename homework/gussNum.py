"""
猜数字游戏：1-100的数字
猜小了 提示小了
猜大了 提示大了
"""
import random

c_num = random.randint(0,100)
while True:
    p_num = int(input('请输入数字：'))
    if p_num>c_num:
        print("你猜大了")
    elif p_num<c_num:
        print('你猜小了')
    else:
        print('你猜对了')
        break