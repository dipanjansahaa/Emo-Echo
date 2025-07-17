from collections import Counter

def max_beautiful_subsequence(arr):
    if len(arr) <= 1:
        return len(arr)
    counts = Counter(arr)
    distinct_values = list(counts.keys())
    if len(distinct_values) == 1:
        return 1
    if set(distinct_values) >= {1, 2, 3}:
        result = 3
        if 5 in distinct_values:
            result += 1
        return result
    if set(distinct_values) >= {3, 1, 4}:
        result = 3
        if 5 in distinct_values:
            result += 1
        return result
    if 0 in counts:
        max_with_zero = 1
        non_zeros = [x for x in distinct_values if x != 0]
        if non_zeros:
            max_with_zero += min(1, len(non_zeros))
        return max_with_zero
    return 2

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    print(max_beautiful_subsequence(a))