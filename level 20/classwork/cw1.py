# 1)შექმენით ფუნქცია რომელსაც გადაეცემა სახელები,
# თქვენი დავალებაა ტერმინალში გამოიტანოთ კენტ 
# ინდექსზე მდგომი სახელები და შეინახოთ ახალ სიაში
def f(list):
    nlist =[]
    for i in list:
        if list.index(i) % 2 != 0:
            nlist.append(i)
    return nlist
print(f(["gabi","gio","luka","mate"]))