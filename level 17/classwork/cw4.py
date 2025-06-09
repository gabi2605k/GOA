# 4)შექმენით ფუნქცია რომესლაც გადაეცემათ სტრინგი,თქვენი დავალებაა შეამოწმოთ თუ
#  ამ სტრინგის პირველი ასო იქნება uppercase ანუ დიდი მაგ შემთხვევაში დააბრუნეთ True
#  სხვა შემთხვევეაში დააბრუნეთ False
name = input()
def f(str):
    for i in str:
        if i == i.capitalize():
            return True
        else:
            return False
print(f(name))