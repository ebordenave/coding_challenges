def intersection(a, b) -> list:
    unique_values = set(a)
    result = []

    for num in b:
        if num in unique_values:
            result.append(num)
    return result
