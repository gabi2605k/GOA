# 5)მომხმარებელს შემოატანინე რიცხვი,for loop ის გამოყენებით
#  გამოიტანე თითოეული რიცხვი ერთიდან ამ რიცხვამდე,იგივე გააკეთეთ While loop-ით
num = int(input("Enter num:"))
for i in range(1,num):
    print(i)

    
j = 0
while j < num:
    j +=1
    print(j)