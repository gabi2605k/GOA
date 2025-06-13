wr = input()
def f(w):
    nl = []
    while wr != "საკმარისია":
        nl.append(wr)
        wr = input()
    return nl
print(f(wr))