a = [1, 1, 1, 2, 8, 6, 1]
b = [2, 4, 6, 1, 4, 18, 61]
c = [2, 8, 18, 2, 1, 1, 8]


def solve(a, b, c):
    answer_set = list()
    answer_set.append((a[0], b[0], c[0]))
    for i in range(1, len(a)):
        input_tuple = [a[i], b[i], c[i]]
        sorted_tuple = sorted([a[i], b[i], c[i]])
        found = False
        for items in answer_set:
            if sorted(items) == sorted_tuple:
                found = True
                break
        if not found:
            answer_set.append(input_tuple)

    print(answer_set)


solve(a, b, c)
