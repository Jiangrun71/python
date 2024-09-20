import pyautogui
import time
from tqdm import tqdm
# 切换到桌面的函数

def downloadfile():    # 假设企业微信的图标在任务栏的第一个位置，点击打开或者切换
    pyautogui.click(x=1048, y=1419)  # 替换成你企业微信在屏幕上的位置坐标
    print("Switched to WeChat")
    time.sleep(1)  # 等待1秒钟，避免频繁操作造成问题
# 主程序，每隔10秒进行一次窗口切换
if __name__ == "__main__":
    try:
        while True:
            switch_to_wechat()  # 切换到企业微信
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nProgram stopped by user")

