import random
import time
import requests
import pandas
import openpyxl
import os
import json
from datetime import date
import re
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED

number = ''
list1 = []


# 获取K线数据
class Kline:
    with open('./system/cookie.json') as f:
        cookie = json.load(f)
        params = cookie['params']
        headers = cookie['ALL_headers']
        cookies = cookie['cookies']
        name = None

    def get_k(self, code=None):
        if code[2:] not in list1:
            self.params['secid'] = code
            response = requests.get(
                url='http://push2his.eastmoney.com/api/qt/stock/kline/get',
                cookies=self.cookies,
                headers=self.headers,
                params=self.params,
                verify=False,
            ).text[19:-2]
            time.sleep(random.randint(160, 200) / 100)
            data = eval(response)
            self.name = data['data']['code']
            date = []
            open = []
            close = []
            hight = []
            low = []
            turnover = []
            amplitude = []
            change_hands = []
            transactions = []
            increase = []
            amount = []
            for info in data['data']['klines']:
                info_list = info.split(',')
                date.append(info_list[0])
                open.append(info_list[1])
                close.append(info_list[2])
                hight.append(info_list[3])
                low.append(info_list[4])
                turnover.append(info_list[5])
                transactions.append(info_list[6])
                amplitude.append(info_list[7])
                increase.append(info_list[8])
                amount.append(info_list[9])
                change_hands.append(info_list[10])
            dataframe = {
                '时间': date,
                '开盘': open,
                '最高': hight,
                '最低': low,
                '收盘': close,
                '涨幅': increase,
                '振幅': amplitude,
                '总手': turnover,
                '金额': transactions,
                '换手率%': change_hands,
                '涨跌额': amount
            }
            dataframe = pandas.DataFrame(dataframe)
            dataframe.to_csv(f'./data/{self.name}.csv', index=False, encoding='utf-8')
            self.save_data()

    def save_data(self):
        data_number = len(os.listdir('./data'))
        list1.append(self.name)
        with open('./system/sys_code.json') as f:
            code_number = len(json.load(f)['code_list'])
            global number
            number = round(data_number / code_number * 100)
            print(f">>>>>>>>>>>>>>>>>{number}%下载中")


# 获取股票代码
class Stock_code:
    data = pandas.read_json('./system/sys_code.json')
    code_end = ''
    code_info = {}
    kline = Kline()

    # 获取系统股票代码
    def get_sys_code(self):
        for code in self.data['code_list']:
            if len(code) == 6:
                if code[0] == '0':
                    self.code_end = '0.' + code
                elif code[0] == '6':
                    self.code_end = '1.' + code
                else:
                    print('input error')
            elif len(code) == 8:
                if 'SZ' in code:
                    self.code_end = '0.' + code[2:]
                elif 'SH' in code:
                    self.code_end = '1.' + code[2:]
                elif 'BJ' in code:
                    self.code_end = 'BJ' + code  # xueqiu.txt
                else:
                    print('input error')
                self.code_info[f'{self.code_end}'] = date.today().ctime()
            else:
                print('error')
        try:
            with ThreadPoolExecutor(max_workers=20) as tp:
                all_task = [tp.submit(self.kline.get_k, code=code) for code in self.code_info]
                wait(all_task, return_when=ALL_COMPLETED)
        except Exception as e:
            print(e, self.code_end)

    # 手动输入股票代码
    def get_input_code(self):
        while 1:
            code = input('请输入股票代码(英文字母为大写)：')
            if len(code) == 8:
                for old_code in self.data['code_list']:
                    if code not in old_code:
                        if len(code) == 8:
                            if 'SZ' in code:
                                self.code_end = '0.' + code[2:]
                                self.code_info[f'{self.code_end}'] = date.today().ctime()
                                self.kline.get_k(code=self.code_end)
                                print(self.code_info)
                                return
                            elif 'SH' in code:
                                self.code_end = '1.' + code[2:]
                                self.code_info[f'{self.code_end}'] = date.today().ctime()
                                self.kline.get_k(code=self.code_end)
                                print(self.code_info)
                                return
                            elif 'BJ' in code:
                                self.code_end = 'BJ' + code  # xueqiu.txt
                                self.code_info[f'{self.code_end}'] = date.today().ctime()
                                print(self.code_info)
                                return
                            else:
                                self.code_info[f'Stock code “{code}” error'] = date.today().ctime()
                                print('code error')
                        print(self.code_info)
                        return
                    else:
                        print(f'{code} is downloaded')
                        return
            elif len(code) == 6:
                for old_code in self.data['code_list']:
                    if code not in old_code[2:]:
                        if code[0] == '0':
                            self.kline.get_k(code=f'0.{code}')
                            self.code_info[f'{self.code_end}'] = date.today().ctime()
                            return
                        elif code[0] == '6':
                            print(code)
                            self.kline.get_k(code=f'1.{code}')
                            self.code_info[f'{self.code_end}'] = date.today().ctime()
                            return
                    else:
                        print(f'{code} is downloaded')
                        return
            elif 8 < len(code) < 6:
                if code.upper() == 'Q':
                    return '初始化页面'
                print('股票代码不正确')


