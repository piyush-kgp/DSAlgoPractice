# cook your dish here
def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

def bestWorkingShield(num_soldiers, attacks, defences):
    defence_order = argsort(defences)
    while defence_order:
        curr_defence = defence_order.pop()
        defence = defences[curr_defence]
        attack_prev = attacks[curr_defence-1] if curr_defence>0 else attacks[num_soldiers-1]
        attack_next = attacks[curr_defence+1] if curr_defence<num_soldiers-1 else attacks[0]
        if defence > attack_prev + attack_next:
            return defence
    return -1

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        num_soldiers = int(input())
        attacks = list(map(int, input().split()))
        defences = list(map(int, input().split()))
        print(bestWorkingShield(num_soldiers, attacks, defences))
