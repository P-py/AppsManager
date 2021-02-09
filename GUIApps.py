from tkinter import *
import subprocess
import os
import pyautogui
import time

GuiAppsRoot = Tk(className=' Apps Manager / Apps Opening Shortcutter')
GuiAppsRoot.geometry('800x500')
Canvas = Canvas(GuiAppsRoot, height=800, width=500, bg='Grey')
Canvas.place(relwidth=1.0, relheight=1.0, rely=0, relx=0)
Title = Label(Canvas, text='APPs OPENING SHORTCUTTER')
Title.pack()


def VSCodeCodingButton():
    VScode = 'C:/Users/pedro/AppData/Local/Programs/Microsoft_VS_Code/Code'
    Edge = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge'
    Terminal = 'C:/WINDOWS/system32/cmd'
    os.startfile(Terminal)
    os.startfile(Edge)
    os.startfile(VScode)
def ChillWithYoutube():
    Edge = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge'
    os.startfile(Edge)
    time.sleep(2)
    pyautogui.typewrite('https://www.youtube.com/')
    pyautogui.press('enter')
def Classes():
    MicroSoftTeams = 'C:/Users/pedro/AppData/Local/Microsoft/Teams/current/Teams'
    Edge = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge'
    os.startfile(Edge)
    os.startfile(MicroSoftTeams)
def GamingWithDiscord():
    Discord = 'C:/Users/pedro/AppData/Local/Discord/app-0.0.309/Discord'
    Steam = 'C:/Program Files (x86)/Steam/steam'
    os.startfile(Discord)
    os.startfile(Steam)

WhiteSpace = Label(Canvas, text='', bg='Grey')
Button1 = Button(Canvas, text='Coding with VSCODE', command=VSCodeCodingButton, padx=25, pady=25)
Button2 = Button(Canvas, text='Youtube', command=ChillWithYoutube, padx=25, pady=25)
Button3 = Button(Canvas, text='Classes', command=Classes, padx=25, pady=25)
Button4 = Button(Canvas, text='Gaming - Discord, steam', command=GamingWithDiscord, padx=25, pady=25)
WhiteSpace.pack()
Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
GuiAppsRoot.mainloop()