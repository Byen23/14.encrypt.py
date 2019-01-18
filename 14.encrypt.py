# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17, 2019

File: encrypt.py
Encrypts an input string of lowercase letters and prints.
the result. The other input is the distance value.
@author: Byen23
"""
# This will be my 14th program to be uploaded on Github.

plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
	ordvalue = ord(ch)
	cipherValue = ordvalue + distance
	if cipherValue > ord('z'):
		cipherValue = ord('a') + distance - \
						(ord('z') - ordvalue + 1)
	code += chr(cipherValue)
print(code)