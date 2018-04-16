import requests
import json

# 关闭https证书验证警告
requests.packages.urllib3.disable_warnings()

# 城市名代码查询字典
# key：城市名 value：城市代码
from .ParseStation import get_station
from .station import stations

# 反转k，v形成新的字典
code_dict = {v: k for k, v in stations.items()}


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
    print(url)

    return url
