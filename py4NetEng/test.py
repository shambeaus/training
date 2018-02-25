x = 10
y = 20
z = 30

def simple_func():

    def simple_func2():
        x= 1000
        print(x)
        print(y)
        print(z)

    x = 100 
    y = 200

    print(x)
    print(y)
    print(z)
    simple_func2()

simple_func()


print(x)
print(y)
print(z)