import itertools

seq_len = int(input())
S = input()

combination_possible = []


def get_all_substrings(input_string, length):

    return [
        input_string[i:j + 1] for i in range(length)
        for j in range(i + 1, length)
    ]


combination_possible = get_all_substrings(S, seq_len)
# print(combination_possible)
substrings = []
for combination in combination_possible:
    if (combination.count('0') > combination.count('1')):
        substrings.append(combination)

print(len(max(substrings)))