#!/bin/env python

# Ex8: Printing, Printing

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
	"Hello World.",
	"Python Programming.",
	"Tong Duy Ngoc.",
	"123HOST."
)

formatter2 = '%r %r %r %r' 

print formatter2 % (
	'Hello World.',
	'Python Programming.',
	'Tong Duy Ngoc.',
	'123HOST.'
)
