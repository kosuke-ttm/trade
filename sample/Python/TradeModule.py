import urllib.request
import json
import pprint

# リクエストレスポンスするための関数
def fetch_data(res):
    req = res
    try:
        with urllib.request.urlopen(req) as res:
            # print(res.status, res.reason)
            # for header in res.getheaders():
            #     print(header)
            # print()
            content = json.loads(res.read())
            # pprint.pprint(content)
            return content
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
        return None
    except Exception as e:
        print(e)
        return None

# APIトークンを発行する関数
def get_token(password):
    obj = { 'APIPassword': password }
    json_data = json.dumps(obj).encode('utf8')
    url = 'http://localhost:18080/kabusapi/token'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    ans = fetch_data(req)
    print(ans['Token'])
    return ans['Token']

#先物銘柄コード取得
def symbolname_future(key):
    url = 'http://localhost:18080/kabusapi/symbolname/future'
    params = { 'FutureCode': 'NK225mini', 'DerivMonth': 202409 }

    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    print(fetch_data(req))

#時価情報・板情報取得
def board(key):
    # url = 'http://localhost:18080/kabusapi/board/5401@1'
    url = 'http://localhost:18080/kabusapi/board/169090019@2'
    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

#銘柄登録（削除もできる）
def register(key):
    obj = { 'Symbols':
        [ 
            # {'Symbol': '169090018', 'Exchange': 2},
            {'Symbol': '169090019', 'Exchange': 2}
        ] }
    json_data = json.dumps(obj).encode('utf8')

    #全削除するときは↓ 
    # url = 'http://localhost:18080/kabusapi/unregister/all'
    # req = urllib.request.Request(url, method='PUT')
    # 一部を削除したいときは↓json_dataに削除したいものを格納（書き方は登録するときと同じ）
    # url = 'http://localhost:18080/kabusapi/unregister'
    # req = urllib.request.Request(url, json_data, method='PUT')

    url = 'http://localhost:18080/kabusapi/register'
    req = urllib.request.Request(url, json_data, method='PUT')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    print(fetch_data(req))

# 取引余力
def capacity(key):
    # url = 'http://localhost:18080/kabusapi/wallet/margin' # 信用
    # url = 'http://localhost:18080/kabusapi/wallet/cash' # 現物
    url = 'http://localhost:18080/kabusapi/wallet/future' # 先物
    # url = 'http://localhost:18080/kabusapi/wallet/future/169090019@24' # 先物mini 24/09
    # url = 'http://localhost:18080/kabusapi/wallet/option' # OP

    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    print(fetch_data(req))

# 注文取消
def canceloder(key,password):
    obj = { 'OrderID': '20200709A02N04712032', 'Password': password }
    json_data = json.dumps(obj).encode('utf8')

    url = 'http://localhost:18080/kabusapi/cancelorder'
    req = urllib.request.Request(url, json_data, method='PUT')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    print(fetch_data(req))

# 銘柄情報
def symbol_info(key):
    url = 'http://localhost:18080/kabusapi/symbol/169090019@2'
    params = { 'addinfo': 'true' } # true:追加情報を出力する、false:追加情報を出力しない　※追加情報は、「時価総額」、「発行済み株式数」、「決算期日」、「清算値」を意味します
    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

#ソフトリミット
def apisoftlimit(key):
    url = 'http://localhost:18080/kabusapi/apisoftlimit'
    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    print(fetch_data(req))

# 為替情報
def exchange(key):
    url = 'http://localhost:18080/kabusapi/exchange/usdjpy'
    #いずれの通貨ペアを指定してください：usdjpy、eurjpy、gbpjpy、audjpy、chfjpy、cadjpy、nzdjpy、zarjpy、eurusd、gbpusd、audusd
    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 詳細ランキング
