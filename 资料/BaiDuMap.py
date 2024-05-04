import random
import time
import os
import requests
import pandas
import openpyxl
import urllib3


class BaiDuMap:
    def __init__(self, kwd=None, pn=1):
        self.headers = {
            'Host': 'apis.map.qq.com',
            'Connection': 'keep-alive',
            'referer': 'https://servicewechat.com/wxb9cc6573ae84aa63/10/page-frame.html',
            'xweb_xhr': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6919',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh'}
        self.kwd = kwd
        self.pn = pn

    def params(self):
        print(f'第{self.pn}页采集中')
        i = 0
        for i in range(self.pn):
            x = '%6d' % random.randint(111111, 999999)
            y = '%6d' % random.randint(111111, 999999)
            i += 1
            url = f'https://apis.map.qq.com/ws/place/v1/search?key=I36BZ-2Z3KD-7CB4E-HWHAQ-F2V6Q-WTFFV&boundary=nearby(34.{x}%2C108.{y}%2C1000%2C1)&keyword={self.kwd}&page_index={i}'
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            response = requests.get(url=url, headers=self.headers, verify=False).json()
            try:
                if response['message'] == '此key每日调用量已达到上限':
                    print(response['message'])
                    break
                if self.pn <= 1:
                    break
                if response['data']:
                    data_list = response['data']
                    self.pn = self.pn - i
                    self.get_info(datas=data_list)
            except Exception as e:
                import sys
                sys.setrecursionlimit(1000000)
                print(e)
                return self.params()

    def get_info(self, datas=None):
        title = []
        address = []
        telphone = []
        category = []
        province = []
        city = []
        aero = []
        for data in datas:
            if data['ad_info']['city'] == '西安市':
                title.append(data['title'])
                address.append(data['address'])
                if data['tel']:
                    telphone.append(data['tel'])
                else:
                    telphone.append('/')
                category.append(data['category'])
                province.append(data['ad_info']['province'])
                city.append(data['ad_info']['city'])
                aero.append(data['ad_info']['district'])
        infos = {
            '名称': title,
            '地址': address,
            '电话': telphone,
            '分类': category,
            '省份': province,
            '城市': city,
            '区域': aero,
        }
        if title:
            print(f'{self.kwd}下载中......')
            self.to_excel(frame=infos)
        elif len(title) == 0:
            import sys
            sys.setrecursionlimit(1000000)
            print('换下一个区域')
            return self.params()

    def to_excel(self, frame=None):
        df = pandas.DataFrame(frame)
        if os.path.exists(f'{self.kwd}.xlsx'):
            old = pandas.read_excel(f'{self.kwd}.xlsx')
            new = old._append(pandas.DataFrame(df))
            new.to_excel(f'{self.kwd}.xlsx', index=False, engine='openpyxl')
        else:
            df.to_excel(f'{self.kwd}.xlsx', index=False, engine='openpyxl')

    def duplicated(self):
        try:
            old = pandas.read_excel(f'{self.kwd}.xlsx')
            new = old.drop_duplicates(keep=False)
            new.to_excel(f'{self.kwd}.xlsx', index=False, engine='openpyxl')
            print(new)
        except Exception as e:
            print(e)

    def start(self, kw_list=None):
        for kw in kw_list:
            self.kwd = kw
            self.params()
            self.duplicated()

 
if __name__ == '__main__':
    kw_list = ['酒店']
    baidu = BaiDuMap(pn=2)
    baidu.start(kw_list=kw_list)
