# -*- coding: UTF-8 -*-
from Tkinter import *
from Func import  *
from EasyIcon import *
from tkMessageBox import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')
oriImagePath = ""
finishDir = ""

root = Tk()
root.title("快速生成全套iOS应用图标")
root.geometry("500x300+200+100")
root.resizable(0,0)


#menu
menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
menu.add_cascade(label='关于',menu=submenu)

#textView
Label(root,text = "请选择图片文件(注意：分辨率为1024*1024)").place(x=10,y=10)
oriLabel = Label(root,text = "图片路径:")
oriLabel.place(x=10,y=40)


# func
def seletImage():
    global oriLabel,oriImagePath
    path = seletFile()
    oriLabel["text"] = "图片路径:"+path
    oriImagePath = path




Button(root,text="选择图片",command=seletImage).place(x=10,y=70)

dirLable = Label(root,text = "生成图标目录:")
dirLable.place(x=10,y=150)

def seletDirHome():
    global finishDir,dirLable
    path = seletDir()
    dirLable["text"] = "生成图标目录:"+path
    finishDir = path

Button(root,text="选择目录",command=seletDirHome).place(x=10,y=180)


def start():
    global oriImagePath,finishDir
    if len(oriImagePath)==0:
        showerror("警告","请选择要生成的图标(务必为1024*1024尺寸的png图片)")
        return
    if len(finishDir)==0:
        showerror("警告","请选择生成图标的目录")
        return
    # try:
    startWork(oriImagePath,finishDir)
    # except Exception,e:
    #     showerror("错误","生成失败")
    #     return
    showinfo("恭喜","图标生成成功")


Button(root,text="开始生成",command=start).place(x=10,y=220)

root.mainloop()
