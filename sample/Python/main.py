import TradeModule as tm
import sys
import websocket
import _thread
import pandas as pd
import json
import matplotlib.pyplot as plt
import configparser
import pyautogui
import time
import subprocess
import logging

# ログの設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# データフレームのインデックス
# ClearingPrice,Exchange,ExchangeName,TradingVolume,TradingVolumeTime,VWAP,TradingValue,BidQty,BidPrice,BidSign,AskQty,AskPrice,AskSign,Symbol,SymbolName,CurrentPrice,CurrentPriceTime,CurrentPriceChangeStatus,CurrentPriceStatus,CalcPrice,PreviousClose,PreviousCloseTime,ChangePreviousClose,ChangePreviousClosePer,OpeningPrice,OpeningPriceTime,HighPrice,HighPriceTime,LowPrice,LowPriceTime,SecurityType,Sell1,Sell2,Sell3,Sell4,Sell5,Sell6,Sell7,Sell8,Sell9,Sell10,Buy1,Buy2,Buy3,Buy4,Buy5,Buy6,Buy7,Buy8,Buy9,Buy10

conf = configparser.ConfigParser()
conf.read('sample/Python/PersonalInformation.ini')

# 個人情報入力
APIPassword = conf["aukabu"]["APIPassword"]
Password = conf["aukabu"]["Password"]
line_token = conf["aukabu"]["Linetoken"]
line_user_id = conf["aukabu"]["Lineuserid"]
application_pass = conf["aukabu"]["Appid"]

#以下は１日１回実行すればよい
'''
# アプリケーションの起動
subprocess.Popen(application_pass)
# アプリケーションが起動するまで待機
time.sleep(3)
# ログイン画面での操作を自動化
# 例: パスワードの入力
pyautogui.click(1073, 586)
pyautogui.write(Password)
# 例: ログインボタンをクリック2118030762
pyautogui.click(1231, 655)
time.sleep(5)
conf["aukabu"]["Token"] = tm.get_token(APIPassword)
# 変更をINIファイルに書き戻す
with open('sample/Python/PersonalInformation.ini', 'w') as configfile:
    conf.write(configfile)
'''
#以上

token_value = conf["aukabu"]["Token"]


tm.register(token_value)

#websocket
def on_message(ws, message):
    try:
        # CSVファイルをデータフレームに読み込む
        df = pd.read_csv('./sample/Python/data/output.csv')
        if len(df)%1000 == 0:
            logging.info("1000行取り込みました")
        # # 5000行超えたら最初の50行を削除 
        # if len(df) > 4000:
        #     df = df.iloc[50:]
        #     # フィルタリングしたデータフレームを新しいCSVファイルとして保存（インデックスあり）
        #     df.to_csv('./sample/Python/data/output.csv')
        new_data = json.loads(message)
        # 新しいデータをデータフレームに追加
        new_row_df = pd.DataFrame([new_data])
        df2 = pd.concat([df, new_row_df], ignore_index=True)
        # # データフレームをcsvファイルに保存する
        df2.to_csv('./sample/Python/data/output.csv', index=False, encoding='utf-8')
    except Exception as e:
        logging.error(f'Error processing message: {e}')

def on_error(ws, error):
    logging.error(f'WebSocket error: {error}')
    # 再接続を試みる
    time.sleep(5)
    tm.send_line_message(line_token, line_user_id, "websocket再接続")
    a = input("もう一回つなぎますか？") #ウィンドウポップアップまたはLINEから許可できるようにしたい
    ws.run_forever()

def on_close(ws):
    tm.send_line_message(line_token, line_user_id, "websocket閉じられました")
    logging.info('WebSocket closed')


def on_open(ws):
    logging.info('WebSocket connected')
    def run(*args):
        while(True):
            line = sys.stdin.readline()
            if line:
                logging.info('Closing WebSocket')
                ws.close()
    _thread.start_new_thread(run, ())

url = 'ws://localhost:18080/kabusapi/websocket'
# websocket.enableTrace(True)
ws = websocket.WebSocketApp(url,
                        on_message = on_message,
                        on_error = on_error,
                        on_close = on_close)
ws.on_open = on_open



if tm.is_within_time_range():
    tm.send_line_message(line_token, line_user_id, "websocket実行")
    ws.run_forever()
else:
    print("取引時間外です")

# 参考にしたいサイト
# https://qiita.com/jkk-technologies/items/81f4424fa142ff3a6db1
