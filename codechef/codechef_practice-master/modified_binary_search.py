import copy
'''
pseudocode
integer binary_search(array a, integer n, integer x):
    integer low, high, mid
    low := 1
    high := n
    while low ≤ high:
        mid := (low + high) / 2
        if a[mid] == x:
            break
        else if a[mid] is less than x:
            low := mid+1
        else:
            high := mid-1
    return mid
'''
'''
def binary_search(A, N, X):
    low = 0
    high = N-1
    while low<=high:
        mid = int((low+high)//2)
        if X==A[mid]: break
        if X<A[mid]: 
            high = mid-1
            #print('Looking in the left subarray', A[low:high+1])
        if X>A[mid]: 
            low = mid+1
            #print('Looking in the right subarray', A[low:high+1])
    if A[mid]!=X: return 'X not present in A'
    return mid+1
'''

def mod_bin_search(A, N, X):
    #if A.index(X)+1==binary_search(A, N, X): return 0, 'Nothing needs to be done'
    #
    if N==1: return 0, '0 length array passed'
    cridx = A.index(X)
    low = 0
    high = N-1
    min_idx = A.index(min(A))
    max_idx = A.index(max(A))
    swaps = 0
    #
    while low<=high:
        mid = int((low+high)//2)
        if X==A[mid]: break
        if X<A[mid]:
            if cridx>mid:
                swaps+=1
                temp = A[min_idx]
                A[min_idx] = A[mid]
                A[mid] = temp
                #print('State of A', A)
                min_idx=mid
                #print('Min IDX', min_idx)
            if X<A[mid]: high = mid-1
            if X>A[mid]: low = mid+1
        if X>A[mid]:
            if cridx<mid:
                swaps+=1
                temp = A[max_idx] 
                A[max_idx] = A[mid]
                A[mid] = temp
                #print('State of A', A)
                max_idx=mid
                #print('MAX IDX', max_idx)
            if X<A[mid]: high = mid-1
            if X>A[mid]: low = mid+1
    if A[mid]!=X: return -1, 'Not found'
    return swaps, mid

T = int(input())
for _ in range(T):
    N, Q = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    for __ in range(Q):
        X=int(input())
        A=[i for i in B]
        #print(B)
        #print('Original=', (A), '\nMin Swaps and returned index of mod_bin_search', mod_bin_search(copy.deepcopy(A), N, X))
        print(mod_bin_search(copy.deepcopy(A), N, X)[0])
