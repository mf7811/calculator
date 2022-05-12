# Lastest modify: 2022/05/12
# Version: 1.2
# Created by YiFang

import calculator
from tkinter import *
from functools import partial
import re

funcStr = ""
buttonWidth = 10
buttonHeight = 5
labelWidth = 45
labelHeight = 6

def add_str(tmpStr):
	global funcStr
	funcStr = funcStr + tmpStr
	print(funcStr)
	label['text'] = funcStr

def button_equal_event():
	global funcStr
	inputStr = funcStr
	inputRegex = re.compile(r'[^\d\+\-\*\/\(\).]')
	if inputRegex.search(inputStr) or (not inputStr[-1].isdigit() and inputStr[-1] != ")"):
		errorMSG = "Input string is abnormal, please check."
		print(errorMSG)
		label['text'] = errorMSG
		funcStr = ""
	else:
		if "(" in inputStr:
			strAfterHandle = calculator.handleParentheses(inputStr)
			outStr = calculator.calculate(strAfterHandle)
		else:
			outStr = calculator.calculate(inputStr)
		print("Final Ouput: ",outStr)
		label['text'] = "=  "+ outStr
		funcStr = outStr

def clean_event():
	global funcStr
	funcStr = ""
	label['text'] = ""

window = Tk()
window.title("Calculator")
window.geometry("505x600+250+200")

currentWidth = window.winfo_width()
currentHeight = window.winfo_height()
topFrame = Frame(window,width=currentWidth,height=150,bg='gray')
topFrame.pack(side=TOP,fill=X)
numberFrame = Frame(window,width=currentWidth,height=currentHeight-150,bg='gray')
numberFrame.pack()

buttonMap = [["C","7","4","1","00"],["(","8","5","2","0"],[")","9","6","3","."],["/","*","-","+","="]]

pixel = PhotoImage(width=1,height=1)
label = Label(topFrame, text = "", width = labelWidth, height= labelHeight,font = ('Arial', 18),bg='gray')
label.pack()

for x in range(0,len(buttonMap)):
	for y in range(0,len(buttonMap[0])):
		if buttonMap[x][y]=="C":
			tmpButton = Button(numberFrame,text = buttonMap[x][y], command = clean_event, width=buttonWidth,height=buttonHeight)
		elif buttonMap[x][y]=="=":
			tmpButton = Button(numberFrame,text = buttonMap[x][y], command = button_equal_event,width=buttonWidth,height=buttonHeight)
		else:
			tmpButton = Button(numberFrame,text = buttonMap[x][y], command = partial(add_str,buttonMap[x][y]),width=buttonWidth,height=buttonHeight)
		tmpButton.grid(column=x,row=y)


window.mainloop()

