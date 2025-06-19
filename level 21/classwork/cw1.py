# მომხმარებელს შემოატანინეთ სიტყვა მანამ სანამ არ შემოიტანს მინიმუმ 6 ნიშნას
def f(wrd):
    word = input("Enter:")
    while len(wrd) != 6:
        word = input("Enter:")
    return word
print(f())