def ranking(key):
    url = 'http://localhost:18080/kabusapi/ranking' #?type=1&ExchangeDivision=ALL
    params = { 'type': 15 } #type - 1:値上がり率（デフォルト）2:値下がり率 3:売買高上位 4:売買代金 5:TICK回数 6:売買高急増 7:売買代金急増 8:信用売残増 9:信用売残減 10:信用買残増 11:信用買残減 12:信用高倍率 13:信用低倍率 14:業種別値上がり率 15:業種別値下がり率
    params['ExchangeDivision'] = 'ALL' #ExchangeDivision - ALL:全市場（デフォルト）T:東証全体 TP:東証プライム TS:東証スタンダード TG:東証グロース M:名証 FK:福証 S:札証
    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 規制情報
def regulations(key):
    url = 'http://localhost:18080/kabusapi/regulations/9433@1'
    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（先物）新規
def sendorder_future_new(key):
    obj = { 'Password': '123456',
            'Symbol': '165120018',
            'Exchange': 23,
            'TradeType': 1,
            'TimeInForce': 2,
            'Side': '2',
            'Qty': 3,
            'FrontOrderType': 30,
            'Price': 22000,
            'ExpireDay': 0,
            'ReverseLimitOrder': {
                                'TriggerPrice': 26010,
                                'UnderOver': 2, #1.以下 2.以上
                                'AfterHitOrderType': 1, #1.成行 2.指値
                                'AfterHitPrice': 0
                                }
        }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder/future'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（先物）返済（決済順序）
def sendorder_future_pay_ClosePositionOrder(key):
    obj = { 'Password': '123456',
            'Symbol': '165120018',
            'Exchange': 23,
            'TradeType': 2,
            'TimeInForce': 2,
            'Side': '2',
            'Qty': 3,
            'ClosePositionOrder': 1,
            'FrontOrderType': 30,
            'Price': 22000,
            'ExpireDay': 0,
            'ReverseLimitOrder': {
                                'TriggerPrice': 26010,
                                'UnderOver': 2, #1.以下 2.以上
                                'AfterHitOrderType': 1, #1.成行 2.指値
                                'AfterHitPrice': 0
                                }
        }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder/future'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（先物）返済（返済建玉指定）
def sendorder_future_pay_ClosePositions(key):
    obj = { 'Password': '123456',
            'Symbol': '165120018',
            'Exchange': 23,
            'TradeType': 2,
            'TimeInForce': 1,
            'Side': '2',
            'Qty': 3,
            'ClosePositions': [
                            {'HoldID':'E20200924*****','Qty':2},
                            {'HoldID':'E20200924*****','Qty':1}
                            ],
            'FrontOrderType': 20,
            'Price': 22000,
            'ExpireDay': 0,
            'ReverseLimitOrder': {
                                'TriggerPrice': 26010,
                                'UnderOver': 2, #1.以下 2.以上
                                'AfterHitOrderType': 1, #1.成行 2.指値
                                'AfterHitPrice': 0
                                }
            }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder/future'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文約定照会
def orders(key):
    url = 'http://localhost:18080/kabusapi/orders'
    params = { 'product': 0 }               # product - 0:すべて、1:現物、2:信用、3:先物、4:OP
    #params['id'] = '20201207A02N04830518' # id='xxxxxxxxxxxxxxxxxxxx'
    #params['updtime'] = 20201101123456    # updtime=yyyyMMddHHmmss
    #params['details'] =  'false'          # details='true'/'false'
    #params['symbol'] = '9433'             # symbol='xxxx'
    #params['state'] = 5                   # state - 1:待機（発注待機）、2:処理中（発注送信中）、3:処理済（発注済・訂正済）、4:訂正取消送信中、5:終了（発注エラー・取消済・全約定・失効・期限切れ）
    #params['side'] = '2'                  # side - '1':売、'2':買
    #params['cashmargin'] = 3              # cashmargin - 2:新規、3:返済

    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 残高照会
def positions(key):
    url = 'http://localhost:18080/kabusapi/positions'
    params = { 'product': 0 }   	# product - 0:すべて、1:現物、2:信用、3:先物、4:OP
    params['symbol'] = '9433'  		# symbol='xxxx'
    params['side'] = '1' 				# 1:売、2:買
    params['addinfo'] = 'false' 	# true:追加情報を出力する、false:追加情報を出力しない　※追加情報は、「現在値」、「評価金額」、「評価損益額」、「評価損益率」を意味します
    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# オプション、ミニオプション(限月)銘柄コード取得
