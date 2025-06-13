# 5)1 დან 50 მდე გამოიტანეთ მხოლოდ ის რიცხვები რომლებიც იყოფიან 5 ზეც და 3 ზეც,შეასრულეთ while loop 
# / for loop ორივეთი
for i in range(1,100):
    if i % 5 == 0 and i % 3 == 0:
        print(i)

s = 0
while s < 100:
    s += 1
    if s % 5 == 0 and s % 3 == 0:
        print(s)

        