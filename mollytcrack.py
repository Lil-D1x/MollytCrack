#!/usr/bin/python
import crypt
import sys

if len (sys.argv) != 2:
	print "Crack Pass Linux - Lil D1x"
	print "Use: python "+sys.argv[0]+" wordlist.txt"
	sys.exit()

hash = raw_input("Type The Full Hash: ")
salt = raw_input("Type Only The Salt EX: $6$rC16LuKd$ : ")

file = open(sys.argv[1],'r')
passwords = file.read().split('\n')
for pass1 in passwords:
	result = crypt.crypt(pass1, salt)
	if(result == hash):
		print "Password Found: "+pass1
		sys.exit(0)
	else:
		print "Trying...: ",pass1
file.close()
sys.exit(0)
