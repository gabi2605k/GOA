# 17)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგებით სავსე სია,შენი დავალებაა შეამოწმო თუ რ
# ამდენი ცალი დიდი ასო ურევია ყველა სტრინგში მთლიანად
def f(list):
    v = "AQZWSEXDRCFTVGYHBUJNIKMOLP"
    g = 0
    for i in list:
        for k in i:
            if k in v:
                g+= 1
    return g
print(f(["gabi",'lukA',"GiorgGi"]))