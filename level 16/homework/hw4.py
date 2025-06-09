# 5) შექმენით ფუნქცია, რომელიც მომხმარებელს შემოატანინებს სახელს სანამ არ
#  შემოიტანს თქვენს სახელს. თან ჩაამატეთ ახალ სიაში. და დააბრუნეთ ეს სია
#  და რამდენი ელემენტისგან შედგება.
name = input("Enter name:")
def f(nm):
    list = []
    while nm != "gabi":
        list.append(nm)
        nm = input("Enter name:")
    return list , len(list)
print(f(name))