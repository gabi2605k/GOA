# 2)შექმენი ფუნქცია რომელსაც გადაეცემა სია,ამ სიაში უნდა იყოს მოთავსებული სახელები,
# თქვენი დავალებაა მიწვდეთ ამ სახელებს და შემდეგ ამ სახელებში მყოფ ასოებს,თქვენი დავა
# ლებაა ახალ სიაში ჩაამატოთ მხოლოდ თანხმოვანია ასოები,შემდეგ ამ სიაში მყოფი ასოები და
# ალაგეთ ანბანის მიხედვით(დაასორტირეთ)მოიძეთ ინფორმაცია თუ როგორ ხდება სორტირება
#  და რომელი ფუნქცია გამოიყენება ამისათვის
def f(list):
    l = []
    x = "aeiou"
    for i in list:
        for k in i:
            if k in x:
                l.append(k)
    return l
lss = ["str","gabo","Goa"]

print(sorted(lss,key=f))