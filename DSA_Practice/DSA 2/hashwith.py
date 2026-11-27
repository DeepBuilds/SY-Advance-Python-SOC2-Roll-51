M, N = map(int, input().split())
keys = list(map(int, input().split()))

table = [-1] * M

for key in keys:
    index = key % M

    if table[index] == -1:
        table[index] = key

    elif table[index] % M == index:
        i = (index + 1) % M

        while table[i] != -1:
            i = (i + 1) % M

        table[i] = key

    else:
        displaced = table[index]
        table[index] = key

        i = (index + 1) % M

        while table[i] != -1:
            i = (i + 1) % M

        table[i] = displaced

for i in range(M):
    print(table[i])



    '''
    elif table[index] % M == index:
            i = (index + 1) % M
    
            while table[i] != -1:
                i = (i + 1) % M
    
            table[i] = key
    
        else:
            displaced = table[index]
            table[index] = key
            '''