#!/usr/bin/env python3
# This script generates 200 codes of length 10 and writes them to file results.txt
# Number varies in range of 0 to 9 inclusive.

import random


f = open("result.txt", 'w')

for _ in range(200):
	code = ''
	for _ in range(10):
		num = random.randint(0,9)
		code += str(num)
	
	f.write(code + '\n')
	
f.close()
	
	





