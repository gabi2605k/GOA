# 4) შექმენით ფუნქცია რომელიც მომხმარებელს შემოატანინებს სიტყვას მანამ სანამ არ 
# შემოიტანს 'საკმარისია'ს. ეს შემოტანილი სიტყვები დაამატეთ სიაში და გაფილტრეთ
# . სიაში უნდა იყოს ისეთი სიტყვები რომლის სიგრძეც არ აღემატება 5-ს და ურევია რიცხვები.
def s(a):
    atempt = 0
    list = []
    lis = []
    while atempt != 5:
        atempt += 1
        word = input("Enter word: ")
        list.append(word)
    for i in list:
        if len(i) < 5:
            lis.append(i)
    return lis
print(s(1))