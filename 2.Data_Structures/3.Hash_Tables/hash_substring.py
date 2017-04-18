# python3
import math
import random

def check_prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def generate_prime(l):
    num = 10**l + 1
    while 1:
        if check_prime(num):
            return num
        num = num + 1

def poly_hash(s,p,x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans

def precompute_hashes(t,len_p,p,x):
    len_t = len(t)
    hash_arr = [0] * (len_t-len_p+1)
    s = t[len_t-len_p:len_t]
    hash_arr[len_t-len_p] = poly_hash(s,p,x)
    y = 1
    for i in range(1,len_p+1):
        y = (y*x)%p
    for j in range(len_t-len_p-1,-1,-1):
        hash_arr[j] = (x*hash_arr[j+1] + (ord(t[j]) - y*ord(t[j+len_p]))) % p
    #print("Hash  precompute_hashes: ",hash_arr)
    return hash_arr

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = generate_prime(7) #select the length as 7 for now...
    x = random.randint(1,p-1)
    result = []
    hash_p = poly_hash(pattern,p,x)
    h_arr = precompute_hashes(text,len(pattern),p,x)
    for i in range(0,len(text)-len(pattern)+1):
        #print("Hash_P: ",hash_p," Hash_subs: ",h_arr[i])
        #hash_t = poly_hash(text[i:i+len(pattern)],p,x)
        if hash_p != h_arr[i]:
            continue
        if text[i:i+len(pattern)] == pattern:
            result.append(i)
    return result
    '''
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]
    '''

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
