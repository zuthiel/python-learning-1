'''
Created on 29/09/2014

@author: Zuthiel
'''

def getFibonacci(n):
    a = 0
    b = 1
    f = True
    
    while n != 0 :
        if f == True :
            print (a)
            print (b)
            f = False
        elif a == 1 & b != 2 :
            print (a)

        elif f == False:
            print (b)
        temp = a
        a = b
        b = b + temp    
        n = n - 1
        
user_number = int(input('Enter a number:'))
getFibonacci(user_number)
