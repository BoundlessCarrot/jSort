def eSort(arr, arr1, maxi):
	for i in range(0, maxi + 1):
		for j in range(0, len(arr)):
			if arr[j] == i:
				arr1.append(arr[j])
				print(arr1)

testArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
finArr = []
eSort(testArr, finArr, 9)
print(finArr)

#I guess this would have a best/worst/avg case of O(n^2)?