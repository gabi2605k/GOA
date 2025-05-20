# 2) შექმენით ფუნქცია, რომესლაც გადაეცემა მომხმარებლის შემოტანილი ტექსტი და დაითვლით
#  ასო 'a'-ს რაოდენობას. (დიდადაც რომ იყოს დაწერილი ისიც რომ ჩაითვალოს). 
text = input("Enter text: ")
def sig(txt):
    count = 0
    for i in txt:
        if i == "a" or i == "A":
            count += 1
    return count
print(sig(text))
