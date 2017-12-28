# -*- coding: UTF-8 -*-
import tkFileDialog

def seletFile():
    fileName =  tkFileDialog.askopenfilename(filetypes=[("All files","*.png")])
    return  fileName
def seletDir():
    dir = tkFileDialog.askdirectory()
    return dir