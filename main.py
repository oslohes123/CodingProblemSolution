a = [1, 1, 1, 2, 8, 6, 1]
b = [2, 4, 6, 1, 4, 18, 61]
c = [2, 8, 18, 2, 1, 1, 8]


def solve(a, b, c):
    answer_set = list()
    for i in range(0, len(a)):
        input_tuple = sorted([a[i], b[i], c[i]])
        answer_set.append(tuple(input_tuple))

    answer_set = list(dict.fromkeys(answer_set))
    print(answer_set)


solve(a, b, c)
