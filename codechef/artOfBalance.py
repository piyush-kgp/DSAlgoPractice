
def minOps(string):
    if not string:
        return 0
    L = len(string)
    H = {s: 0 for s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    for s in string:
        H[s] += 1
    num_unique_letters_orig = sum([count>0 for count in H.values()])
    S = list(H.values())
    S = sorted(S)
    changes = list()
    memory = {}
    for i in range(1, 27):
        # print('RUNNING with i, L', i, L)
        if i>L:
            # print('Breaking because no more possible at i = ', i)
            break
        if L%i != 0:
            continue
        num_occur_each = L//i
        relevant_S = S[-i:]
        num_changes = 0
        for item in relevant_S:
            if item>=num_occur_each:
                break
            num_changes+=(num_occur_each-item)
        changes.append(num_changes)
        memory[i] = num_changes
    # print('MEMORY', memory)
    return min(changes) if changes else 0


if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        print(minOps(S))
