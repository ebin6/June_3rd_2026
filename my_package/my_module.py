def is_even(num):
    if num%2==0:
        return True
    else:
         return False
    

def is_prime(num):
    flag=True
    if num>1:
        for k in range(2,(num//2)+1):
            if num%k==0:
                return False
            break
    else:
        flag=False
    if flag:
        return True
    else:
        return False