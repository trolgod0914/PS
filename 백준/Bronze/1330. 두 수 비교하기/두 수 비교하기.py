a, b = input('').split()
if int(a) > int(b):
    print(">")
else:
    if int(a) < int(b):
        print("<")
    else:
        print("==")