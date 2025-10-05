# 3)დაწერე ფუნქცია, რომელიც მიიღებს სტრინგს და დააბრუნებს ყველაზე გრძელ სიტყვას.
# მაგ: "I love programming in Python" → "programming".
def f(l):
    l = " "
    wrd = l.split(" ")
    for i in wrd:
        if len(i) > len(l):
            return l
print(f("goal oriented academy"))