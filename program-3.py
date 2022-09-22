if __name__ == '__main__':
    a = int(input("Enter a number:"))

    if a%2 == 0:
        a = a-1
    p = 1
    for x in range(a):
        print(p, end=',')
        p = p+2
