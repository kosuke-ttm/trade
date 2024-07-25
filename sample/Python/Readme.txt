【前提】
・PCにpython3がインストールされていること。
・PUSH配信(websocket)をするには、python3のインストール後にコマンドプロンプトにて以下のコマンドを実行する。
コマンド：py -m pip install websocket-client


【注意】
「token.py」ファイル名は、pythonで予約とされているため使用できません。

TradeModule.pyの構造
１．トークン発行
get_token(password)
※１で発行したtokenを２以降の各ファイル内の「X-API-KEY」に指定する

２．注文発注（現物）
（１）買
sendorder_cash_buy(key)

（２）売
sendorder_cash_sell(key)

３．注文発注（信用）
（１）新規
sendorder_margin_new(key)

（２）新規_プレミアム料入札
endorder_margin_daytrade(key)

（３）返済（決済順序）
sendorder_margin_pay_ClosePositionOrder(key)

（４）返済（返済建玉指定）
kabusapi_sendorder_margin_pay_ClosePositions(key)

４．注文発注（先物）
（１）新規
sendorder_future_new(key)

（２）返済（決済順序）
sendorder_future_pay_ClosePositionOrder(key)

（３）返済（返済建玉指定）
sendorder_future_pay_ClosePositions(key)

５．注文発注（OP）
（１）新規
sendorder_option_new(key)

（２）返済（決済順序）
sendorder_option_pay_ClosePositionOrder(key)

（３）返済（返済建玉指定）
sendorder_option_pay_ClosePositions(key)

６．注文取消
cancelorder(key,password)

７．取引余力（現物）（信用）（先物）（OP）
capacity(key)

11．時価情報・板情報
board(key)

12．銘柄情報
symbol_info(key)

13．注文約定照会
orders(key)

14．残高照会
positions(key)

15．先物銘柄コード取得
symbolname_future(key)

16．オプション、ミニオプション(限月)銘柄コード取得
symbolname_option(key)

17．PUSH配信開始はmain関数で実装
コマンド：python kabusapi_websocket.py

18．銘柄登録・解除
register(key)

21. 詳細ランキング
ranking(key)

22. 為替情報
exchange(key)

23. 規制情報
regulations(key)

24. 優先市場
primaryexchange(key)

25. ソフトリミット
apisoftlimit(key)

26. プレミアム料取得
marginpremium(key)

27．ミニオプション(限週)銘柄コード取得
symbolname_minioptionweekly(key)


// ライセンスについて
Copyright (c) 2020 au Kabucom Securities Co., Ltd.
Released under the MIT license
https://opensource.org/licenses/mit-license.php
