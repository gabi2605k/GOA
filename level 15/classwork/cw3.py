# 3)შექმენი ფუნქცია როომელსაც გადაეცემა სტრინგი --> fortoxali,
# თქვენი დავალებაა დააბრუნოთ თითოეული ასოს ინდექსი სიის სახით
#  (არ გამოიყენოთ len ფუნქცია)
def f(st):
    res = []
    for i in st:
        res.append(st.find(i))
    return res
print(f("fortoxali"))
#3)შექმენი ფუნქცია როომელსაც გადაეცემა სახელებით სავსე
#  სია,თქვენი დავალებაა დააბრუნოთ თითოეული ელემენტის
#  ინდექსი(არ გამოიყენოთ len ფუნქცია)
def d(name):
    res = []
    for i in name:
        res.append(name.index(i))
    return res
print(d(["Gabo","nika","luka","gio"]))