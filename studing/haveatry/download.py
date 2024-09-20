import pyautogui
import time
from tqdm import tqdm
# 切换到桌面的函数
def switch_to_desktop():
    pyautogui.hotkey('winleft', 'd')  # 使用 Win + D 快捷键切换到桌面
    print("Switched to Desktop")
    time.sleep(1)  # 等待1秒钟，避免频繁操作造成问题

def downloadfile():
    switch_to_desktop()
    time.sleep(2)
    #点击按钮下载
    pyautogui.click(x=2562, y=632)
    pyautogui.click(x=26234, y=723)
    time.sleep(3)
    #进到下载界面，点击保存 ,位置固定不变
    pyautogui.click(x=3415, y=2197)
    time.sleep(2)

    pyautogui.click(x=2555, y=736)
    pyautogui.click(x=2644, y=830)
    time.sleep(3)
    # 进到下载界面，点击保存 ,位置固定不变
    pyautogui.click(x=3415, y=2197)
    time.sleep(2)

    pyautogui.click(x=2555, y=844)
    pyautogui.click(x=2644, y=935)
    time.sleep(3)
    #进到下载界面，点击保存 ,位置固定不变
    pyautogui.click(x=3415, y=2197)
    time.sleep(2)

    pyautogui.click(x=2555, y=946)
    pyautogui.click(x=2644, y=1034)
    time.sleep(3)
    # 进到下载界面，点击保存 ,位置固定不变
    pyautogui.click(x=3415, y=2197)
    time.sleep(2)

    pyautogui.click(x=2555, y=1054)
    pyautogui.click(x=2644, y=1145)
    time.sleep(3)
    # 进到下载界面，点击保存 ,位置固定不变
    pyautogui.click(x=3415, y=2197)
    time.sleep(2)
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