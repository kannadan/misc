import random

#creates a list of 100 random numbers and does a quicsort on it

def Quicksort(List, first, last):
	if first < last:
		
		jakaja = partition(List, first, last)
		Quicksort(List, jakaja+1, last)		#RECUUURSIOOON
		Quicksort(List, first, jakaja-1)

	
def partition (List, first, last):
	pivotvalue = List[last]
	left = first
	right = last-1
	done = False
	
	while not done:
	
		while left <=  right and List[left] <= pivotvalue:
			left = left + 1
		while right >= left and List[right] >= pivotvalue:
			right = right - 1
		if right < left:
			done = True
		else:
			temp = List[left]
			List[left] = List[right]
			List[right] = temp
	temp = List[last]
	List[last] = List[left]
	List[left] = temp
	return left
seed = 100
pohja = 0
yla = 100
A = []
for i in range(seed):
	A.append(random.randint(pohja, yla))
L = len(A)-1
a = 0
Quicksort(A, a, L)
print(A)
