# შექმენით ფუნქცია რომელიც შეამოწმებს არის თუ არა არგუმენტად გადაცემულ სტრინგში ერთი დიდი ასო მაინც
w = input()
def f(wr):
    for i in wr:
        if i == i.capitalize():
            return i
print(f(w))
    