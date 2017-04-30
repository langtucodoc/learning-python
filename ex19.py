#!/bin/env python

# Ham tinh tong hai so

#from sys import argv

#script, number1, number2 = argv
print "Nhap vao so thu nhat: ", 
a = raw_input()
print "Nhap vao so thu hai: ",
b = raw_input()

def sum(number1, number2):
	tong = float(number1) + float(number2) # Ep kieu sang float do dung raw_input()
	print "Tong hai so la: ", tong

sum (a, b)
