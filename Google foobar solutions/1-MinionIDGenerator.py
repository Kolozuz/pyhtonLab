from math import sqrt

def is_prime(i):
    # check if i can be divided by a number equal or lower than the squared root of i, different than 1 and itsef
    if i < 2:
        print("False")
        return False

    for num in range(2, round(sqrt(i))+1):
        if i % num == 0:
            print("False")
            return False
    
    print("True")
    return True    

def solution(i):
    prime_nums = ""
    next_five_prime_nums = ""

    z = 1

    while len(prime_nums) < 10000:
        if is_prime(z):
            prime_nums += str(z) 

        z+=1

    x = i

    while len(next_five_prime_nums) < 5:
        next_five_prime_nums += prime_nums[x]
        x += 1
    
    return next_five_prime_nums

print(solution(0))
