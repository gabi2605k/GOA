# 5)შექმენით სია სადაც შეიყვანთ რიცხვებს,თქვენი დავალებაა გაიგოთ ლუწ ინდექსზე მდგომი ელემენტების ჯამი
nl = [2,61,93,18,621]
j = 0
for i in range(0,len(nl)):
    if i % 2 == 0:
        j += nl[i]
print(j)