# შექმენით სია რომელიც სტრინგებით იქნება სავსე. გადაუარეთ ამ სიას და თითოეული ელემენტის კენტ
#  ინდექსზე მყოფი სიმბოლოები გაერთიანეთ და ისე ჩაამატეთ ახალ სიაში.
def f(list):
    list1 = []
    for i in range(0,len(list)):
        if i % 2 != 0:
            list1.append(list[i])
    return list1
print(f(["Goa","chad","gabi","gio"]))