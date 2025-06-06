# 7)შექმენით ფუნქცია რომელსაც გადაეცემა შემდეგი სია["kaxi" , 5 ,"Aleqsandre", 10,
#  "Giorgi" ,20 , "beqa"] თვენი დავალებაა ამ სიიდან ამოშალოთ მხოლოდ integer ები
#  და დააბრუნოთ სია მათ გარეშე
def f(list):
    for i in list:
        if type(i) == int:
            list.remove(i)
    return list
print(f(["kaxi" , 5 ,"Aleqsandre", 10,"Giorgi" ,20 , "beqa"]))