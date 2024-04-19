n_cases = int(input())

#For each case
for case in range(0, n_cases):
    #1 to n smallest multiple
    n = int(input())

    #Start on n
    smallest_multiple = n

    while True:
        #Is smallest_multiple divisible by 2..n-1 
        # (n is trivial because we increment by n)
        divisble_by_all = True
        for divisor in range(n-1, 1, -1):
            if (smallest_multiple % divisor != 0):
                divisble_by_all = False
                break

        #The smallest multiple has been found
        if divisble_by_all:
            print(smallest_multiple)
            break
        
        #increment possible smallest multiple by n
        smallest_multiple += n