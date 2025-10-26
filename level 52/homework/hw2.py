def categorize_numbers(lst):
    positive = 0
    negative = 0
    zero = 0
    for num in lst:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1

    return positive, negative, zero
