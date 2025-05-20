# 4) მომხმარებელს შემოატანინეთ ტექსტი და ამ ტექსტში დაითვალეთ რიცხვების რაოდენობა.
text = input("Enter text")
def sig(txt):
    count = 0
    for i in txt:
        count += 1
    return count
print(sig(text))