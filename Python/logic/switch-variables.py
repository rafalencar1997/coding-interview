
'''
Problem: switch a and b values without using any other variable
'''

def solution(a,b):

    # Write your code here

    a = a + b
    b = a - b
    a = a - b

    # end of code

    return a, b 
