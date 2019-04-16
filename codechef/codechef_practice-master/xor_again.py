
T = int(input())
for _ in range(T):
	N = int(input())
	A = [int(i) for i in input().split()]
	if N==1:
		print(2*A[0])
	else:
		xor = A[0]^A[1]
		if N>2:
			for i in range(2, N): xor = xor^A[i]
		print(2*xor)
