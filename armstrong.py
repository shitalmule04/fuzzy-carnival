abc=int(input("Enter number"))
ab=int(abc//10)
a=int(ab//10)
b=int(ab%10)
c=int(abc%10)
if (a**3 + b**3 + c**3)==abc:
        print('yes')
else:
        print('Not')

