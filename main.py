
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]



cnum = len(numbers[0])
rnum = len(numbers) // cnum

print ('Sum of rows: ', end=' ')
for i in range(rnum):
	rsum = sum(numbers[i])
	print (rsum, end=' ')
print("Sum of colums:", end = ' ')
for j in range(cnum):
    col = []
    for i in range(rnum):
        col.append(numbers[i][j])
    print(sum(col), end = ' ')


# ******************************
# Make your Code
# ******************************
