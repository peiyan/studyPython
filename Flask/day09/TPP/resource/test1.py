######## 装饰器基本概念



import time

# 计算时间装饰器
def total_time(func):
    def total():
        starttime = time.time()
        func()
        endtime = time.time()
        print(endtime-starttime)

    return total


def eat():
    time.sleep(1)
    print('哥，正在吃饭....')
    time.sleep(1)

def study():
    time.sleep(1)
    print('正在学习，我学习我光荣....')
    time.sleep(2)

@total_time
def game():
    time.sleep(1)
    print('正在玩游戏，我游戏我光荣....')
    time.sleep(2)


if __name__ == '__main__':
    # 问题引入
    # starttime = time.time()
    # eat()
    # endtime = time.time()
    # print(endtime-starttime)
    #
    # starttime = time.time()
    # study()
    # endtime = time.time()
    # print(endtime - starttime)


    # 假设有100个，需要计算时间，怎么办？
    # 装饰器
    game()