def jSort(arr, arr1, maxi):
	for i in range(0, maxi + 1):
		for j in range(0, len(arr)):
			if arr[j] == i:
				arr1.append(arr[j])

testArr = [2, 5, 7, 9, 3, 4, 6, 8, 1]
finArr = []
jSort(testArr, finArr, 9)
print(finArr)

#I guess this would have a time complexity best/worst/avg case of O(n^2) and space complexity of O(n)? IDK.
