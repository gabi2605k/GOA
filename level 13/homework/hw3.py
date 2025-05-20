# 3) შექმენით ფუნქცია, რომელიც მომხმარებლის შემოტანილ float ტიპის მოცანემს გახლიჩავს.
#  შედეგი ასე რომ იყოს :  19.27 => 19 + 0.27 
num = float(input("enter num:"))
def number(nm):
    fl = 0
    ints = int(nm)
    fl = num - ints
    return fl
print(number(num))