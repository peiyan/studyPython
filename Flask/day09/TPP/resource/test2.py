### 装饰器基本使用(带参数)


import time



# 带参数1/2/3/4    1~3学习  4玩游戏
def study_control(control):
    def isstudy(func):
        def study(*args, **kwargs):
            if control == 4:
                func(*args, **kwargs)
            else:
                print('我爱学习!!!')
        return study
    return isstudy


@study_control(4)
def game():
    time.sleep(1)
    print('正在玩游戏，我游戏我光荣....')
    time.sleep(2)



if __name__ == '__main__':
    game()
