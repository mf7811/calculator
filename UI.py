# Lastest modify: 2022/05/10
# Version: 1.1
# Created by YiFang

import calculator
from tkinter import *
from functools import partial

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
window.geometry("502x600+250+200")

label = Label(window, text = "", width = labelWidth, height= labelHeight, bg='#bdbdbd',font = ('Arial', 18))
button_1 = Button(window, text = "1", command = partial(add_str,"1"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_2 = Button(window, text = "2", command = partial(add_str,"2"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_3 = Button(window, text = "3", command = partial(add_str,"3"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_4 = Button(window, text = "4", command = partial(add_str,"4"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_5 = Button(window, text = "5", command = partial(add_str,"5"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_6 = Button(window, text = "6", command = partial(add_str,"6"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_7 = Button(window, text = "7", command = partial(add_str,"7"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_8 = Button(window, text = "8", command = partial(add_str,"8"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_9 = Button(window, text = "9", command = partial(add_str,"9"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_0 = Button(window, text = "0", command = partial(add_str,"0"), width = 24, height= buttonHeight, font = ('Arial', 15))
button_dot = Button(window, text = ".", command = partial(add_str,"."), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_plus = Button(window, text = "+", command = partial(add_str,"+"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_minus = Button(window, text = "-", command = partial(add_str,"-"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_multiply = Button(window, text = "x", command = partial(add_str,"*"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_divide = Button(window, text = "/", command = partial(add_str,"/"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_leftperen = Button(window, text = "(", command = partial(add_str,"("), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_rightperen = Button(window, text = ")", command = partial(add_str,")"), width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_equal = Button(window, text = "=", command = button_equal_event, width = buttonWidth, height= buttonHeight, font = ('Arial', 15))
button_clean = Button(window, text = "C", command = clean_event, width = buttonWidth, height= buttonHeight, font = ('Arial', 15))

label.place(x=0,y=0)
button_1.place(x=0,y=210)
button_2.place(x=125,y=210)
button_3.place(x=250,y=210)
button_4.place(x=0,y=300)
button_5.place(x=125,y=300)
button_6.place(x=250,y=300)
button_7.place(x=0,y=390)
button_8.place(x=125,y=390)
button_9.place(x=250,y=390)
button_0.place(x=0,y=480)
button_dot.place(x=250,y=480)
button_divide.place(x=375,y=120)
button_multiply.place(x=375,y=210)
button_minus.place(x=375,y=300)
button_plus.place(x=375,y=390)
button_equal.place(x=375,y=480)
button_leftperen.place(x=125,y=120)
button_rightperen.place(x=250,y=120)
button_clean.place(x=0,y=120)


window.mainloop()

