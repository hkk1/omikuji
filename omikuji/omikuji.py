# -*- coding: utf-8 -*-

import random

random.seed()

i = random.randint(0,2)

if i == 0:
	print(u'大吉')
elif i == 1:
	print(u'中吉')
elif i == 2:
	print(u'吉')
else i == 3:
	print(u'凶')
	
	