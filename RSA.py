import math 
import random 

SHIFT = 96 

def alpha_to_num(a):
  """Mapping of the alphabet [a,b,c,...,z] -> [1,2,3,...,26] 
  Precondition: a in domain of alphabet"""
  return ord(a) - SHIFT 

def num_to_alpha(n): 
  """Inverse mapping of alpha_to_num"""
  return chr(n+SHIFT) 

def lowercase(s): 
  """Returns string [s'] with letters in [s] all lowercased """
  if s == "":
    return s
  
  first = s[0] 
  return first.lower() + lowercase(s[1:])



def encrypt(mssg, lock):
  """RSA encryption of string [mssg] using 2-integer-tuple [lock]""" 


  mssg = lowercase(mssg)
  encrypted_mssg = "" 

  (n1, n2) = lock 
  for lttr in mssg:

    #get corresponding num
    n = alpha_to_num(lttr) 

    #encrypt and add to output 
    encrypted_mssg += num_to_alpha((n**n1)%n2) 
  
  return encrypted_mssg 

def decrypt(mssg, key): 
  """RSA decryption of string [mssg] using 2-integer tuple [key] """
  mssg = lower_case(mssg) 
  (m1, m2) = key 

  decrypted_mssg = "" 
  for lttr in mssg: 

    n = alpha_to_num(lttr)

    decrypted_mssg += num_to_alpha((n**m1)%m2))


def list_primes(n): 
  """Generates list of the first n prime numbers, where [n] is a non-negative integer """
  assert n>= 0 

  output = [] 
  curr_num = 1 
  while len(output) < n: 
    if isPrime(curr_num): 
      output.append(curr_num)
    #else 
    curr_num += 1 
  return output 

def isPrime(p): 
  """Returns true if [p] is a prime number, false otherwise """
  if p < 2:
    return False 
  if p ==2:
    return True 
  
  d = 2
  while d <= math.sqrt(p):
    if p%d == 0: 
      return False 
    d += 1 
  return True 

def generate_RSAKey(n): 
  """Generates RSA Lock and Key for Encryption/Decryption """

  i1 = random.randint(1, n)
  i2 = random.randint(1,n)
  #need to make a few assertions:
    #these aren't equal
    #enough variabilities 
  lst = list_primes(n) 

  #pick primes p and q
  p = lst[i1] 
  q = lst[i2] 
  
  #compute N and totient(N) 
  N = p*q 
  phi_N = (p-1)*(q-1) 

  E = 2 
  possible_vals = [] 
  while E < phi_N:
    if gcd(E,N) == 1 and gcd(E, phi_N) == 1:
      possible_vals.append(E) 

    E += 1 
  
  best_E = findBest(possible_vals, N) 
  lock = (best_E, N) 

  #need to compute key as well 
  find a d: 

  d = 1 
  while (best_E*d)%phi_N != 1:
    d += 1 
  
  best_d = d 

  key = (best_d, N) 
