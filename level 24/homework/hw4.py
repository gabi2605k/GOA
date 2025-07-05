# 4)შექმენი ფუნქცია რომელსაც გადაეცემა სია,შენი დავალებაა შეამოწმო თუ ამ სიაში მყოფი სახელების 
# სიმბოლოები დგანან კენტ ინდექსზე და ასევე არიან lowercase ები,ჩაამატო ერთ მთლიან სიაში ასეთი ასოები
def f(list):
    ls = []
    for i in range(0,len(list)):
        if i % 2 != 0:
            ls.append(i)
    for s in list:
        if s == s.lowercase():
            ls.append(s)
    return ls
print(f(["str","gabo","Goa"]))