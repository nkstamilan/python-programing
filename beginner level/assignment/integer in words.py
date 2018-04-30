import inflect
a=int(input())
p = inflect.engine()
x=p.number_to_words(a)
print(x)
