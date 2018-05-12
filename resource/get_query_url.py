# -*- coding: utf-8 -*-
import requests
import json
import mysql.connector
from resource.station import stations

# 关闭https证书验证警告
requests.packages.urllib3.disable_warnings()

# 城市名代码查询字典
# key：城市名 value：城市代码


# 反转k，v形成新的字典
code_dict = {v: k for k, v in stations.items()}

conn = {}


def get_query_url(text):
    '''
    返回调用api的url链接
    '''
    # 解析参数 aggs[0]里是固定字符串：车票查询 用于匹配公众号接口
    args = str(text).split(' ')
    try:
        date = args[1]
        from_station_name = args[2]
        to_station_name = args[3]
        from_station = stations[from_station_name]
        to_station = stations[to_station_name]
    except:
        date, from_station, to_station = '--', '--', '--'
        # 将城市名转换为城市代码

    # api url 构造
    url = (
        'https://kyfw.12306.cn/otn/leftTicket/query?'
        'leftTicketDTO.train_date={}&'
        'leftTicketDTO.from_station={}&'
        'leftTicketDTO.to_station={}&'
        'purpose_codes=ADULT'
    ).format(date, from_station, to_station)

    return url


def query_train_info(url, conn):
    '''
    查询火车票信息：
    返回 信息查询列表
    '''

    info_list = []
    try:
        r = requests.get(url, verify=False)
        # 获取返回的json数据里的data字段的result结果
        raw_trains = r.json()['data']['result']

        for raw_train in raw_trains:
            # 循环遍历每辆列车的信息
            data_list = raw_train.split('|')

            # 车次号码
            train_no = data_list[3]
            # 出发站
            from_station_code = data_list[6]
            from_station_name = code_dict[from_station_code]
            # 终点站
            to_station_code = data_list[7]
            to_station_name = code_dict[to_station_code]
            # 出发时间
            start_time = data_list[8]
            # 到达时间
            arrive_time = data_list[9]
            # 总耗时
            time_fucked_up = data_list[10]
            # 一等座
            first_class_seat = data_list[31] or '--'
            # 二等座
            second_class_seat = data_list[30]or '--'
            # 软卧
            soft_sleep = data_list[23]or '--'
            # 硬卧
            hard_sleep = data_list[28]or '--'
            # 硬座
            hard_seat = data_list[29]or '--'
            # 无座
            no_seat = data_list[26]or '--'

            cursor = conn.cursor()
            cursor.execute('insert into tickets (time,train_id, start_station, end_station, start_time, end_time, use_time,\
             left_one, left_two, left_soft_sleep, left_hard_sleep, left_hard_sit, left_no_sit) values (Now(),\
             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', [train_no, from_station_name, to_station_name, start_time
            , arrive_time, time_fucked_up, first_class_seat, second_class_seat, soft_sleep, hard_sleep, hard_seat,
                                                     no_seat])
            conn.commit()
            cursor.close()
            # print(train_no)
            # 打印查询结果
            info = ('{}/车程:{}-{}/时间:{}-{},用时:{}/余票:一等座[{}],二等座[{}],软卧[{}],硬卧[{}]硬座[{}],无座[{}]'.format(
                train_no, from_station_name, to_station_name, start_time, arrive_time, time_fucked_up, first_class_seat,
                second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat))

            info_list.append(info)

        return info_list
    except:
        return ' 输出信息有误，请重新输入'


if __name__ == '__main__':
    conn = mysql.connector.connect(user='root', password='', database='tickets', use_unicode=True)
    url = get_query_url('cs 2018-05-23 北京 重庆')
    datas = query_train_info(url, conn)
    for i in datas:
        print(i)
    conn.close()
