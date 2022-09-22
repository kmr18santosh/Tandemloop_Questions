if __name__ == '__main__':
    print('Enter the values (space separated) for the list')
    inp = list(map(int, input().rstrip().split()))
    dict = {}

    for x in range(1,10):
        count = 0
        for y in inp:
            if y%x == 0:
                count += 1
        
        dict[x] = count
    
    print(dict)
