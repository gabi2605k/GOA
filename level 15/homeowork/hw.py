# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი,შენი 
# დავალებაა ამ სტრინგიდან ამოშალო კენტ იდექსზე 
# მდგომი ასოები და დააბრუნო სტრინგი მათ გარეშე
def f(name):
    kent = []
    for i in range(len(name)):
        if i % 2 != 0:  
            kent.append(name[i])
    return kent
print(f("Gabo"))