# 初始化系统文件
class System:
    if not os.path.exists('system'):
        os.mkdir('./system')
    if not os.path.exists('system/sys.json'):
        json_data = {
            'VERSION': '1.0.0',
            'SYSTEM': 'win',
            'SYSTEM_DIR': 'system',
            'AUTHOR': '曲涵',
            'PRO_DATE': '2023-7-29'
        }
        with open('./system/sys.json', 'w') as f:
            json.dump(json_data, f)
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('system/sys_code.json'):
        try:
            data = pandas.read_excel('./system/List(1).xlsx', engine='openpyxl')
            sys_code = {}
            code_list = []
            for code in data['代码']:
                code_list.append(code)
            sys_code = {'code_list': code_list}
            with open('./system/sys_code.json', 'w') as f:
                json.dump(sys_code, f)
        except Exception as e:
            print('system error: List(1).xlsx not defined')
    if not os.path.exists('system/catch.json'):
        catch = {}
        with open('./system/catch.json', 'w') as f:
            json.dump(catch, f)

    def update_code(self):
        sys_code = []
        data = pandas.read_excel('./system/List(1).xlsx', engine='openpyxl')
        for code in data['代码']:
            sys_code.append(code)
        with open('./system/sys_code.json', 'r') as f:
            info = json.load(f)
            info['code_list'] = sys_code
            with open('./system/sys_code.json', 'w') as f:
                json.dump(info, f)


# 系统文件维护
class SystemMaintenance:

    def __int__(self):
        pass

    def save_catch(self, data=None):
        with open('./system/catch.json', 'r') as f:
            try:
                old_catch = json.load(f)
                if old_catch['sys_blog']:
                    old_catch['sys_blog'].append({date.today().ctime(): data})
                    with open('./system/catch.json', 'w') as f:
                        json.dump(old_catch, f)
                else:
                    info = []
                    info.append({date.today().ctime(): data})
                    new_catch = {'sys_blog': info}
                    with open('./system/catch.json', 'w') as f:
                        json.dump(new_catch, f)
                        print('1ok')
            except Exception as e:
                info = []
                info.append({date.today().ctime(): data})
                new_catch = {'sys_blog': info}
                with open('./system/catch.json', 'w') as f:
                    json.dump(new_catch, f)
                    print('2ok')

    def show_catch(self):
        with open('./system/catch.json', 'r') as f:
            catch = json.load(f)
            print(json.dumps(catch))
            return json.dumps(catch)


class Abnormal:
    with open('./system/cookie.json', 'r') as f:
        cookie = json.load(f)
        params = cookie['params']
        headers = cookie['ALL_headers']
        cookies = cookie['cookies']

    def __int__(self):
        pass

    def down_excel(self, code=None):
        self.params['secid'] = code
        response = requests.get(
            url='http://push2his.eastmoney.com/api/qt/stock/kline/get',
            cookies=self.cookies,
            headers=self.headers,
            params=self.params,
            verify=False,
        ).text[19:-2]
        # time.sleep(random.randint(160, 200) / 100)
        data = eval(response)
        self.name = data['data']['code']
        date = []
        open = []
        close = []
        hight = []
        low = []
        turnover = []
        amplitude = []
        change_hands = []
        transactions = []
        increase = []
        amount = []
        for info in data['data']['klines']:
            info_list = info.split(',')
            date.append(info_list[0])
            open.append(info_list[1])
            close.append(info_list[2])
            hight.append(info_list[3])
            low.append(info_list[4])
            turnover.append(info_list[5])
            transactions.append(info_list[6])
            amplitude.append(info_list[7])
            increase.append(info_list[8])
            amount.append(info_list[9])
            change_hands.append(info_list[10])
        dataframe = {
            '时间': date,
            '开盘': open,
            '最高': hight,
            '最低': low,
            '收盘': close,
            '涨幅': increase,
            '振幅': amplitude,
            '总手': turnover,
            '金额': transactions,
            '换手率%': change_hands,
            '涨跌额': amount
        }
        dataframe = pandas.DataFrame(dataframe)
        dataframe.to_excel(f'./excel/{code[2:]}.xlsx', index=False)


