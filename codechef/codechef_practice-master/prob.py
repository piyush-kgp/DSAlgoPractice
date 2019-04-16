T = int(input('Enter Target\n'))
A = [int(i) for i in input().split()]

def isPairSum(A, T):
	S=set()
	i=0
	while i<len(A):
		if T-A[i] in S:
			return True
		else:
			S.add(T-A[i])
			#print(S)
		i+=1
	return False

print(isPairSum(A, T))
