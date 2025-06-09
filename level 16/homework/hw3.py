# 4) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ სიტყვას ასო a-ზე გახლიჩავს და დააბრუნეთ სიის სახით.
word = input("Enter word:")
def f(wrd):
    return wrd.split("a")
print(f(word))