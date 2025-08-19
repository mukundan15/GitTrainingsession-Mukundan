def quick_sort(arr):
	if len(arr) <= 1:
		return arr

	pivot = arr[0]
	left = []
	right = []

	for i in range(1,len(arr)):
		if arr[i] < pivot:
			left.append(arr[i])

		else:
			right.append(arr[i])

	return quick_sort(left) + [pivot] + quick_sort(right)

	#heelpppsdaddddddssds

b = [1,2,3,4]

a = [5,2,9,1,3]
print(quick_sort(a))