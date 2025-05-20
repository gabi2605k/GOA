# BONUS: შექმენით ფუნქცია რომელიც მომხმარებლის 
# შემოტანილ რიცხვის ჩათვლით გამოგვიტანს ყველა მარტივი რიცხვის ნამრავლს. 
num = int(input("Enter num;"))
def n(nm):
    mar = 0
    for i in range(1,num+1):
        for s in i:
            if s % i:
                mar = mar * s
    return mar
print(n(num))