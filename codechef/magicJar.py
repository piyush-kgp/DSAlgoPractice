T = int(input())
for _ in range(T):
    num_chefs = int(input())
    dishes = list(map(int, input().split()))
    print(sum(dishes)-num_chefs+1)
