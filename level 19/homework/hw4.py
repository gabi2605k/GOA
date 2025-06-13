# შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილი რიცხვის ჩათვლით გამოგვიტანს ყველა კენტი 
# რიცხვის კვადრატის ჯამს
num = int(input())
def f(n):
    sum = 0
    for i in range(1,n):
        if i % 2 == 1:
            sum = i*i
    return sum
print(f(num))