# 2) შექმენით ფუნქცია რომელიც მომხმარებელის შემოატანილ რიცხვის ფაქტორიალს დააბრუნებს.
n = int(input("Enter num:"))
def f(num):
    fac = 1
    for i in range(1,num +1):
        fac = fac * i
    return fac
print(f(n))