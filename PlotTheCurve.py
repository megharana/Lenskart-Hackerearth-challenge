no_testcases = int(input())

coefficients_and_mode = [int(x) for x in input().split(" ")]
coefficients = coefficients_and_mode[0:len(coefficients_and_mode) - 1]
mode = coefficients_and_mode[len(coefficients_and_mode) - 1]
len_pair_values = int(input())
pair_values = [int(x) for x in input().split(" ")]
print(coefficients)


def get_possible_pairs(pair_values):
    return [(x, y) for x in pair_values for y in pair_values
            #if x != y
            ]


def find_pairs(possible_pairs):
    count_possible_pair = 0
    for pair in possible_pairs:
        if (pair[1]**2) % mode == (
            (coefficients[0] * pair[0]**3) + (coefficients[1] * pair[0]**2) +
            (coefficients[2] * pair[0]) + (coefficients[3])) % mode:
            print(pair)
            count_possible_pair += 1
    return count_possible_pair


print(get_possible_pairs(pair_values))
possible_pairs = get_possible_pairs(pair_values)
print(find_pairs(possible_pairs))
