# შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ წინადადებაში ხმოვან ასოებს გაფილტრავს.
def f(list):
    x = "aeiou"
    nlist = []
    for i in list:
        if i in x:
            nlist.append(i)
    return nlist
print(f("Goa is best"))
