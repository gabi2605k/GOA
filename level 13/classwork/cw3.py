# 3) შექმენით ფუნქცია რომელსაც არგუმენტად სია, ამ სიაში
#  უნდა იყოს სხვადასხვა ტიპის მონაცემები და დაითვალოს
#  რამდენი სტრინგ ტიპის მონაცემი არის 
def string(list):
    nlist = []
    for i in list:
        if type(i) == str:
            nlist.append(i)
    return nlist
print(string([41,15,"ra","51",True]))