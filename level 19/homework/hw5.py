# შექმენით ფუნქცია რომელიც მომხმარებელს შემოტანილ სიტყვიდან ლიწ 
# ინდექსზე მდგომ სიმბოლოების გაერთიანებას დაგვიბრუნებს
w = input()
def f(word):
    new = ""
    for i in word:
        if word.index(i) % 2 != 0:
            new += i
    return new
print(f(w))