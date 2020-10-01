# It's never too late to start!
from bisect import bisect_left, bisect_right
import os
import sys
from io import BytesIO, IOBase
from collections import Counter
from collections import deque, defaultdict
import math
import heapq
import re

def sin():
    return input()
def ain():
    return list(map(int, sin().split()))
def sain():
    return input().split()
def iin():
    return int(sin())

LOW = 'abcdefghijklmnopqrstuvwxyz'
UP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAX = float('inf')
MIN = float('-inf')
MOD = 1000000007
def primeFactors(n): 
      
    maxi = MIN
    while n % 2 == 0: 
        maxi = 2
        n = n // 2
    
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            maxi = max(maxi, i)
            n = n // i 
 
    if n > 2:
        maxi = max(maxi, n) 
    return maxi

def sieve(n): 
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime

# Stay hungry, stay foolish!

def main():
    for _ in range(iin()):
        n, k = ain()
        l = ain()
        l += l
        maxi = sum(l[:k])
        suma = maxi
        for i in range(1, n):
            suma -= l[i-1]
            suma += l[i+k-1]
            maxi = max(maxi, suma)
        print(maxi)

        









    



                    
            








        






    



    
    
    


    

    






            







        
    











            


        













            




        





        






        




        
























    




            
        

        













    
    



# Fast IO Template starts

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

if os.getcwd() == 'D:\\code':
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: sys.stdin.readline().rstrip("\r\n")
# Fast IO Template ends

if __name__ == "__main__":
    main()

# Never Give Up - John Cena