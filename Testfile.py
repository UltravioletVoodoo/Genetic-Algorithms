import math
import random

Father = [3.123456, 0.99543]
Mother = [3.198765, 0.99345]

StrFather = str(Father[0])
StrMother = str(Mother[0])


print StrFather
print StrMother

child = []
for x in StrFather:
	r = random.randint(1,2)
	if r == 1:
		child = child + [x]
	else:
		child = child + ["*"]
length = len(child)
while length > 0:
	if child[length - 1] == "*":
		child [length - 1] = StrMother[length - 1]
	length = length - 1
child = "".join(child)
print child