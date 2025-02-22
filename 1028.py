def calc(a, b):

    if(b == 0):

        return a

    else:

        return calc(b, a % b)

N = int(input())

for i in range(N):

    a, b = input().split()

    a = int(a)
    b = int(b)

    print("{}".format(calc(a, b)))