# 4)შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია,
# თქვენი დავალებაა ამ სიიდან ამოშალოთ კენტი რიცხვები და 
# დააბრუნოთ სია კენტი რიცხვების გარეშე
def f(num):
    for i in num:
        if i % 2 != 0: 
            num.remove(i)
    return num
print(f([41,25,44,98,414225]))