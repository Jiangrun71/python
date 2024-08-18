import pyautogui
import threading
import keyboard
import time
from tqdm import tqdm

# 切换到桌面的函数
def switch_to_desktop():
    pyautogui.hotkey('winleft', 'd')
    print("Switched to Desktop")
    time.sleep(1)

def switch_to_wechat():
    pyautogui.click(x=1048, y=1419)
    print("Switched to WeChat")
    time.sleep(1)

def switch_to_browser():
    pyautogui.click(x=438, y=1418)
    print("Switched to browser")
    time.sleep(1)

def switch_to_moba():
    pyautogui.click(x=520, y=1413)
    print("Switched to MOBA")
    time.sleep(1)

def jindutiao(pause_event, stop_event):
    with tqdm(total=500) as pbar:
        for i in range(500):
            if stop_event.is_set():
                print("\nStopping due to user request")
                break
            pause_event.wait()  # 阻塞直到 pause_event 被设置
            time.sleep(1)
            pbar.update(1)

def main_process_func(pause_event, stop_event):
    switch_to_desktop()
    jindutiao(pause_event, stop_event)
    if stop_event.is_set(): return
    switch_to_wechat()
    jindutiao(pause_event, stop_event)
    if stop_event.is_set(): return
    switch_to_browser()
    jindutiao(pause_event, stop_event)
    if stop_event.is_set(): return
    switch_to_browser()
    jindutiao(pause_event, stop_event)

pause_event = threading.Event()
pause_event.set()
stop_event = threading.Event()

def toggle_pause():
    if pause_event.is_set():
        pause_event.clear()
        print("Paused")
    else:
        pause_event.set()
        print("Resumed")

def stop_program():
    stop_event.set()
    print("Stopping the program")

def monitored_process():
    while not stop_event.is_set():
        try:
            pause_event.wait()
            main_process_func(pause_event, stop_event)
        except KeyboardInterrupt:
            print("\nProgram stopped by user")
            stop_event.set()
            break

def main():
    # 设置快捷键
    keyboard.add_hotkey('p', toggle_pause)
    keyboard.add_hotkey('q', stop_program)

    # 启动监控线程
    process_thread = threading.Thread(target=monitored_process)
    process_thread.start()

    # 等待线程结束
    try:
        process_thread.join()
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
        stop_event.set()
        process_thread.join()

if __name__ == "__main__":
    main()
