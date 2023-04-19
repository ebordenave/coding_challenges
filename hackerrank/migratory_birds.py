from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    return Counter(sorted(arr)).most_common(1)[0][0]


arr = [3, 3, 2, 2, 1, 1]
print(migratoryBirds(arr))
