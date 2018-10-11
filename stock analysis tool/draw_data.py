class draw_data(object):


    def draw_10ma(self):#画十日均线图

        #导入包
        import pandas as pd
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates
        import mpl_finance as mpf
        import glob

        #获取文件列表
        for filename in glob.glob(r'c:\\Users\\biaoc\\Desktop\\py_tools\\stock analysis tool\\*.csv'):
            print (filename)

        #输入文件名
        ticker = input('ticker:')
        #导入数据
        df = pd.read_csv(ticker,parse_dates=True,index_col=0)
        
        #十日均线
        df['10ma'] = df['Adj Close'].rolling(window=10,min_periods=0).mean()

        #坐标轴
        ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
        ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)

        #绘图(折线图）
        ax1.plot(df.index,df['Adj Close'])
        ax1.plot(df.index,df['10ma'])
        ax2.bar(df.index,df['Volume'])
        
        plt.show()

        


    def draw_candle(self):#画蜡烛图
        #导入包
        import pandas as pd
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates
        import mpl_finance as mpf
        import glob

        for filename1 in glob.glob(r'c:\\Users\\biaoc\\Desktop\\py_tools\\stock analysis tool\\*.csv'):
            print (filename1)

        filename = input('filename:')
        #导入数据
        try:
            df = pd.read_csv(filename,parse_dates=True,index_col=0)
        except:
            print("fliename is wrong")
        else:
            #价格平均，交易量求和
            df_ohlc = df['Adj Close'].resample('10D').ohlc()
            df_volume = df['Volume'].resample('10D').sum()

            #时间重置
            df_ohlc.reset_index(inplace=True)
            df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

            #作图（分区域）
            fig = plt.figure()
            ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
            ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)
            ax1.xaxis_date()

            #作图（生成蜡烛图）
            mpf.candlestick_ohlc(ax1,df_ohlc.values,width=5,colorup='g')
            ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)

            plt.show()






