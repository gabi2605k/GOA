# შექმენით სია რომელიც სავსე იქნება სტრინგებით და დაასორტირეთ ეს სია ასო კ-ს რაოდენობის მიხედვით
list = ["kvati","gabo","kakali"]
def f(l):
    return l.count("k")
print(sorted(list,key = f))