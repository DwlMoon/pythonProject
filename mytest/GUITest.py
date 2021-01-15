from tkinter import *
import tkinter.messagebox as messagebox
from mytest import CreateLiving


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        account_name = Label(self, text="账号 :")
        account_name.pack()
        self.account = Entry(self, bd=5, width=30)
        self.account.pack()
        pass_name = Label(self, text="密码 :")
        pass_name.pack()
        self.password = Entry(self, bd=5, width=30)
        self.password.pack()
        excel_line = Label(self, text="Excel列数 :")
        excel_line.pack()
        self.excel = Entry(self, bd=5, width=30)
        self.excel.pack()
        self.alertButton = Button(self, text='注册', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        acount = self.account.get() or 'world'
        password = self.password.get() or 'world'
        excel = self.excel.get() or 'world'
        print("获取的账号为:%s"% acount)
        print("获取的密码为:%s"% password)
        result=CreateLiving.createliving.createLivingRoom(None,acount,password,excel)
        if "success" is result:
            messagebox.showinfo('Message', '您输入的账号： %s 注册直播间成功 !' % acount)
        elif "fail" is result:
            messagebox.showinfo('Message', '您输入的账号： %s 注册直播间失败 !' % acount)



app = Application()
# 设置窗口标题:
app.master.title('注册速卖通直播间')
app.master.geometry('400x200')

# 主消息循环:
app.mainloop()


if __name__ == '__main__':
   Application.hello(None)

