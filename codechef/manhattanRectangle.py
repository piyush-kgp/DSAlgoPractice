
def getRect(distances):
    return {'found': True, 'coords':'1, 2, 3, 4'}

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        distances = []
        for _ in range(1000):
            print('Q 1 2')
            d = int(input())
            distances.append(d)
            res = getRect(distances)
            if res['found']:
                print('A '+res['coords'])
                break
        verdict = int(input())
        if verdict<0:
            exit('WA')
        if verdict>0:
            continue
