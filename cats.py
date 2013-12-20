#-*- coding:gbk -*-

from Tkinter import *

global login_flag
login_flag = False

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
    
    # ��� Text2 ��������
    Text2.delete(0.0, END)
        
    if cats_data.get(name):
        # ����������è����Ӧ������ ����ʾ�� Text2 ��
        columns = cats_data[name]
        display = u"è����" +  columns[0]
        display += u"\nӢ������" +  columns[1]
        display += u"\n���ͣ�" +  columns[2]
        display += u"\n���أ�" +  columns[3]
        display += u"\në����" +  columns[4]
        display += u"\n���ܣ�" +  columns[5]
        Text2.insert(0.0, display)
        
    else:
        # ���û����Ӧ��¼ ����ʾ�޼�¼
        Text2.insert(0.0, u"δ�鵽������")



def Command_login_Cmd(event=None):
    """ ���µ�¼��ť�����¼�
    """
    global login_flag
    username = Text_username.get()
    password = Text_password.get()
    # ��֤����
    if username.lower() == "abcde" and password == "12345":
        # �˳���¼�� ����������
        login_flag = True
        login.quit()
        login.destroy()
        


# ���Ƶ�¼����
login = Tk()
login.title('Login')
login.geometry('300x160')

# ���ֱ�ǩ
Label_l1 = Label(login, text=u'�û�����')
Label_l1.place(x=30, y=30, width=80, height=17)
Label_l1 = Label(login, text=u'���룺')
Label_l1.place(x=30, y=70, width=80, height=17)

# �ı���
Text_username = Entry(login)
Text_username.place(x=120, y=30, width=130, height=18)
Text_password = Entry(login, show="*")
Text_password.place(x=120, y=70, width=130, height=18)

# ��¼��ť
Command_login = Button(login, text=u'��¼', command=Command_login_Cmd)
Command_login.place(x=100, y=110, width=89, height=33)


login.mainloop()


# ������������沼��
top = Tk()
top.title('Cats')
top.geometry('400x300')

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
Text2 = Text(top)
Text2.place(x=32, y=56, width=320, height=220)


# ����ѵ�¼����ʾ������
if login_flag:
    top.mainloop()



