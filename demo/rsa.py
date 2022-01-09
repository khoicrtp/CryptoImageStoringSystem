import numpy as np
import random
def bezout(a, b):
    if(b==0 ):
        return a,1,0    
    m, n = a, b
    xm, ym = 1, 0
    xn, yn = 0, 1
    while (n > 0):
        q = m // n # chia lấy phần nguyên
        r = m % n # chia lấy phần dư
        xr, yr = xm - q*xn, ym - q*yn
        m = n
        xm, ym = xn, yn
        n = r
        xn, yn = xr, yr
    return xm,ym

def modular_inverse(num, modulus):
    _,d = bezout(modulus, num)
    return d if(d>0) else d+modulus

def modular_power(base, exp, modulus):
    result = 1
    base %= modulus

    while exp:
        if exp % 2 == 1:
            result = (result * base) % modulus
        exp >>= 1
        base = (base ** 2) % modulus

    return result
def is_prime(n, k=10):
    #Base Cases
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    # Try k times
    else:
        for i in range(k):
            #random numbern [2..n-2]     
            a = random.randint(2, n - 2)
            # Fermat's little 
            if modular_power(a, n - 1, n) != 1:
                return False
            
    return True

def get_random_prime(num_bits):
    lower_bound = 2 ** (num_bits - 2)
    upper_bound = 2 ** (num_bits - 1) - 1
    guess = random.randint(lower_bound, upper_bound)

    if guess % 2 == 0:
        guess += 1

    while not is_prime(guess):
        guess += 2

    return guess
def gcd(x,y):
    g=0
    while((x&1)==0 and (y&1)==0):
        g=g+1
        x=x>>1
        y=y>>1   
    while(x>0):
        while((x&1)==0):
            x=x>>1
        while((y&1)==0):
            y=y>>1
        if(x>=y):
            x=int((x-y)/2)
        else:
            y=y-x
    return y<<g
def coprime(a, b):
    return gcd(a, b) == 1
    
def create_key_pair(prime_bit_length):
    p = get_random_prime(prime_bit_length)
    q = get_random_prime(prime_bit_length)
    n = p * q
    totient = (p - 1) * (q - 1)
    while True:
        e_candidate = random.randint(3, totient - 1)
        if e_candidate % 2 == 0:
            e_candidate += 1
        if coprime(e_candidate, totient):
            e = e_candidate
            break
    d = modular_inverse(e, totient)
    
    return e, d, n
# E,D,N= create_key_pair(10)
def encryptKeyHill(A,E,N):
  for i in range(len(A)):
    for j in range(len(A)):
      A[i][j]=modular_power(A[i][j],E,N)
  return A
def decryptKeyHill(A,D,N):
  for i in range(len(A)):
    for j in range(len(A)):
      A[i][j]=modular_power(A[i][j],D,N)
  return A
