# 2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის
#  შემოტანილი სიტყვა და ამ სიტყვაში დაითვლის ასო "k'ს რაოდენობას.
#  დააიგნოროს ქეის სენსიტიურობა.
word = input("Enter word:")
def k(wordd):
    count = 0
    for i in wordd:
        if i == "k":
            count += 1
    return count
print(k(word))