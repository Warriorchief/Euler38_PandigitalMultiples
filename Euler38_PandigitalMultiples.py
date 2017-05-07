"""
Euler38_PandigitalMultiples
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
import time 

def make_concat(x):
    s=str(x)
    i=2
    while len(s)+len(str(x*i))<10:
        s+=str(x*i)
        i+=1
    if len(s)!=9:
        return '0' #if it doesn't make a 9-term integer, mark it as eliminated using '0'
    return s
    
def assemble_concats():
    c=[]
    i=3
    while i<10000:
        c.append(make_concat(i))
        i+=1
    #print(len(c))
    return c
    
things=sorted(assemble_concats(),reverse=True) #print(len(things)) #--> 9997
print(things)


def is_pandigital(x):
    for i in range(1,10):
        if str(i) not in x:
            return False
    return True 

def main():
    for t in things:
        if is_pandigital(str(t)):
            print('found it!',t)
            return t 

start=time.time()
main()      #--> found it! 932718654 CORRECT 
elapse=time.time()-start
print('this took processing time:',elapse)   #this took processing time: 0.0009310245513916016