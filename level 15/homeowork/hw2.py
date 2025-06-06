# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი --> "hidroeleqtrosadguri" 
# ,თქვენი დავალებაა ამოშალოთ ამ სტრინგიდან მხოლოდ ხმოვნები და დააბრუნოთ
#  ეს სტრინგი ხმოვნების გარეშე
def f(wrd):
    xmv = ""
    for i in wrd:
        if i not in "hdrlqtrsdgr":
            xmv += i
    return xmv
print(f("hidroeleqtrosadguri"))