def symbolname_option(key):
    url = 'http://localhost:18080/kabusapi/symbolname/option'
    #params = { 'OptionCode': 'NK225op', 'DerivMonth': 202306, 'PutOrCall': 'C', 'StrikePrice': 27250 }
    params = { 'OptionCode': 'NK225miniop', 'DerivMonth': 202306, 'PutOrCall': 'C', 'StrikePrice': 27250 }

    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 優先市場
def primaryexchange(key):
    url = 'http://localhost:18080/kabusapi/primaryexchange/9433'
    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# プレミアム料取得
def marginpremium(key):
    url = 'http://localhost:18080/kabusapi/margin/marginpremium/6502'
    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# ミニオプション(限週)銘柄コード取得
def symbolname_minioptionweekly(key):
    url = 'http://localhost:18080/kabusapi/symbolname/minioptionweekly'
    params = { 'DerivMonth': 202306, 'DerivWeekly': 1, 'PutOrCall': 'C', 'StrikePrice': 27250 }

    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（現物）買
def sendorder_cash_buy(key):
    obj = { 'Password': '123456',
            'Symbol': '9433',
            'Exchange': 1,
            'SecurityType': 1,
            'Side': '2',
            'CashMargin': 1,
            'DelivType': 2,
            'FundType': 'AA',
            'AccountType': 2,
            'Qty': 100,
            'FrontOrderType': 30,
            'Price': 2762.5,
            'ExpireDay': 0,
            'ReverseLimitOrder': {
                                'TriggerSec': 3, #1.発注銘柄 2.NK225指数 3.TOPIX指数
                                'TriggerPrice': 1600,
                                'UnderOver': 2, #1.以下 2.以上
                                'AfterHitOrderType': 1, #1.成行 2.指値 3. 不成
                                'AfterHitPrice': 0
                                }
            }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（現物）売
def sendorder_cash_sell(key):
    obj = { 'Password': '123456',
            'Symbol': '9433',
            'Exchange': 1,
            'SecurityType': 1,
            'Side': '1',
            'CashMargin': 1,
            'DelivType': 0,
            'FundType': '  ',
            'AccountType': 2,
            'Qty': 100,
            'FrontOrderType': 30,
            'Price': 2762.5,
            'ExpireDay': 0,
            'ReverseLimitOrder': {
                                'TriggerSec': 1, #1.発注銘柄 2.NK225指数 3.TOPIX指数
                                'TriggerPrice': 2600,
                                'UnderOver': 1, #1.以下 2.以上
                                'AfterHitOrderType': 1, #1.成行 2.指値 3. 不成
                                'AfterHitPrice': 0
                                }
            }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（信用）新規
def sendorder_margin_new(key):
    obj = { 'Password': '123456',
            'Symbol': '9433',
            'Exchange': 1,
            'SecurityType': 1,
            'Side': '2',
            'CashMargin': 2,
            'MarginTradeType': 2,
            'DelivType': 0,
            'AccountType': 2,
            'Qty': 100,
            'FrontOrderType': 30,
            'Price': 2762.5,
            'ExpireDay': 0,
            'ReverseLimitOrder': {
                                'TriggerSec': 2, #1.発注銘柄 2.NK225指数 3.TOPIX指数
                                'TriggerPrice': 30000,
                                'UnderOver': 2, #1.以下 2.以上
                                'AfterHitOrderType': 2, #1.成行 2.指値 3. 不成
                                'AfterHitPrice': 8435
                                }
        }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（信用）新規_プレミアム料入札
def sendorder_margin_daytrade(key):
    obj = { 'Password': '111111',
            'Symbol': '5104',
            'Exchange': 1,
            'SecurityType': 1,
            'Side': '1',
            'CashMargin': 2,
            'MarginTradeType': 3,
            'MarginPremiumUnit': 422,
            'DelivType': 0,
            'AccountType': 2,
            'Qty': 100,
            'FrontOrderType': 20,
            'Price': 425,
            'ExpireDay': 0
        }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（信用）返済（決済順序）
