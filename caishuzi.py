import random

i = 0
while i<4:
    print ('****************************************')
    num = input('请输入0到9的任意一个数：')
    xnum = random.randint(0,9)

    x = 3-i

    if num ==str(xnum):
        print('运气真好，猜对了')
        break
    elif num > str(xnum):
        print('''猜大了！\n 哈哈，正确答案是:%s\n 您还有%s次机会''' %(xnum,x))
    elif num < str(xnum):
        print('''猜小了！\n 哈哈，正确答案是:%s\n 您还有%s次机会''' % (xnum, x))
    print('****************************************')

    i+= 1