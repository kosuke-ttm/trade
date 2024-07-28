import pyautogui
import time
import TradeModule as tm

# while True:
#     x, y = pyautogui.position()
#     print(f'X: {x}, Y: {y}')
#     time.sleep(1)  # 1秒ごとに位置を表示

token = '****'
user_id = '****'
message = 'success login'

tm.send_line_message(token, user_id, message)