def f(list):
    newl = []
    for i in list:
        if type(i) == int:
            newl.append(i)
    return newl

print(f([14,51,"gabo"]))