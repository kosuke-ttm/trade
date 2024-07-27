import TradeModule as tm
import matplotlib.pyplot as plt
import pandas as pd
import configparser

conf = configparser.ConfigParser()
conf.read('sample/Python/PersonalInformation.ini')

# 個人情報入力
APIPassword = conf["aukabu"]["APIPassword"]
token_value = conf["aukabu"]["Token"]
Password = conf["aukabu"]["Password"]

# tm.get_token(APIPassword)

# tm.register(token_value)
df = pd.read_csv('./sample/Python/data/output.csv')

first_column_data = df['BidPrice']
second_column_data = df['CurrentPriceTime']

plt.xlabel('BidPrice')
plt.ylabel('Time')
plt.plot(first_column_data, second_column_data, linestyle='solid', marker='o')
plt.show()