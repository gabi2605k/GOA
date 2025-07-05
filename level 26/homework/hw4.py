# 4)შექმენი ფუნქცია რომელსაც გადაეცემა სია,შენი დავალებაა შეამოწმო თუ ამ სიაში მყოფი სახელების
# სიმბოლოები დგანან კენტ ინდექსზე და ასევე არიან lowercase ები,ჩაამატო ერთ მთლიან სიაში ასეთი ასოები
def f(l):
    ls = []
    for i in range(0,len(l)):
        if i % 2 != 0 :
            ls.append(i)
    for k in l:
        if k == k.lowercase():
            ls.append(k)
    return ls
list = ["Gabrieli","luka",12,61,True,124.67]
print(sorted(list))