
def who_wins(A, N, K):
	if N==1: return False
	#we want Player2 to win
	A1 = [A[2*i] for i in range((N+1)//2)] #player1
	A2 = [A[2*i+1] for i in range(N//2)] #player2

	S1 = sum(A1)
	S2 = sum(A2)

	if S2>S1: return True
	if K==0: return False
	D=S1-S2
	A1.sort(reverse = True)
	A2.sort()

	k=0
	while k<K and k<N//2:
		if A1[k]<=A2[k]: return False
		D -= 2*(A1[k]-A2[k])
		if D<0: return True
		k+=1
	return False

T = int(input())

for _ in range(T):
	N, K = [int(i) for i in input().split()]
	A = [int(i) for i in input().split()]
	print('YES') if who_wins(A, N, K) else print('NO')



