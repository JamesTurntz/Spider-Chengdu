from pyquery import PyQuery as pq
import pandas as pd
import codecs
import time

name = ['楼盘', '均价', '位置', '链接']
dataList = []

for page in range(1, 31):
    _url = 'https://cd.fang.anjuke.com/loupan/all/p' + str(page) + '/'
    d = pq(url=_url)
    root = d('.key-list').find('.item-mod')
    items = root.find('.items-name')
    princes = root.find('.favor-pos').find('span')
    maps = root.find('.list-map')
    lps = root.find('.lp-name')
    for i in range(len(items)):
        tempList = []
        tempList.append(items.eq(i).text())
        tempList.append(princes.eq(i).text())
        tempList.append(maps.eq(i).text())
        tempList.append(lps.eq(i).text())
        dataList.append(tempList)

    time.sleep(0.2)
    print('page ' + str(page) + ' ok')

f = codecs.open('loupan.csv', 'w', "utf-8-sig")
pd.DataFrame(columns=name, data=dataList).to_csv(f)
