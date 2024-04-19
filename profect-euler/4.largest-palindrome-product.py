n_cases = int(input())

def find_nearest_smaller_palindrome(n):
    chars = str(n)

    first_three_digits = chars[0:3]

    palindrome = first_three_digits
    #Last three digits are the reverse of the first three
    for i in range(2, -1, -1):
        #Concat the string in reverse order
        palindrome += first_three_digits[i]

    palindrome = int(palindrome)

    if (palindrome > n):
        return reduce_palindome(palindrome)
    else:
        return palindrome

#Reduce palindrome by lowering the first 3 digits of the 6 digit palindrome
def reduce_palindome(palindrome):
    #Take away 1000 to reduce third digit
    chars = str(palindrome - 1000)
    
    first_three_digits = chars[0:3]

    #First three digits 
    reduced_palindrome = first_three_digits 
    #Last three digits are the reverse of the first three
    for i in range(2, -1, -1):
        #Concat the string in reverse order
        reduced_palindrome += first_three_digits[i]

    return int(reduced_palindrome)

#Check if palindrome has 2 three digit factors
def has_three_digit_pair_factors(palindrome):

    for divisor in range(100, 999):
        if (palindrome % divisor == 0 and palindrome // divisor < 1000):
            #print(divisor, " and ", palindrome // divisor)
            return True
    
    return False

#For each case
for case in range(0, n_cases):
    n = int(input())

    current_palindrome = find_nearest_smaller_palindrome(n-1)
    
    while True:
        #If the current palindrome has 2 three digit factors, print
        if (has_three_digit_pair_factors(current_palindrome)):
            print(current_palindrome)
            break
        else:
            #If no 3 digit factors, reduce the palindrome and check again
            current_palindrome = reduce_palindome(current_palindrome)
            