import operator as op
from functools import reduce
no_testcases = int(input())
import math


def ncr(n, r):

    return math.factorial(n) / (math.factorial(n - r) * math.factorial(r))


def get_charge_threshold(no_elements):
    threshold = 0
    for r in range(0, no_elements + 1):
        threshold += ncr(no_elements, r)
        print(threshold)
    # print(threshold)
    return threshold


for test_case in range(no_testcases):
    no_elements = int(input())
    A = [int(x) for x in input().split(" ")]
    total_charge = 0
    threshold_1 = get_charge_threshold(no_elements - 1)
    for element in A:

        if (element >= threshold_1):
            total_charge += element

    print(total_charge)

# def remove_list(combination_possible):
#     resultant_list = []
#     for x in combination_possible:
#         for y in x:
#             resultant_list.append(y)
#     return resultant_list

# def dict_count(combination_possible):
#     pass
#     count = {}

#     for element in set(A):
#         c = 0
#         for combination in combination_possible:
#             if (element in combination):
#                 c += 1
#         count.update({str(element): str(c)})

#     return count

# combination_possible = []
# for N in range(no_elements + 1):
#     combination_possible.append(list(set(itertools.combinations(A, N))))

# combination_possible = remove_list(combination_possible)
# print(combination_possible)
# charged_dict = dict_count(combination_possible)
# total_charge = 0

# for key, value in charged_dict.items():
#     if (int(key) >= int(value)):
#         total_charge += int(key)
