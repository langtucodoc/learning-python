#!/bin/env python

from sys import argv

script, filename = argv

print "Ban vua tao mot tap tin la %r." % filename
print "Dang mo file..."
target = open(filename, 'w')

print "Bay gio toi se hoi ban ba dong sau."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "Toi se ghi ba dong tren vao file da tao."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "The la xong, chung ta dong file lai."
target.close()

print "In ra noi dung trong file."
obj = open(filename, 'r')
s = obj.read()
print s
obj.close()
