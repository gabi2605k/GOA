# 1) შექმენით ფუნქცია, სადაც მოხმარებელს შემოატანინებთ რიცხვს და ამ რიცხვის გამყოფებს დააბრუნებს სიაში.
num = int(input("Enter num:"))
def gam(numb):
    gum = []
    for i in range(1,numb):
        if numb % i == 0:
            gum.append(i)
    return gum
print(gam(num))