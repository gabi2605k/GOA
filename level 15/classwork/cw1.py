# 1)შექმენი ფუნქცია,რომელსაც გადაეცემა სტრინგი --> aleqsandre , თქვენი დავალება
# ა დააბრუნოთ კენტ ინდექსზე მდგომი ასოები
def f(name):
    kent = []
    for i in range(len(name)):
        if i % 2 != 0:  
            kent.append(name[i])
    return kent
print(f("aleqsandre"))