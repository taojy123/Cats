#-*- coding:gbk -*-

from Tkinter import *

global login_flag
login_flag = False

def read_data(filename):
    """ 读取数据库方法
        filename - 数据文件名
    """
    data = {}
    # 读取全部数据
    read_str = open(filename).read().decode("gbk")
    for row in read_str.split("\n")[1:]:
        # 分行处理
        columns = row.split(",")
        data[columns[0]] = columns
    return data

# 读取数据到 cats_data 变量
cats_data = read_data("data.csv") 


def Command1_Cmd(event=None):
    """ 按下查询按钮触发事件
    """
    # 获取文本框输入
    name = Text1.get()
    
    # 清空 Text2 现有内容
    Text2.delete(0.0, END)
        
    if cats_data.get(name):
        # 如果有输入的猫名对应的资料 则显示到 Text2 中
        columns = cats_data[name]
        display = u"猫名：" +  columns[0]
        display += u"\n英文名：" +  columns[1]
        display += u"\n体型：" +  columns[2]
        display += u"\n体重：" +  columns[3]
        display += u"\n毛长：" +  columns[4]
        display += u"\n介绍：" +  columns[5]
        Text2.insert(0.0, display)
        
    else:
        # 如果没有相应记录 则提示无记录
        Text2.insert(0.0, u"未查到该数据")



def Command_login_Cmd(event=None):
    """ 按下登录按钮触发事件
    """
    global login_flag
    username = Text_username.get()
    password = Text_password.get()
    # 验证密码
    if username.lower() == "abcde" and password == "12345":
        # 退出登录框 进入主界面
        login_flag = True
        login.quit()
        login.destroy()
        


# 绘制登录窗口
login = Tk()
login.title('Login')
login.geometry('300x160')

# 文字标签
Label_l1 = Label(login, text=u'用户名：')
Label_l1.place(x=30, y=30, width=80, height=17)
Label_l1 = Label(login, text=u'密码：')
Label_l1.place(x=30, y=70, width=80, height=17)

# 文本框
Text_username = Entry(login)
Text_username.place(x=120, y=30, width=130, height=18)
Text_password = Entry(login, show="*")
Text_password.place(x=120, y=70, width=130, height=18)

# 登录按钮
Command_login = Button(login, text=u'登录', command=Command_login_Cmd)
Command_login.place(x=100, y=110, width=89, height=33)


login.mainloop()


# 绘制主界面界面布局
top = Tk()
top.title('Cats')
top.geometry('400x300')

# 提示文字
Label1 = Label(top, text=u'请输入猫名：')
Label1.place(x=32, y=16, width=73, height=17)

# 输入文本框
Text1 = Entry(top)
Text1.place(x=120, y=16, width=130, height=18)

# 查询按钮
Command1 = Button(top, text=u'查询', command=Command1_Cmd)
Command1.place(x=270, y=8, width=89, height=33)

# 输出内容文字
Text2 = Text(top)
Text2.place(x=32, y=56, width=320, height=220)


# 如果已登录则显示主界面
if login_flag:
    top.mainloop()



