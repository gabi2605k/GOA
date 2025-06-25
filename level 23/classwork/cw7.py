# 7)შექმენით ფუნქცია რომელიც ამოშლის სიიდან ლუწ ინდექსზე მდგომ ელემენტებს 
# , და კენტ ინდექსზე მდგომ ელემენტებს ჩაამატებს ახალ სიაში
def f(list):
    lis1 = []
    for i in list:
        if list.index(i) % 2 == 0:
            list.remove(i)
        else:
            lis1.append(i)
    return lis1
print(f([1,2,3,4,5,6]))