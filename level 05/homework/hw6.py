# 6)მომხმარებელს შემოატანინე ათზე მაღალი რიცხვი,for loop ის გამოყენებით იპოვეთ 5 
# დან მომხმარებლის შემოტანილ რიცხვამდე ყველა რიცხვის ჯამი,იგივე გააკეთეთ while loop ითაც
num = int(input("Enter num:"))
if num >= 10:
    sum = 0
    for i in range(5,num):
        i +=1
        sum +=i
    print(sum)

    while i < num:
        i +=1
        sum +=i
    print(sum)
