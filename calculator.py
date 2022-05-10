# Lastest modify: 2022/05/10
# Version: 1.1
# Created by YiFang

import re

def multiplyDivide(opArr,numArr):
	for i in range(0,len(numArr)):
		if opArr[i] == "*-":
			opArr[i] = "*"
			numArr[i] = "-" + numArr[i]
		if opArr[i] == "/-":
			opArr[i] = "/"
			numArr[i] = "-" + numArr[i]

		if opArr[i] == "*":
			tempValue = float(numArr[i-1]) * float(numArr[i])
			numArr[i-1] = str(tempValue)
		elif opArr[i] == "/":
			tempValue = float(numArr[i-1]) / float(numArr[i])
			numArr[i-1] = str(tempValue)
		else:
			continue
		numArr[i] = ""
		opArr[i] = ""
		outStr = ""
		for j in range(0,len(numArr)):
			outStr = outStr + opArr[j] + numArr[j]
		return outStr

	print("The formula contains unsupported operator.\n")

def plusMinus(opArr,numArr):
	tempValue = float(numArr[0])
	for i in range(1,len(numArr)):
		if opArr[i] == "--":
			opArr[i] = "+"
		elif opArr[i] == "+-":
			opArr[i] = "-"

		if opArr[i] == "+":
			tempValue = tempValue + float(numArr[i])
		elif opArr[i] == "-":
			tempValue = tempValue - float(numArr[i])
	return str(tempValue)


def calculate(inputStr):
	if inputStr[0] == "-":
		inputStr = "0" + inputStr
	opArr = re.split("[\d.]+",inputStr)
	numArr = re.split("[\+\-\*\/]+",inputStr)
	if "*" in inputStr or "/" in inputStr:
		outStr = multiplyDivide(opArr,numArr)
		if outStr[0] == "0" and outStr[1] != ".":
			outStr = outStr[1:]
		try:
			if outStr[-2:] == ".0":
				outStr = outStr[:-2]
			outValue = float(outStr)
			return outStr
		except: #not number, need calculate
			return calculate(outStr)
	elif "+" in inputStr or "-" in inputStr:
		outStr = plusMinus(opArr,numArr)
		if outStr[-2:] == ".0":
			outStr = outStr[:-2]
		return outStr

def handleParentheses(inputStr):
	print("inputStr",inputStr)
	subStrPattern = re.compile(r'\([\d\+\-\*\/.]*\)')
	subStrMatch = subStrPattern.search(inputStr)
	subStr = inputStr[subStrMatch.span()[0]+1:subStrMatch.span()[1]-1]
	outStr = calculate(subStr)
	afterHandle = inputStr.replace("("+subStr+")",outStr)

	if "(" not in afterHandle:
		return afterHandle
	else:
		return handleParentheses(afterHandle)


if __name__ == "__main__":
	while 1:
		print("===================")
		inputStr = input("Enter: \n")

		inputRegex = re.compile(r'[^\d\+\-\*\/\(\).]')
		if inputRegex.search(inputStr) or (not inputStr[-1].isdigit() and inputStr[-1] != ")"):
			print("Input string is abnormal, please check.")
		else:
			if "(" in inputStr:
				strAfterHandle = handleParentheses(inputStr)
				outStr = calculate(strAfterHandle)
			else:
				outStr = calculate(inputStr)
			print("Final Ouput: ",outStr)






