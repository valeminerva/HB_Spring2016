# for num in range(1,21):
# 	if num == 13:
# 		print "Hello"
# 	else: 
# 		print num

# fruits = ["apples", "oranges", "bananas"]

# # for fruit in fruits:
# # 	print fruit

# for index in range(len(fruits)):
# 	print fruits[index]

def sum_nums(num):
	tot = 0
	for index in range(num):
		tot = index + tot 
	return tot

print sum_nums(5)





