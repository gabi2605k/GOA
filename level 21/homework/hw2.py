# შექმენით ფუნქცია რომელიც შეაბრუნებს სიის ელემენტებს, (for loop-ით)
def f(l):
    for i in l:
        return i[::-1]
print(f(["gabo",12,"gao"]))