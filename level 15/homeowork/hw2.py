# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი --> "hidroeleqtrosadguri" 
# ,თქვენი დავალებაა ამოშალოთ ამ სტრინგიდან მხოლოდ ხმოვნები და დააბრუნოთ
#  ეს სტრინგი ხმოვნების გარეშე
def f(wrd):
    xmv = []
    for i in wrd:
        if i == "a" or i == "e" or i == 'i' or i == "o" or i == "u":
            xmv.append(i)
    return xmv
print(f("hidroeleqtrosadguri"))