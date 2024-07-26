import TradeModule as tm
import sys
import websocket
import _thread
import pandas as pd
import json

# データフレームのインデックス
# ClearingPrice,Exchange,ExchangeName,TradingVolume,TradingVolumeTime,VWAP,TradingValue,BidQty,BidPrice,BidSign,AskQty,AskPrice,AskSign,Symbol,SymbolName,CurrentPrice,CurrentPriceTime,CurrentPriceChangeStatus,CurrentPriceStatus,CalcPrice,PreviousClose,PreviousCloseTime,ChangePreviousClose,ChangePreviousClosePer,OpeningPrice,OpeningPriceTime,HighPrice,HighPriceTime,LowPrice,LowPriceTime,SecurityType,Sell1,Sell2,Sell3,Sell4,Sell5,Sell6,Sell7,Sell8,Sell9,Sell10,Buy1,Buy2,Buy3,Buy4,Buy5,Buy6,Buy7,Buy8,Buy9,Buy10


APIPassword = '****'
token_value = '69d95847184849d49a2dcfe1cd218940'


# tm.get_token(APIPassword)

tm.register(token_value)

#websocket
def on_message(ws, message):
    # print('--- RECV MSG. --- ')
    #読み込みがされているかを出力
    print('.',end='')
    # CSVファイルをデータフレームに読み込む
    df = pd.read_csv('./sample/Python/data/output.csv')
    # 5000行超えたら最初の50行を削除 
    if len(df) > 4000:
        df = df.iloc[50:]
        # フィルタリングしたデータフレームを新しいCSVファイルとして保存（インデックスあり）
        df.to_csv('./sample/Python/data/output.csv')
    
    new_data = json.loads(message)
    # 新しいデータをデータフレームに追加
    new_row_df = pd.DataFrame([new_data])
    df2 = pd.concat([df, new_row_df], ignore_index=True)
    # # データフレームをcsvファイルに保存する
    df2.to_csv('./sample/Python/data/output.csv', index=False, encoding='utf-8')
    # print(message)

def on_error(ws, error):
    print('--- ERROR --- ')
    print(error)

def on_close(ws):
    print('--- DISCONNECTED --- ')

def on_open(ws):
    print('--- CONNECTED --- ')
    def run(*args):
        while(True):
            line = sys.stdin.readline()
            if line != '':
                print('closing...')
                ws.close()
    _thread.start_new_thread(run, ())

url = 'ws://localhost:18080/kabusapi/websocket'
# websocket.enableTrace(True)
ws = websocket.WebSocketApp(url,
                        on_message = on_message,
                        on_error = on_error,
                        on_close = on_close)
ws.on_open = on_open
ws.run_forever()

# 参考にしたいサイト
# https://qiita.com/jkk-technologies/items/81f4424fa142ff3a6db1