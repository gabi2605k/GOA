# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სხვადასხვა მონაცემეებით სავსე სია,თქვენი დავალებაა 
# ახალ სიაში ჩააამატოთ მხოლოდ სტრინგ ტიპის მონაცემები
def f(list):
    list2 = []
    for i in list:
        if type(i) == str:
            list2.append(i)
    return list2
print(f([14,51,"at","14"]))