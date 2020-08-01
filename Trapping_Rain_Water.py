# My Solution

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split(" ")[:-1]]
    n = len(arr)
    i = 0
    su = 0
    for j in range(1, n):
        if(arr[j]<arr[i]):
            continue
        elif(arr[j]>=arr[i]):
            for k in range(j-1, i, -1):
                su += arr[i] - arr[k]
            i = j
            
    while(i != n-1):
        ma = arr[i+1]
        ind = i+1
        for k in range(i+2, n):
            if(ma < arr[k]):
                ma = arr[k]
                ind = k
                
        for k in range(ind-1,i,-1):
            su += arr[ind] - arr[k]
        
        i = ind
        
    print(su)

# Hint Solution given after problem submission.
'''
def TrappingWater(arr,n):
	left_max = 0
	right_max = 0
	result = 0
	low = 0
	high = n-1

	while(low<=high):
		if(arr[low]<arr[high]):
			if(arr[low] > left_max):
				left_max = arr[low]
			else:
				result += left_max - arr[low]
			low += 1

		else:
			if(arr[high] > right_max):
				right_max = arr[high]
			else:
				result += right_max - arr[high]
			high -= 1
	return result


if __name__ == "__main__":

	t = int(input())
	while(t>0):
		n = int(input())
		lst = [int(x) for x in input().strip().split()]
		print(TrappingWater(lst,n))


		t -= 1
    
    '''
