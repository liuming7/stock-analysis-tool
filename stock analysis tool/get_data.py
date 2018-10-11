class get_data(object):

    #获取单一公司一段时间股票
    def get_stockData(self,get_name):
        
        #导入包
        import bs4 as bs
        from prettytable import PrettyTable as pt
        import pickle
        import requests
        import datetime as dt
        import pandas_datareader as pdr#E01:版本0.5.0
        import pandas_datareader.data as web

        def sp500Name():
            #请求url
            resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
            #载入
            soup = bs.BeautifulSoup(resp.text,'lxml')
            #定位标签位置
            table = soup.find('table',{'class':'wikitable sortable'})
            
            tickers = []
            
            #查找并存储
            for row in table.findAll('tr')[1:]:
                #查找
                ticker=row.findAll('td')[0].text
                #存储
                tickers.append(ticker)

            tickers = list(set(tickers))
            #保存为.pickle
            with open('sp500tickers.pickle','wb') as f:
                pickle.dump(tickers,f)

            return tickers

        try:
            if get_name == True:
                #获取代号
                tickers = sp500Name()
                tickers_table = pt(["1","2","3","4","5","6","7","8","9","10"])
        
                #补全数据
                for va in range(len(tickers)%10):
                    tickers.append("N/A")
        
                #制表
                for n in range(int(len(tickers)/10)):
                    start = 0+10*n
                    end = 10+10*n
                    tickers_table.add_row(tickers[start:end])
        
                #显示
                print(tickers_table)
                get_name = False
                
        except:
            print("try again,crash at table")

        else:
            #输入查询信息
            print('shape as yyyymmdd')
            time_s = input('start:')
            time_e = input('end:')
            ticker_i = input('ticker:')

            try:
                #声明时间段
                start = dt.datetime(int(time_s[0:4]),int(time_s[4:6]),int(time_s[6:8]))
                end = dt.datetime(int(time_e[0:4]),int(time_e[4:6]),int(time_e[6:8]))

                #获取数据集
                df = pdr.get_data_yahoo(ticker_i,start,end)#获取特斯拉的股票    #E01-s:安装fix-yahoo-finance-0.0.21,已解决报错问题
                #df=web.DataReader('TSLA','yahoo',start,end)    ----暂不可用
                #print(df.head())

                #存为.csv文件
                filename = ticker_i + '-' + time_s + '-' + time_e + '.csv'
                df.to_csv(filename)
            except:
                print("try again,crash at data")
        return(get_name)


    #获取标普500公司数据
    def get_SP500Data(self):
        
        #导入包
        import bs4 as bs
        import pickle
        import requests
        import os
        import pandas as pd
        import pandas_datareader as pdr
        import datetime as dt

        #内置爬虫，爬取500公司名单
        def save_sp500Name():
            #请求url
            resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
            #载入
            soup = bs.BeautifulSoup(resp.text,'lxml')
            #定位标签位置
            table = soup.find('table',{'class':'wikitable sortable'})
            
            tickers = []
            
            #查找并存储
            for row in table.findAll('tr')[1:]:
                #查找
                ticker=row.findAll('td')[0].text
                #存储
                tickers.append(ticker)

            #保存为.pickle
            with open('sp500tickers.pickle','wb') as f:
                pickle.dump(tickers,f)

            return tickers
        #save_sp500Name()


        #内置爬虫，分别爬取500公司数据
        def get_data_from_yahoo(isReload=False):

            #设置reload，选择从文件导入还是即时生成
            if isReload:#即时生成
                tickers = save_sp500Name()
            else:#导入
                with open('sp500tickers.pickle','rb') as f:
                    tickers = pickle.load(f)

            #新建文件夹
            if not os.path.exists('stock_dfs'):
                os.makedirs('stock_dfs')

            #爬虫参数
            start = dt.datetime(2016,1,1)
            end = dt.datetime(2017,1,1)

            proc=len(tickers)

            #爬取
            for ticker in tickers:
                print(proc)#剩余个数
                
                #校验是否已下载，若无则下载
                if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
                    df = pdr.get_data_yahoo(ticker,start,end)#下载
                    df.to_csv('stock_dfs/{}.csv'.format(ticker))#保存
                    print('DC {}'.format(ticker))
                #若有，则过
                else:
                    print('AH {}'.format(ticker))

                proc-=1

        get_data_from_yahoo(True)






