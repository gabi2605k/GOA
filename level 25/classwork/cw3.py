# შექმენით სია, ამ სიაში უნდა იყოს სტრინგები და ეს სია დაასორტირეთ ასო G-ს რაოდენობის მიხედვით კლებადობით.
list = ["gabi","goa","chad"]
def f(l):
    return l.count("G")
print(sorted(list,reversed = True,key = f))