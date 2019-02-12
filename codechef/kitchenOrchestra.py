
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_DICT = {ALPHABET[i]: i+1 for i in range(len(ALPHABET))}

def prettinessValue(S: str, prettyMelodies: dict) -> int:
    V = 0
    for melody in prettyMelodies:
        if melody in S:
            V+=prettyMelodies[melody]
    return V

def op_1(S, pos, char):
    cost = abs(ALPHABET_DICT[char] - ALPHABET_DICT[S[pos]])
    S[pos] = char
    return S, cost

def op_2(S, start, end, char):
    cost = abs(ALPHABET_DICT[char] - ALPHABET_DICT[S[pos]])
    S[pos] = char
    return S, cost

def optimizeScore(S, prettyMelodies, goodMelodies, budget, cost_3):
    return S

def main():
    N, M, A, X, R = list(map(int, input().split()))
    S = input()
    prettyMelodies = {}
    for _ in range(M):
        T, C = input().split()
        prettyMelodies[T] = int(C)
    goodMelodies = {}
    for _ in range(A):
        P, Q = input().split()
        goodMelodies[P] = Q
    # print('S=', S)
    # print('M =', M, 'Pretty melodies = ', prettyMelodies)
    # print('A =', A, 'Good melodies = ', goodMelodies)
    # print('X =', X, 'R =', R)
    print('S_old = %s, V_old = %s' %(S, prettinessValue(S, prettyMelodies)))
    S_new = optimizeScore(S, prettyMelodies, goodMelodies, budget=X, cost_3=R)
    V_new = prettinessValue(S_new, prettyMelodies)
    print('S_new = %s, V_new = %s' %(S_new, V_new))


if __name__=='__main__':
    main()
