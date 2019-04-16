def fibonacci(n):
	if n==1: return [0]
	if n==2: return [0, 1]
	fibArray = [0, 1]
	for i in range(2, n):
		fibArray.append(fibArray[i-1]+fibArray[i-2])
	return fibArray

T = int(input())
for _ in range(T):
	M, N = [int(i) for i in input().split()]

	A = [int(i) for i in input().split()]
	B = [int(i) for i in input().split()]

	F = fibonacci(max(2, N))
	answer = M*F[-2]*sum(A) + M*F[-1]*sum(B)
	print(answer%(10**9 + 7))