def sendorder_margin_pay_ClosePositionOrder(key):
    obj = { 'Password': '123456',
            'Symbol': '9433',
            'Exchange': 1,
            'SecurityType': 1,
            'Side': '1',
            'CashMargin': 3,
            'MarginTradeType': 2,
            'DelivType': 2,
            'AccountType': 2,
            'Qty': 100,
            'ClosePositionOrder': 1,
            'FrontOrderType': 30,
            'Price': 2762.5,
            'ExpireDay': 0,
            'ReverseLimitOrder': {
                                'TriggerSec': 2, #1.発注銘柄 2.NK225指数 3.TOPIX指数
                                'TriggerPrice': 30000,
                                'UnderOver': 2, #1.以下 2.以上
                                'AfterHitOrderType': 2, #1.成行 2.指値 3. 不成
                                'AfterHitPrice': 8435
                                }
        }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（信用）返済（返済建玉指定）
def sendorder_margin_pay_ClosePositions(key):
    obj = { 'Password': '123456',
            'Symbol': '9433',
            'Exchange': 1,
            'SecurityType': 1,
            'Side': '1',
            'CashMargin': 3,
            'MarginTradeType': 1,
            'DelivType': 2,
            'AccountType': 2,
            'Qty': 200,
            'ClosePositions': [
                                {'HoldID':'E20200924*****','Qty':100},
                                {'HoldID':'E20200924*****','Qty':100}
                            ],
            'FrontOrderType': 30,
            'Price': 2762.5,
            'ExpireDay': 0,
            'ReverseLimitOrder': {
                                'TriggerSec': 2, #1.発注銘柄 2.NK225指数 3.TOPIX指数
                                'TriggerPrice': 30000,
                                'UnderOver': 2, #1.以下 2.以上
                                'AfterHitOrderType': 2, #1.成行 2.指値 3. 不成
                                'AfterHitPrice': 8435
                                }
        }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（OP）新規
def sendorder_option_new(key):
    obj = { 'Password': '123456',
            'Symbol': '145123218',
            'Exchange': 23,
            'TradeType': 1,
            'TimeInForce': 2,
            'Side': '1',
            'Qty': 5,
            'FrontOrderType': 30,
            'Price': 0,
            'ExpireDay': 0,
            'ReverseLimitOrder': {
                                'TriggerPrice': 1150,
                                'UnderOver': 1, #1.以下 2.以上
                                'AfterHitOrderType': 1, #1.成行 2.指値
                                'AfterHitPrice': 0
                                }
        }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder/option'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（OP）返済（決済順序）
def sendorder_option_pay_ClosePositionOrder(key):
    obj = { 'Password': '123456',
            'Symbol': '145123218',
            'Exchange': 23,
            'TradeType': 2,
            'TimeInForce': 2,
            'Side': '2',
            'Qty': 1,
            'ClosePositionOrder': 1,
            'FrontOrderType': 30,
            'Price': 0,
            'ExpireDay': 0,
            'ReverseLimitOrder': {
                                'TriggerPrice': 1150,
                                'UnderOver': 1, #1.以下 2.以上
                                'AfterHitOrderType': 1, #1.成行 2.指値
                                'AfterHitPrice': 0
                                }
        }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder/option'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))

# 注文発注（OP）返済（返済建玉指定）
def sendorder_option_pay_ClosePositions(key):
    obj = { 'Password': '123456',
            'Symbol': '145123218',
            'Exchange': 23,
            'TradeType': 2,
            'TimeInForce': 2,
            'Side': '2',
            'Qty': 3,
            'ClosePositions': [{'HoldID':'E20200924*****','Qty':2},{'HoldID':'E20200924*****','Qty':1}],
            'FrontOrderType': 30,
            'Price': 0,
            'ExpireDay': 0,
            'ReverseLimitOrder': {
                                'TriggerPrice': 1150,
                                'UnderOver': 1, #1.以下 2.以上
                                'AfterHitOrderType': 1, #1.成行 2.指値
                                'AfterHitPrice': 0
                                }
        }
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder/option'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', key)
    pprint.pprint(fetch_data(req))