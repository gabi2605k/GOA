# შექმენით ფუნქცია რომელიც შეამოწმებს არგუმენტად გადაცემულ სტრინგში თუ არის რიცხვი.
w = input()
def f(wr):
    for i in wr:
        if i == "1" or i == "2" or i == "3" or  i == "4" or i == "5" or  i == "6" or i == "7" or i == "8" or  i == "9" or  i == "0":
            return "არის"
print(f(w))