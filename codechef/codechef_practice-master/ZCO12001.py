
def nested(arr):
    i=0
    opens = closes = 0

    nested_loops = []
    while i<len(arr):
        if arr[i]==1:
            opens+=1
        elif arr[i]==2:
            closes+=1
            if opens==closes:
                nested_loops.append((opens, i+2-(opens+closes)))
                opens = closes = 0
        i+=1
    return nested_loops


def max_nested(arr):
    x = nested(arr)
    y = [i[0] for i in x]
    z = [i[1] for i in x]
    maxL = y.index(max(y))
    ind_maxL = z[maxL]
    return 2*maxL, ind_maxL


def nest_depths(arr):
    i=0
    braces = 0
    tracker=[]
    while i<len(arr):
        if arr[i]==1:
            braces+=1
        elif arr[i]==2:
            braces-=1
        tracker.append(braces)
        i+=1
    return tracker


def max_nest_depth(arr):
    tracker = nest_depths(arr)
    x=max(tracker)
    y=tracker.index(x) + 1
    return x, y


_ = input()
arr = [int(i) for i in input().split()]
x = max_nest_depth(arr)
y = max_nested(arr)
z = [str(i) for i in x+y]
print(' '.join(z))
