#!/bin/env python

# Ex 16: Reading and Writing Files


obj = open("abc.txt","w")
obj.write("Xin chao cac ban")
obj.close()
obj1 = open("abc.txt","r")
s = obj1.read()
print s
obj1.close()
obj2 = open("abc.txt","r")
s1 = obj2.read(8)
print s1
obj2.close()
