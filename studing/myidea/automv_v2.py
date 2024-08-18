import pyautogui
import time
from tqdm import tqdm
# 切换到桌面的函数
def switch_to_desktop():
    pyautogui.hotkey('winleft', 'd')  # 使用 Win + D 快捷键切换到桌面
    print("Switched to Desktop")
    time.sleep(1)  # 等待1秒钟，避免频繁操作造成问题

def switch_to_wechat():    # 假设企业微信的图标在任务栏的第一个位置，点击打开或者切换
    pyautogui.click(x=1048, y=1419)  # 替换成你企业微信在屏幕上的位置坐标
    print("Switched to WeChat")
    time.sleep(1)  # 等待1秒钟，避免频繁操作造成问题
def switch_to_broswer():
    pyautogui.click(x=438, y=1418)
    print("switch to broswer")
    time.sleep(1)
# 主程序，每隔10秒进行一次窗口切换
if __name__ == "__main__":
    try:
        while True:
            switch_to_desktop()  # 切换到桌面
            for i in tqdm(range(500)):
                time.sleep(1)
            switch_to_wechat()  # 切换到企业微信
            for i in tqdm(range(500)):
                time.sleep(1)
            switch_to_broswer()
            for i in tqdm(range(500)):
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
# import pyautogui
# import time
# from tqdm import tqdm
#
#
# def switch_apps():
#     # 模拟按键操作切换桌面和企业微信
#     pyautogui.hotkey('alt', 'tab')
#     time.sleep(1)  # 等待切换完成
#
#
# def main():
#     try:
#         while True:
#             switch_apps()
#             # 打印间隔时间进度
#             for i in tqdm(range(100)):
#
#                 time.sleep(1)
#
#             print("")  # 换行以显示下一个循环开始的消息
#
#     except KeyboardInterrupt:
#         print("\nProgram manually terminated.")
#
#
# if __name__ == "__main__":
#     main()

