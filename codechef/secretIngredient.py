T = int(input())
for _ in range(T):
    dishes = []
    num_dishes = int(input())
    for _ in range(num_dishes):
        dishes.append(set(input()))
    main_ingredient = set.intersection(*dishes)
    print(len(main_ingredient))
