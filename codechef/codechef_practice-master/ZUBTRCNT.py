
T = int(input())
for t in range(T):
    L, K = list(map(int, input().split()))
    print("Case " + str(t+1) + ": " + str(sum(range(L-K+2))))
