# 3) მომხმარებელს შემოატანინეთ რიცხვი და სიის სახით
#  დააბრუნეთ ისეთი რიცხვები რომლებიც არ იყოფა მომხმარებლის შემოტანილ რიცხვზე.
num = int(input("Enter num:"))
def gam(numb):
    gum = []
    for i in range(1,numb):
        if numb % i != 0:
            gum.append(i)
    return gum
print(gam(num))