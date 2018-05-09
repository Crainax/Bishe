from tkinter import *


class spider:

    def __init__(self):
        self.root = Tk()
        self.root.title("车票监控")

        self.root.geometry('470x320')
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
        self.frm_LT.pack()

        self.frm_LT2 = Frame(self.frm_L)
        self.destination = StringVar()
        e2 = Entry(self.frm_LT2, textvariable=self.destination, width=5, font=('Verdana', 15))
        e2.insert(10, '北京')
        e2.pack(side=RIGHT)
        Label(self.frm_LT2, text='终点站', font=('Arial', 12)).pack(side=LEFT)
        self.frm_LT2.pack()

        self.frm_L.pack(side=LEFT)

        self.frm.pack()


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
