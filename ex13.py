#!/bin/env python

# Ex13: Parameters, Unpacking, Variables

#name = "Tong Duy Ngoc"

#print "My name is %s" % name
#print "My name is", name

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
