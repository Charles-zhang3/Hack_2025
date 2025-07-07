def median(numbers):
    numbers_sorted = sorted(numbers)
    n = len(numbers)
    if n % 2 == 1:
        return numbers_sorted[n // 2]
    else:
        mid1 = numbers_sorted[n // 2 - 1]
        mid2 = numbers_sorted[n // 2]
        return (mid1 + mid2) / 2

