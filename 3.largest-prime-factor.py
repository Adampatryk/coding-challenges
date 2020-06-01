n_cases = int(input())

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        #print '\t',f
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True  

#For each case
for case in range(0, n_cases):
    prime_factors = []

    n = int(input())
    factors = [n]

    #While factors list is not empty
    while len(factors) > 0:
        if is_prime(factors[0]):
            prime_factors.append(factors.pop(0)) #Remove and retrieve factor at index 0
        else:
            #If the factor is not prime, find a pair of factors
            for divisor in range(2, factors[0]//2 + 1): #35 , 35/2 = 17
                if (factors[0] % divisor == 0): #is the factor divisible by the divisor
                    #Append the pair of found factors
                    factors.append(divisor)
                    factors.append(factors[0] // divisor)

                    factors.pop(0) #remove factor that has been replaced
                    break

    #Find largest prime factor
    largest_prime_factor = -1
    for prime in prime_factors:
        if prime > largest_prime_factor:
            largest_prime_factor = prime

    #Output
    print(largest_prime_factor)