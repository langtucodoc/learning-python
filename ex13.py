#!/bin/env python

# Ex11: Parameters, Unpacking, Variables

#name = "Tong Duy Ngoc"

#print "My name is %s" % name
#print "My name is", name

from sys import argv

name, height, weight = argv

print "My name is", name
print "Tall", height
print "Heavy", weight
