from random import randint, choice, uniform
import csv
from time import gmtime, strftime
import sys
from math import ceil

validString = {True: "Correct", False: "Incorrect"}

def writeSumToFile(dataArray):
	with open("answers.csv", "a") as csvfile:
		answerFile = csv.writer(csvfile)
		answerFile.writerow(dataArray);

def validateIntAnswer(a,b,op, answer):
	print "Solve: "
	print "%9d" % a
	print op, "%7d" % b
	print "-"*10
	userAnswer = int(raw_input())

	if userAnswer == answer:
		print "Great work"
	else:
		print "Incorrect. Correct answer is:", answer

	valid = validString[userAnswer == answer]
	return ["%9d" % a,op,"%7d" % b,answer, userAnswer, valid]

def validateIntDivAnswer(a,b, quo, rem):
	print "Solve: "
	print "%9d" % a
	print "/", "%7d" % b
	print "-"*10

	userQuo = int(raw_input("Quotient ?:"))
	userRem = int(raw_input("Remainder ?:"))

	if userQuo == quo and userRem == rem:
		print "Great work"
	else:
		print "Incorrect. Correct answer is: Quotient", quo, "Remainder:", rem

	valid = validString[userQuo == quo and userRem == rem]

	return ["%9d" % a,"/","%7d" % b,"Q: %d R: %d"%(quo,rem),  "Q: %d R: %d"%(userQuo,userRem), valid]

def validateFloatAnswer(a,b,op, answer):
	print "Solve: "
	print "%10.4f" % a
	print op, "%7.4f" % b
	print "-"*15
	userAnswer = float(raw_input())
	if userAnswer == answer:
		print "Great work"
	else:
		print "Incorrect. Correct answer is: %7.4f" % answer

	valid = validString[userAnswer == answer]
	return ["%9.4f" % a,op,"%7.4f" % b,answer, userAnswer, valid]

def validateFloatDivAnswer(a,b, quo, rem):
	print "Solve: "
	print "%10.4f" % a
	print "/", "%7.4f" % b
	print "-"*10

	userQuo = int(raw_input("Quotient ?:"))
	userRem = float(raw_input("Remainder ?:"))

	if userQuo == quo and userRem == rem:
		print "Great work"
	else:
		print "Incorrect. Correct answer is: Quotient: %d Remainder: %7.3f" % (quo, rem)

	valid = validString[userQuo == quo and userRem == rem]

	return ["%9.3f" % a,"/","%7.3f" % b,"Q: %d R: %d"%(quo,rem),  "Q: %d R: %d"%(userQuo,userRem), valid]

def generateIntAdd():
	a = randint(1000,9999999)
	b = randint(1000,9999999)
	answer = a + b
	return validateIntAnswer(a,b,'+',answer)

def generateIntSub():
	a = randint(1000,9999999)
	b = randint(1000,9999999)
	answer = a - b
	return validateIntAnswer(a,b,'-',answer)

def generateIntMult():
	a = randint(10,1000)
	b = randint(10,100)
	answer = a * b
	return validateIntAnswer(a,b,'*',answer)

def generateIntDiv():
	a = randint(10,999)
	b = randint(3,99)

	if a < b:
		temp = a
		a = b
		b = temp

	answerQuo = a // b
	answerRem = a % b
	return validateIntDivAnswer(a,b, answerQuo, answerRem)

def generateFloat(min=10.0, max=999.0, multiplier = 1000):
	return ceil(uniform(min,max)*multiplier)/multiplier

def generateFloatAdd():
	a = generateFloat(10.0,999.0,10000)
	b = generateFloat(10.0,999.0,10000)
	answer = a + b
	return validateFloatAnswer(a,b,'+',answer)

def generateFloatSub():
	a = generateFloat(10.0,999.0,1000)
	b = generateFloat(10.0,999.0,1000)
	answer = a - b
	return validateFloatAnswer(a,b,'-',answer)

def generateFloatMult():
	a = generateFloat(10.0,999.0)
	b = generateFloat(10.0,999.0)
	answer = a * b
	return validateFloatAnswer(a,b,'*',answer)

def generateFloatDiv():
	a = generateFloat(100,9999)
	b = generateFloat(100,9999)

	if a < b:
		temp = a
		a = b
		b = temp

	answerQuo = a // b
	answerRem = a % b
	return validateFloatDivAnswer(a,b, answerQuo, answerRem)


options = [generateIntAdd, generateIntSub, generateIntMult, generateIntDiv,
			generateFloatAdd, generateFloatSub]

numOfProblems = 10

if len(sys.argv) > 1:
	numOfProblems = sys.argv[1]

for i in range(1,numOfProblems):
	print "Problem No: ", i
	op = choice(options)
	data = op()
	data.insert(4,"Answer Given:")
	data.insert(3,"Answer Expected:")
	data.insert(0,strftime("%Y-%m-%d", gmtime()))
	data.insert(0,strftime("%H:%M:%S", gmtime()))
	data.insert(0,i)
	writeSumToFile(data)
