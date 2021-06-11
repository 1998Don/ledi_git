import os
import time

class ScreenRobot:
    def screen(self,count):
        # 截屏
        os.system(f"adb shell screencap -p /sdcard/{count}.png")


if __name__ == '__main__':
    count = 1
    robot = ScreenRobot()
    while True:
        try:
            robot.screen(count)
            os.system(f"adb pull -a /sdcard/{count}.png")
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), f'picture{count}.png')
            time.sleep(0.5)
            count += 1
        except:
            break