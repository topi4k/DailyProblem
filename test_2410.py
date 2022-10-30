def find_the_first(test_list):
    i = 0
    while i < len(test_list):
        b = test_list[i]
        if 0 < b < len(test_list) and b != test_list[b - 1]:
            test_list[i], test_list[b - 1] = test_list[b - 1], test_list[i]
        else:
            i += 1
    test_list = [tst - rng for tst, rng in zip(test_list, [h+1 for h in range(len(test_list))])]
    return next(test_list.index(test_list_item) for test_list_item in test_list if test_list_item != 0)


test = [1, 2, 3, 4, 5, 33, 44, 34, -2, -58, 394, 74, 6, 39, 7, 932, 8]
assert(find_the_first(test)==8)