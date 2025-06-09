# 6)შექმენით ფუნქცია რომელსაც გადაეცემა სია -- >["kaxi" , "ana" ,"Aleqsandre", "ia" , "Giorgi" , "Iamze" , "beqa"],
# თქვენი დავალებაა შეამოწმოთ თუ ამ სიიდან თითოეული ელემენტი იწყება დიდ ასოზე ანუ არის capitalize() 
# ეს ელემენტები ადაამატოთ ახალ სიაში და დააბრუნოთ ეს ახალი სია სადაც მოთავსებული გვექნება დიდი ასოთი
#  დაწყებული სიტყბვები
def f(list):
    list2 = []
    for i in list:
        if i == i.capitalize():
            list2.append(i)
    return list2
print(f(["kaxi" , "ana" ,"Aleqsandre", "ia" , "Giorgi" , "Iamze" , "beqa"]))