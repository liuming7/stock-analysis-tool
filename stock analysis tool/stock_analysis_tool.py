#导入类
from get_data import get_data
from draw_data import draw_data
get_data01 = get_data()
draw_data01 = draw_data()

i = 1
get_name = True

#界面：
while True:
    #选择操作
    str = '%s%s%s' % ('操作', i, ':')
    x = input(str)
    i+=1

    #退出
    if x=='quit' or i==102:
        print('what???')
        break


    #获取数据
    elif x=='get':
        print('ok,get and')
        y = input('which:')
        #获取单一公司一段时间股票
        if y=='stockdata':
            get_name = get_data01.get_stockData(get_name)
            print('stockdata done')
        #获取500强公司数据
        elif y=='sp500n':
            get_data01.get_SP500Data()
            print('SP500N done')
        #无效输入
        else:
            print('not found')


    #画图
    elif x=='draw':
        print('ok,draw and')
        y = input('which:')
        #画十日均线图
        if y=='10ma':
            draw_data01.draw_10ma()
            print('draw_10ma done')
        #画蜡烛图
        elif y=='candle':
            draw_data01.draw_candle()
            print('draw_candle done')
        #无效输入
        else:
            print('not found')


    #整合
    elif x=='compile':
        print('no')


    #无效输入
    else:
        print('are u really a developer')


