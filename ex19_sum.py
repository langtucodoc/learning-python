#!/bin/env python

# Chuong trinh tinh tong hai so truyen vao

from sys import argv

script, number1, number2 = argv

def sum (a, b):
	sum = float(a) + float(b)
	print "Tong hai so la: %d" % sum
sum(number1, number2)
