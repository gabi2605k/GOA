def multiples_of_five(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 3 == 0:
            result.append(num)
    return result