# 数据更新
class Update:
    params = {
        'fields1': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13',
        'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
        'beg': '0',
        'end': '20500101',
        'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
        'rtntype': '6',
        'secid': '1.688073',
        'klt': '101',
        'fqt': '1',
        'cb': 'jsonp1690523531511',
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'http://quote.eastmoney.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
    }
    cookies = {
        'qgqp_b_id': 'ae8270857f3c86d017c6ce291041f113',
        'st_si': '14054124059535',
        'st_asi': 'delete',
        'HAList': 'ty-1-688318-%u8D22%u5BCC%u8D8B%u52BF%2Cty-1-688646-N%u9038%u98DE%2Cty-107-DBO-%u539F%u6CB9ETF-PowerShares%2Cty-0-301519-N%u821C%u79B9%2Cty-0-002310-%u4E1C%u65B9%u56ED%u6797%2Cty-0-300059-%u4E1C%u65B9%u8D22%u5BCC%2Cty-1-688651-N%u76DB%u90A6',
        'st_pvi': '87135487880220',
        'st_sp': '2023-07-01%2015%3A39%3A30',
        'st_inirUrl': 'https%3A%2F%2Fwww.eastmoney.com%2F',
        'st_sn': '6',
        'st_psi': '20230728150452814-113200313000-9806440735',
    }

    def get_data(self, code=None):
        self.params['secid'] = code
        response = requests.get(
            'http://push2his.eastmoney.com/api/qt/stock/kline/get',
            cookies=self.cookies,
            headers=self.headers,
            params=self.params,
            verify=False
        ).text
        time.sleep(random.randint(50, 100) / 100)
        date = []
        open = []
        close = []
        hight = []
        low = []
        turnover = []
        amplitude = []
        change_hands = []
        transactions = []
        increase = []
        amount = []
        data = eval(re.findall(r'jsonp\d+(.*)', response)[0][1:-2])['data']['klines'][-1].split(',')
        date.append(data[0])
        open.append(data[1])
        close.append(data[2])
        hight.append(data[3])
        low.append(data[4])
        turnover.append(data[5])
        transactions.append(data[6])
        amplitude.append(data[7])
        increase.append(data[8])
        amount.append(data[9])
        change_hands.append(data[10])
        dataframe = {
            '时间': date,
            '开盘': open,
            '最高': hight,
            '最低': low,
            '收盘': close,
            '涨幅': increase,
            '振幅': amplitude,
            '总手': turnover,
            '金额': transactions,
            '换手率%': change_hands,
            '涨跌额': amount
        }
        frame = pandas.DataFrame(dataframe)
        frame.to_csv(f'./data/{code[2:]}.csv', mode='a', index=False, header=False)
        print(f'{code[2:]}>>>>>>>>>>>>>>>>>>>>更新中')

    def get_code(self):
        filename = os.listdir('./data')
        start = time.time()
        with ThreadPoolExecutor(max_workers=20) as tp:
            try:
                codes = []
                for name in filename:
                    if name[0] == '0':
                        codes.append(f'0.{name[:-4]}')
                    elif name[0] == '6':
                        codes.append(f'1.{name[:-4]}')
                all_task = [tp.submit(self.get_data, code=code) for code in codes]
                wait(all_task, return_when=ALL_COMPLETED)
            except Exception as e:
                print(e)
        end = time.time()
        print(f'耗时{int(end - start)}秒>>>>>>>>>>{time.ctime()}')

    def get_input(self):
        code = input('输入股票代码：>>>')
        if len(code) == 6:
            if code[0] == '0':
                self.get_data(code=f'0.{code}')
            elif code[0] == '6':
                self.get_data(code=f'1.{code}')
            else:
                print('input error')
        elif len(code) == 8:
            if 'SZ' in code:
                self.get_data(code=f'0.{code[2:]}')
            elif 'SH' in code:
                self.get_data(code=f'1.{code[2:]}')
            # elif 'BJ' in code:
            #     self.code_end = 'BJ' + code  # xueqiu.txt
            else:
                print('input error')


