import yfinance as yf
import mplfinance as mpf

# 指定股票代碼和時間範圍
stock_symbol = '2330.TW'  # 台積電股票代碼
start_date = '2023-01-01'
end_date = '2024-03-13'

# 使用 yf.Ticker() 函數來獲取股票數據
stock_data = yf.Ticker(stock_symbol)

# 使用 history() 方法獲取歷史股價
historical_data = stock_data.history(start=start_date, end=end_date)

# 計算20日和50日移動平均線
historical_data['MA_20'] = historical_data['Close'].rolling(window=7).mean()  # 20日移動平均線
historical_data['MA_50'] = historical_data['Close'].rolling(window=30).mean()  # 50日移動平均線

# 計算黃金交叉點
historical_data['Golden_Cross'] = (historical_data['MA_20'] > historical_data['MA_50']) & (historical_data['MA_20'].shift(1) < historical_data['MA_50'].shift(1))

# 繪製K線圖和黃金交叉點
mpf.plot(historical_data, type='candle', mav=(20, 50), volume=True, style='charles', addplot=mpf.make_addplot(historical_data['Golden_Cross'], scatter=True, markersize=100, marker='^', color='red'), title='K-line chart with Golden Cross for 2330.TW')
