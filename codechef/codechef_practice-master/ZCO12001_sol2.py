

def brace_tracker(arr):
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
    tracker = brace_tracker(arr)
    x=max(tracker)
    y=tracker.index(x)+1
    return x, y

def max_nest_length(arr):
    tracker = brace_tracker(arr)
    terminals=[0]
    for i in range(len(tracker)):
        if tracker[i]==0: terminals.append(i+1)
    lengths = [terminals[i+1]-terminals[i] for i in range(len(terminals)-1)]
    x=max(lengths)
    y=lengths.index(x)
    z=terminals[y]+1
    return x, z


_ = input()
arr = [int(i) for i in input().split()]
x = max_nest_depth(arr)
y = max_nest_length(arr)
z = [str(i) for i in x+y]
print(' '.join(z))