# 系统主界面
class LoginSystem:
    System()
    catch = SystemMaintenance()
    interface = """
        =============================================
        |       股票数据下载     v 1.0.0              |
        =============================================
        |请按照菜单提示选择：                           |
        ---------------------------------------------
        |            1.    股票信息                   |
        |            2.    数据下载                   |
        |            3.    删除数据                   |
        |            4.    更新数据                   |
        |            5.    返回主页面                 |
        |            6.    系统文件更新
        |            H.    帮    助                  |
        |            Q.    退    出                  | 
        ---------------------------------------------
    """
    print(interface)
    while 1:
        number = str(input('选项（5:返回主页面|H帮助页面|Q退出）>>>：'))
        if number == '1':
            menum_1 = """
            |================股票信息==================|
            |       A.      全部信息                   |
            |       B.      指定信息                   |
            |       5.      返回主页面                 |
            |===================END==================|
            """
            print(menum_1)
            while 1:
                num_1 = input('选项(5.返回上一页|H帮助)>>>')
                filename = os.listdir('./data')
                if num_1.upper() == 'A':
                    num = len(filename)
                    for name in filename:
                        print(f'{name}')
                    data = {'open data': num}
                    catch.save_catch(data=data)
                elif num_1.upper() == 'B':
                    num_1_b = """
                    =============输入股票代码（包含字母大写）============
                    """
                    num_1_b_code = input('股票代码>>>')
                    if len(num_1_b_code) == 8:
                        for name in filename:
                            result = re.search(num_1_b_code[2:], name)
                            if result:
                                try:
                                    data = pandas.read_csv(f'./data/{name}')
                                    info = {'search': name}
                                    catch.save_catch(data=info)
                                    print(data)
                                except Exception as e:
                                    data = pandas.read_excel(f'./excel/{name[:-4]}.xlsx')
                                    info = {'search': name}
                                    print(data)
                                    catch.save_catch(data=info)
                    elif len(num_1_b_code) == 6:
                        for name in filename:
                            result = re.search(num_1_b_code, name)
                            if result:
                                try:
                                    data = pandas.read_csv(f'./data/{name}')
                                    info = {'search': name}
                                    catch.save_catch(data=info)
                                    print(data)
                                    catch.save_catch(data=info)
                                except Exception as e:
                                    data = pandas.read_excel(f'./excel/{name[:-4]}.xlsx')
                                    info = {'search': name}
                                    print(data)
                                    catch.save_catch(data=info)
                    elif num_1_b_code == '5':
                        break
                    elif num_1_b_code.upper() == 'H':
                        print('====================帮    助==================')
                        break
                    else:
                        print('股票代码输入有误')
                        break
                elif num_1 == '5':
                    break
                else:
                    print('input error')
        elif number == '2':
            menum_download = """
                            |=============数据下载================|
                            |    A.下载全部数据                    |
                            |    B.指定数据下载                    |
                            |    C.保存EXCEL                      |
                            |    5.返回主页面                      |
                            |===============END==================|  
                                                """
            print(menum_download)
            while 1:
                filename = os.listdir('./data')
                num_2 = str(input('选项(5.返回上一页|H帮助)>>>'))
                if num_2.upper() == 'A':
                    i = 0
                    start = time.time()
                    while 1:
                        i += 1
                        Stock_code().get_sys_code()
                        if i == 20:
                            print('已下载完成')
                            info = {'down': '下载全部数据成功', 'time': time.ctime()}
                            catch.save_catch(data=info)
                            break
                    end = time.time()
                    print(f'耗时{int(end - start)}秒')
                    break
                elif num_2.upper() == 'B':
                    Stock_code().get_input_code()
                    print('指定数据下载')
                    break
                elif num_2.upper() == 'C':
                    start = time.time()
                    for name in os.listdir('./data'):
                        try:
                            data = pandas.read_csv(f'./data/{name}', encoding='c')
                            data.to_excel(f'./excel/{name[:-4]}.xlsx', engine='openpyxl', index=False)
                            print(f'{name[:-4]}保存excel完成')
                        except Exception as e:
                            if name[0] == '0':
                                r_code = f'0.{name[:-4]}'
                                Abnormal().down_excel(r_code)
                            elif name[0] == '6':
                                r_code = f'1.{name[:-4]}'
                                Abnormal().down_excel(r_code)
                            print(f'{name[:-4]}保存excel完成')
                            # continue
                    end = time.time()
                    info = {'down_excel': '导出excel成功', 'time': time.ctime()}
                    catch.save_catch(data=info)
                    print(f'耗时{int(start - end)}')
                    break
                elif num_2 == '5':
                    print(interface)
                    break
                else:
                    print('input error')
                    break
        elif number == '3':
            menum_del = """
            =============删除数据=================
            |    A   所有数据                    |
            |    B   指定数据                    |
            |    5   返回主页面                   |
            |================END================|
            """
            print(menum_del)
            while 1:
                num_3 = str(input('选项(5.返回上一页|H帮助)>>>'))
                if num_3.upper() == 'A':
                    names = os.listdir('./data')
                    for name in names:
                        del_path = os.path.join('./data/', name)
                        os.remove(del_path)
                        info = {'del': '全部删除成功', 'time': time.ctime()}
                        catch.save_catch(data=info)
                        print(f'{name}删除成功')
                    print(f'>>>>>>>>>>>>>文件全部删除成功<<<<<<<<<<<<')
                elif num_3.upper() == 'B':
                    code = str(input('输入股票代码:>>>'))
                    if len(code) == 6:
                        try:
                            del_path = os.path.join('./data/', f'{code}.csv')
                            os.remove(del_path)
                            info = {'del': f'{code}.csv删除成功'}
                            print(f'{code}.csv删除成功')
                        except Exception as e:
                            print(f'未找到{code}.csv文件')
                    elif len(code) == 8:
                        try:
                            del_path = os.path.join('./data/', f'{code[2:]}.csv')
                            os.remove(del_path)
                            info = {'del': f'{code[2:].csv}删除成功'}
                            catch.save_catch(data=info)
                            print(f'{code[2:]}.csv删除成功')
                        except Exception as e:
                            print(f'未找到{code[2:]}.csv文件')
                elif num_3 == '5':
                    print('返回主页面')
                    break
                else:
                    print('input error')
        elif number == '4':
            menum_4 = """
            |==================数据更新================|
            |           A.  全部数据                   |
            |           B.  指定数据                   |
            |           5.  返回主页面                 |
            |===================END==================|
            """
            print(menum_4)
            while 1:
                num_4 = input('选项(5.返回上一页|H帮助)>>>')
                if num_4.upper() == 'A':
                    update_name = os.listdir('./data')
                    data = pandas.read_csv(f'./data/{update_name[-1]}')
                    if list(data['时间'])[-1] != time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())[:10]:
                        Update().get_code()
                        info = {'upload': '全部更新成功'}
                        catch.save_catch(info)
                    print('今日数据已更新完成')
                    break
                elif num_4.upper() == 'B':
                    update_name = os.listdir('./data')
                    data = pandas.read_csv(f'./data/{update_name[-1]}')
                    if list(data['时间'])[-1] != time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:10]:
                        Update().get_input()
                    print('今日数据已更新完成')
                    break
                elif num_4 == '5':
                    print('返回主页面')
                    break
                else:
                    print('input error')
        elif number == '5':
            print(interface)
        elif number == '6':
            System().update_code()
            print('系统更新完成')
            print(interface)
        elif number.upper() == 'H':
            help = """
            ====================帮助=====================
            运行环境：window。
            最低配置：CPU：4核，内存：4g，硬盘：2g，网络：50M。
            股票代码更新：按照List(1).xlsx内格式复制相关信息，系
            统内按“6”将尽心自动更新股票代码（请勿更改文件名）。
            注意事项：请勿删除system内一“.json”结尾的文件。
            """
            print(help)
        elif number.upper() == 'Q':
            print("""
            ==================结束本次操作=================
            """)
            break
        else:
            print('input error')


if __name__ == '__main__':
    LoginSystem()
