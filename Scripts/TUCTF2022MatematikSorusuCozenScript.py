from pwn import *
import re
import logging

datam = remote("chals.tuctf.com", 30202)
k = 0
for dongu1 in range(510000):
		if k == 0:
			k+=1
			question = str(datam.recvline())
			if "exec" in question:
				continue
			print(question)
			unquest = question[2:100]
			unquest2 = unquest[:-3]
			cevap= str(eval(unquest2))
			print(cevap)
			datam.sendline(cevap)
			print(str(datam.recvline()))
		else:
			question = str(datam.recvline())
			if "exec" in question:
				continue
			print(question)
			unquest = question[2:100]
			unquest2 = unquest[:-3]
			cevap= str(eval(unquest2))
			print(cevap)
			datam.sendline(cevap)
			print(str(datam.recvline()))
