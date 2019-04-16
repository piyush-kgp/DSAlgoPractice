

def binary_search(A, V):
    first = 0
    last = len(A)-1
    found = False
    while first <= last and not found:
        middle = (first+last)//2
        if A[middle] == V:
            found = True
        else:
            if A[middle] < V:
                first = middle+1
            else:
                last = middle-1
    return found

def tester():
    A = [int(i) for i in input('Enter sorted numbers..\n').split()]
    V = int(input('What to search?\n'))
    print(binary_search(A, V))

tester()



            
