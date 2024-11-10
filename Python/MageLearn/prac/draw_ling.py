def ling(x):
    y = 2 * x
    for i in range(1,y):
        for j in range(abs(i-x)):
            print(" ", end="")
        for k in range(2 * (x-abs(i-x)) - 1):
            print("*", end="")
        print("")

ling(3)