# 1)ფუნქციამ მიიღოს სტრინგი და შეამოწმოს არის თუ არა ის პალინდრომი (წინიდან და უკნიდან ერთნაირად იკითხება).
# 👉 მაგალითი: "level" → True, "hello" → False
def f (wrd):
    if wrd == wrd[::-1]:
        return True
    else:
        return  False
print(f("level"))