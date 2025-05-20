# 4) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია სადაც
#  იქნება სხვადასხვა ტიპის მონაცემი
# . გაიგეთ ამ სიაში რიცხვების ჯამი 
def lis(list):
    sum = 0
    for i in list:
        if type(i) == int or type(i) == float:
            sum  += i
    return sum 
print(lis([41,61,14.0,15.12,"sqr",True]))