import pandas as pd
from pickle_dump import getAllDatas
from filter import filter

def save_all():
    datas = getAllDatas()
    pd.DataFrame(datas).to_csv('校园司令.csv', encoding="utf_8_sig")

if __name__ == '__main__':
    list = filter('editor', '名字')

    url = 'http://www.shwilling.com/portal/index/detail/'
    for item in list:
        item['url'] = url + item['id']
        print(item['url'])
    pd.DataFrame(list).to_csv('名字.csv', encoding="utf_8_sig")