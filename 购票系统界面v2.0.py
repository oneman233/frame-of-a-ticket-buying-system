#购票系统v2.0
#缺陷在于文件读取实际上没有任何作用，没有从文件中获取价格和地名变量
#优势在于从用户输入框中获取信息时添加了try-except的异常处理

from tkinter import *
import tkinter.messagebox

first = Tk() #初始化首界面
sw = first.winfo_screenwidth()
#得到屏幕宽度
sh = first.winfo_screenheight()
#得到屏幕高度
ww = 400
wh = 400
#窗口宽高为400
x = (sw-ww) / 2
y = (sh-wh) / 2
first.geometry("%dx%d+%d+%d" %(ww,wh,x,y)) #设置窗口大小并且保持窗口居中
first.title("购票系统v2.0") #设置窗口名称

sum_piao = 0
sum_piao = int(sum_piao) #储存当前已购买的票数

def buy_ticket(): #弹出购买框函数
    global second #设定购买框为全局变量，便于后面关闭second
    second = Tk() #初始化购票界面
    second.geometry("300x300")
    second.title("购买界面")
    anjian1 = Button(second,text = "购买票一",command = buy_confirm)
    anjian1.pack()
    anjian2 = Button(second,text = "购买票二",command = buy_confirm)
    anjian2.pack()
    anjian3 = Button(second,text = "购买票三",command = buy_confirm)
    anjian3.pack()
    anjian4 = Button(second,text = "多张购买",command = buy_multi)
    anjian4.pack()
    #注意，由于second最后将被关闭，所以不需要加上消息循环

def buy_multi(): #多张购买函数
    second.destroy()
    global third
    third = Tk()
    third.geometry("400x150")
    third.title("多张购买")
    global zhangshu #把这条label设置为全局变量，便于在下面输出错误提示信息
    zhangshu = Label(third,text = "购买张数：")
    zhangshu.pack(side = LEFT) #把购买张数的提示文字插入到左侧
    global shuru
    shuru = Entry(third,bd = 7) #第二个参数是设定背景框宽度
    shuru.pack(side = RIGHT) #把输入框插入到右侧
    anniu_quxiao = Button(third,text = "取消",command = third.destroy,font = 15).pack(side = BOTTOM)
    anniu_queren = Button(third,text = "确认",command = get_num,font = 15).pack(side = BOTTOM)
    #font参数调整了按钮的字号大小
    #确认键会尽可能的靠近底部，但是必须在取消键之上，因为pack的插入有严格的先后顺序

def get_num(): #获取用户输入值函数
    try: #尝试获取用户输入值，有可能遇到问题
        tianjia=eval(shuru.get())
    except:
        zhangshu.config(text = "输入有误，请重新输入")
        return #返回一个空值，某种意义上相当于结束了函数
    third.destroy()
    global sum_piao
    sum_piao+=tianjia
    tishi.config(text = "购票成功，当前已购买"+str(sum_piao)+"张票")

def buy_confirm():
    second.destroy()
    ans = tkinter.messagebox.askokcancel("确认","是否确认购买该车票") #弹出一个是否确认的窗口，返回一个布尔值
    if ans:
        global sum_piao #设定票的总数为全局变量
        sum_piao+=1
        tishi.config(text = "购票成功，当前已购买"+str(sum_piao)+"张票")
    else:
        tishi.config(text = "购票被取消")
    
f = open('ticket.txt','r') #打开文件
ticket = f.readlines() #不断读取一行，直到文件末尾

list_ticket = Listbox(first) #新创建一个列表用于存储各种票的信息
for item in ticket:
    list_ticket.insert(0,item)
list_ticket.pack() #把票的信息的列表插入当前窗口

biaoti = Label(first,text = "欢迎进入购票系统v2.0",fg = "red",relief = SUNKEN) #fg代表颜色，relief代表边框样式
biaoti.pack() #把标题插入first窗口
goumai = Button(first,text = "购买",command = buy_ticket)
goumai.pack()
tishi = Label(first,text = "当前未进行任何操作") #用于输出提示信息
tishi.pack()
pic = Canvas(first,bg = "black",cursor = "plus") #添加一个画布，鼠标移动到画布上时将会变成加号
pic.pack()

first.mainloop() #首页进入消息循环
