import pyautogui
import time

# 現在のマウス位置を取得
while True:
    current_x, current_y = pyautogui.position()
    print(f'マウス位置: ({current_x}, {current_y})')
    time.sleep(1)
