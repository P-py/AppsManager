from tkinter import *
import subprocess
import os
import pyautogui
import time             #Importing all the necessary libraries/modules

GuiAppsRoot = Tk(className=' Apps Manager / Apps Opening Shortcutter') 
#Creating the "root" window
GuiAppsRoot.geometry('800x500') #Definning the size of the root
Canvas = Canvas(GuiAppsRoot, height=800, width=500, bg='Grey') #creating a canvas
Canvas.place(relwidth=1.0, relheight=1.0, rely=0, relx=0)#placing it
Title = Label(Canvas, text='APPs OPENING SHORTCUTTER')#creating and placing the title
Title.pack()


def VSCodeCodingButton():
    VScode = '(Your coding IDE path)'
    Edge = '(Your personal browser path'
    Terminal = 'C:/WINDOWS/system32/cmd'
    os.startfile(Terminal)
    os.startfile(Edge)
    os.startfile(VScode)
def ChillWithYoutube():
    Edge = '(Your personal browser path)'
    os.startfile(Edge)
    time.sleep(2)
    pyautogui.typewrite('https://www.youtube.com/')
    pyautogui.press('enter')
def Classes():
    MicroSoftTeams = '(Your school app path)'  # Can be also lines of code (using webscraping) to open the browser in the site of the school app or something like that 
    Edge = '(Your personal browser path, mine is edge so...)'
    os.startfile(Edge)
    os.startfile(MicroSoftTeams)
def GamingWithDiscord():
    Discord = '(your Discord path)'
    Steam = '(your Steam path)'
    os.startfile(Discord)
    os.startfile(Steam)
#Defining the function of the buttons that I want to have, if you want to use different buttons you will need to edit the source code
    
WhiteSpace = Label(Canvas, text='', bg='Grey')
Button1 = Button(Canvas, text='Coding', command=VSCodeCodingButton, padx=25, pady=25)
Button2 = Button(Canvas, text='Youtube', command=ChillWithYoutube, padx=25, pady=25)
Button3 = Button(Canvas, text='Classes', command=Classes, padx=25, pady=25)
Button4 = Button(Canvas, text='Gaming - Discord, steam', command=GamingWithDiscord, padx=25, pady=25)
WhiteSpace.pack()
Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
GuiAppsRoot.mainloop()
