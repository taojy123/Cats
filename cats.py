#-*- coding:gbk -*-

from Tkinter import *


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
    if cats_data.get(name):
        # 如果有输入的猫名对应的资料 则显示到 Label2 文字标签中
        columns = cats_data[name]
        display = u"猫名：" +  columns[0]
        display += u"\n英文名：" +  columns[1]
        display += u"\n体型：" +  columns[2]
        display += u"\n体重：" +  columns[3]
        display += u"\n毛长：" +  columns[4]
        Label2["text"] = display
    else:
        # 如果没有相应记录 则提示无记录
        Label2["text"] = u"未查到该数据"


# 创建图形界面布局
top = Tk()
top.title('Cats')
top.geometry('400x200')

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
Label2 = Label(top)
Label2.place(x=32, y=56, width=300, height=120)

top.mainloop()




