# 4. შექმენით ფუნქცია, რომელსაც გადაეცემა სია, თქვენი დავალებაა გამოიტანოთ ყველაზე დიდი რიცხვი. 
# (max ფუნქცია არ გამოიყენოთ)
def f(list):
    mnum = list[0]  
    for num in list[1:]:
        if num > mnum:
            mnum = num
    return mnum
print(f([41,15,6161,11,15]))