#-*- coding:gbk -*-

from Tkinter import *


def read_data(filename):
    """ ��ȡ���ݿⷽ��
        filename - �����ļ���
    """
    data = {}
    # ��ȡȫ������
    read_str = open(filename).read().decode("gbk")
    for row in read_str.split("\n")[1:]:
        # ���д���
        columns = row.split(",")
        data[columns[0]] = columns
    return data

# ��ȡ���ݵ� cats_data ����
cats_data = read_data("data.csv") 


def Command1_Cmd(event=None):
    """ ���²�ѯ��ť�����¼�
    """
    # ��ȡ�ı�������
    name = Text1.get()
    if cats_data.get(name):
        # ����������è����Ӧ������ ����ʾ�� Label2 ���ֱ�ǩ��
        columns = cats_data[name]
        display = u"è����" +  columns[0]
        display += u"\nӢ������" +  columns[1]
        display += u"\n���ͣ�" +  columns[2]
        display += u"\n���أ�" +  columns[3]
        display += u"\në����" +  columns[4]
        Label2["text"] = display
    else:
        # ���û����Ӧ��¼ ����ʾ�޼�¼
        Label2["text"] = u"δ�鵽������"


# ����ͼ�ν��沼��
top = Tk()
top.title('Cats')
top.geometry('400x200')

# ��ʾ����
Label1 = Label(top, text=u'������è����')
Label1.place(x=32, y=16, width=73, height=17)

# �����ı���
Text1 = Entry(top)
Text1.place(x=120, y=16, width=130, height=18)

# ��ѯ��ť
Command1 = Button(top, text=u'��ѯ', command=Command1_Cmd)
Command1.place(x=270, y=8, width=89, height=33)

# �����������
Label2 = Label(top)
Label2.place(x=32, y=56, width=300, height=120)

top.mainloop()




