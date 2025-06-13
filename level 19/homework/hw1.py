#შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგად დიდი წინადადება. თქვენი მიზანია ეს წინადადება გახლიჩოთ 
# და შეაერთოთ ისევ, ოღონდ ისე რომ თითოეული სიტყვის პირველი ასო იყოს დიდად,
def f(word):
    new = word.split()
    for i in word:
        new.append(i.capitalize())
    return "".join(new)
print(f("goa is best academy"))