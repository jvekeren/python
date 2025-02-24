word="yes"
word="no"
a=(len(word))
print (a, word[:a-1])
a,b=1,2
while b<1000 :
    print(b, end=",")
    a,b=b,a+b
print(b)
print ("\nklaar")

a=b=c=1
a=2
print(a,b,c)

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list
print (tuple)
print (list)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def concat(*args, sep="-"):
    return sep.join(args)

print(concat("1","2","3"))
print(concat("een","twee","drie"))
print(concat("earth", "mars", "venus", sep="/"))


input("\n\nPress the enter key to exit.")
