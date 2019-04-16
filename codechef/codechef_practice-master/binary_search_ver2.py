import sys

def binary_search(A, N, X):
    low = 0
    high = N-1
    while low<=high:
        mid = int((low+high)//2)
        if X==A[mid]: break
        if X<A[mid]: high = mid-1
        if X>A[mid]: low = mid+1
    if A[mid]!=X: return 'Dekh ke daal na bhai\nfaaltu log(N) search!!'
    return mid+1

def tester():
    A = [int(i) for i in input('Enter sorted numbers..\n').split()]
    N=len(A)
    while True:
        X = int(input('What to search?(Must be in array)\n'))
        if X==-1: sys.exit()
        print(binary_search(A, N, X))

tester()



            
