import requests


def usr_login():
    # 获取输入的账号密码
    usr_name = '174030138'
    usr_pwd = '191039'
    url = 'http://172.16.18.6/a70.htm'

    cookies = {
        '__guid': '149234166.3958882504061907500.1568543011125.1177',
        'monitor_count': '99',
    }

    headers = {
        'Origin': 'http://172.16.18.6',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'http://172.16.18.6/a70.htm',
        'Connection': 'keep-alive',
    }

    data = {
        'DDDDD': '174030138',
        'upass': '191039',
        'R1': '0',
        'R2': '',
        'R3': '0',
        'R6': '1',
        'para': '00',
        '0MKKey': '123456',
        'buttonClicked': '',
        'redirect_url': '',
        'err_flag': '',
        'username': '',
        'password': '',
        'user': '',
        'cmd': '',
        'Login': '',
        'v6ip': ''
    }

    response = requests.post(url, headers=headers, cookies=cookies, data=data)
