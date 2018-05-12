from tkinter import *
from resource.get_query_url import *
import time
import threading


class spider:

    boolean_monitor = False
    integer_monitor = 0
    conn = 0

    def __init__(self):

        self.root = Tk()
        self.root.title("车票监控")

        self.root.geometry('1200x360')
        # Top
        self.frm = Frame(self.root)
        Label(self.root, text="车票监控", font=('Arial', 15)).pack()

        # Left
        self.frm_L = Frame(self.frm)
        self.frm_LT = Frame(self.frm_L)
        self.start = StringVar()
        e1 = Entry(self.frm_LT, textvariable=self.start, width=5, font=('Verdana', 15))
        e1.insert(10, '武汉')
        e1.pack(side=RIGHT)
        Label(self.frm_LT, text='始发站', font=('Arial', 12)).pack(side=LEFT)
        self.frm_LT.pack(pady=10)

        self.frm_LT2 = Frame(self.frm_L)
        self.destination = StringVar()
        e2 = Entry(self.frm_LT2, textvariable=self.destination, width=5, font=('Verdana', 15))
        e2.insert(10, '北京')
        e2.pack(side=RIGHT)
        Label(self.frm_LT2, text='终点站', font=('Arial', 12)).pack(side=LEFT)
        self.frm_LT2.pack(pady=10)

        self.frm_LT3 = Frame(self.frm_L)
        self.year = StringVar()
        e3 = Entry(self.frm_LT3, textvariable=self.year, width=4, font=('Verdana', 8))
        e3.insert(10, '2018')
        e3.pack(side=LEFT)
        Label(self.frm_LT3, text='年', font=('Arial', 12)).pack(side=LEFT)
        self.month = StringVar()
        e4 = Entry(self.frm_LT3, textvariable=self.month, width=3, font=('Verdana', 8))
        e4.insert(10, '05')
        e4.pack(side=LEFT)
        Label(self.frm_LT3, text='月', font=('Arial', 12)).pack(side=LEFT)
        self.day = StringVar()
        e4 = Entry(self.frm_LT3, textvariable=self.day, width=3, font=('Verdana', 8))
        e4.insert(10, '23')
        e4.pack(side=LEFT)
        Label(self.frm_LT3, text='日', font=('Arial', 12)).pack(side=LEFT)
        self.frm_LT3.pack(pady=10)

        self.frm_LT4 = Frame(self.frm_L)
        self.btString = StringVar()
        self.btString.set('开始监控')
        Button(self.frm_LT4, textvariable=self.btString, command=self.monitor, width=8, height=1,
               font=('宋体', 20)).pack(side=LEFT)
        self.frm_LT4.pack(pady=20)

        self.frm_L.pack(side=LEFT)

        self.frm_R = Frame(self.frm)
        self.frm_RT1 = Frame(self.frm_R)
        self.t_show = Text(self.frm_RT1, width=100, height=15, font=('Verdana', 12))
        self.t_show.insert('1.0', '')
        self.t_show.pack()
        self.frm_RT1.pack()

        self.frm_RT2 = Frame(self.frm_R)
        self.times = StringVar()
        self.times.set('已监控0次')
        self.l_times = Label(self.frm_RT2, textvariable=self.times, font=('Arial', 12)).pack()
        self.frm_RT2.pack()

        self.frm_R.pack(side=RIGHT)

        self.frm.pack()

        self.thread_crawl = threading.Thread(target=self.loop_crawl, name='LoopThread')
        self.thread_crawl.start()

    def loop_crawl(self):
        while True:
            if self.boolean_monitor:
                comd = 'cs ' + self.year.get() + '-' + self.month.get() + '-' + self.day.get() + " " + self.start.get() + " " \
                       + self.destination.get()
                url = get_query_url(comd)
                results = query_train_info(url, self.conn)

                self.integer_monitor = self.integer_monitor + 1
                self.times.set('已监控' + str(self.integer_monitor) + '次')

                self.t_show.delete(1.0, END)
                self.t_show
                for result in results:
                    self.t_show.insert(1.0, result + '\n')
            else:
                pass
            time.sleep(60)

    def monitor(self):
        self.boolean_monitor = not self.boolean_monitor
        if self.boolean_monitor:
            self.conn = mysql.connector.connect(user='root', password='', database='tickets', use_unicode=True)
            self.btString.set('停止监控')
        else:
            self.conn.close()
            self.btString.set('开始监控')


def main():
    s = spider()
    mainloop()


if __name__ == '__main__':
    main()

#
# def hehe():
#     print('123')
#
#
# def resize(ev=None):
#     print(scale.get())
#
#
# root = Tk()
#
# # li     = ['C','python','php','html','SQL','java']
# # movie  = ['CSS','jQuery','Bootstrap']
# # listb  = Listbox(root)          #  创建两个列表组件
# # listb2 = Listbox(root)
# # for item in li:                 # 第一个小部件插入数据
# #     listb.insert(END,item)
# #
# # for item in movie:              # 第二个小部件插入数据
# #     listb2.insert(0,item)
# #
# # listb.pack()                    # 将小部件放置到主窗口中
# # listb2.pack()
#
# label = Label(root,text = 'hahaha')
# label.pack()
# button = Button(root,text='hehe',command=hehe)
# # button.pack()
# button.pack(fill=X)
# scale = Scale(root, from_=10, to=40, orient=HORIZONTAL, command=resize)
# scale.set(12)
# scale.pack(fill=X, expand=1)
#
# root.mainloop()                 # 进入消息循环
#
