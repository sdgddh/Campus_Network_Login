from tkinter import *
import tkinter as tk
import tkinter.messagebox
import requests

#设置窗口居中
def window_info():
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    return x,y
  
#设置登陆窗口属性
window = tk.Tk()
window.title('湖南涉外经济学院')
a,b=window_info()
window.geometry("450x300+%d+%d"%(a,b))

#登陆界面的信息
tk.Label(window,text="校园网登录系统",font=("宋体",32)).place(x=80,y=50)
tk.Label(window,text="账号：").place(x=120,y=150)
tk.Label(window,text="密码：").place(x=120,y=190)
#显示输入框
var_usr_name = tk.StringVar()
#显示默认账号
var_usr_name.set('1740301')
entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=190,y=150)
var_usr_pwd = tk.StringVar()
#设置输入密码后显示*号
entry_usr_pwd = tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=190,y=190)

def usr_login():
 #获取输入的账号密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    url='http://172.16.18.6/a70.htm'
    
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
        'DDDDD': usr_name,
        'upass': usr_pwd,
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


#登陆按钮
btn_login = tk.Button(window,text="登陆",command=usr_login,width=7,height=2)
btn_login.place(x=220,y=230)

window.mainloop()
