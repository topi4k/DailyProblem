import numpy as np
import time


def defi2210_v1(numbers):
    start_time = time.time()
    tot = np.prod(numbers)
    return [tot / k for k in numbers], "--- %s seconds ---" % (time.time() - start_time)


def defi2210_v2(numbers):
    start_time = time.time()
    result = []
    for k in range(len(numbers)):
        to_add = 1
        for cur in numbers:
            if cur != numbers[k]:
                to_add *= cur
        result += [to_add]
    return result, "--- %s seconds ---" % (time.time() - start_time)


print(defi2210_v1(list(range(1, 20))))

print(defi2210_v2(list(range(1, 20))))
