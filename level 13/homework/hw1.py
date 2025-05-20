# 1) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა მომხმარებლის
#  შემოტანილი სიტყვა. ხმოვნები სადაც იქნება !
#  ნიშნით ჩაინაცვლოს და თანხმოვნები *-ით სხვა დანარჩენი სიმბოლო იყოს ისე როგორ იქნება. 
wordd = input("enter word:")
def wd(word):
    wrd = []
    for i in word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i=="u":
            wrd.append("!")
        else:
            wrd.append("*")
    return wrd
print(wd(wordd))