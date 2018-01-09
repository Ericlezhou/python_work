#4-3
for x in range(1,21):
	print(x)
print()
#4-4
for x in range(1,1000001):
	pass#print(x)
print()
#4-5
numList = list(range(1,1000001))
print(min(numList))
print(max(numList))
print(sum(numList))
print()
#4-6
jishu = list(range(1,20,2))
for x in jishu:
	print(x)
print()
#4-7
threeList = list(range(3, 31, 3))
for x in threeList:
	print(x)
print()
#4-8
lifangArr = []
src = list(range(1,11))
for x in src:
	lifangArr.append(x**3)
for x in lifangArr:
	print(x)
print()
#4-9
lifang = [x**3 for x in range(1,11)]
for x in lifang:
	print(x)
