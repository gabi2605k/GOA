# მომხმარებელს შემოატანინე პაროლი. და ჰქონდეს სამი ცდა.
pasword1 = input("Enter password:")
c = 3
i = 0
while i != c:
    while input("Enter password:") == pasword1:
        i = i + 1
    pasword1 = input("Enter new password:")
print("corect")