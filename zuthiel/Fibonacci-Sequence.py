'''
Created on 29/09/2014

@author: Zuthiel
'''

def getFibonacci(n):
    a = 0
    b = 1
    while n != -1 :
        print (a)
        temp = a
        a = b
        b = b + temp    
        n = n - 1
        
user_number = int(input('Enter a number:'))
getFibonacci(user_number)
