# 3) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილი რიცხვის ჩათვლით
#  დაგვიბრუნებს გამრავლების ტაბულას.
n = int(input("Enter num:"))
def f(num):
    for i in range(1, num + 1):
        for j in range(1, 11):
            return i , j
print(f(n))
#  ????