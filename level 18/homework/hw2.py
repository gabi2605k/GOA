# 2)შექმენით ფუნქცია,რომელსაც გადაეცემა სტრინგებით სავსე სია,რომელი სტრინგის სიგრძეც მეტია 
# 6 ზე დააბრუნეთ ეს სტრინგები ოღონდ შემოტრიალებული და პირველი ასო ქონდეთ დიდი(CAPITALIZE)
def f(list):
    rstr = []
    revstr = ""
    for i in list:
        if len(i) > 6 :
            revstr = i[::-1].capitalize()
            rstr.append(revstr)
    return rstr
print(f(["gabirlei","gio","luka"]))