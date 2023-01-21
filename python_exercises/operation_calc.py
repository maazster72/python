"""
This program takes two operands and returns the following:
sum
product
ratio
modulus
exponentiation
"""

import math

#operations_results
def sum(op1, op2):
    return op1 + op2

def product(op1, op2):
    return op1 * op2

def modulus(op1, op2):
    return op1 % op2

def exponentiation(op1, op2):
    return op1 ** op2

#ratio
def ratio(op1, op2):
    hcf = math.gcd(op1, op2)
    antecedent = int(op1/hcf)
    consequent = int(op2/hcf)
    res = []
    res.append(antecedent)
    res.append(consequent)

    return res


#operations_strings
def strSum(op1, op2):
    res = str(op1) + " + " + str(op2) + " = " + str(sum(op1,op2))
    return res

def strProduct(op1, op2):
    res = str(op1) + " * " + str(op2) + " = " + str(product(op1,op2))
    return res

def strModulus(op1, op2):
    res = str(op1) + " mod " + str(op2) + " = " + str(modulus(op1,op2))
    return res

def strExponentiation(op1, op2):
    res = str(op1) + "^" + str(op2) + " = " + str(exponentiation(op1,op2))
    return res

def strRatio(op1, op2):
    nums = ratio(op1, op2)
    res = str(nums[0]) + ":" + str(nums[1])
    return res


def showEquations(op1, op2):
    operations = [
        strSum(op1, op2),
        strProduct(op1, op2),
        strModulus(op1, op2),
        strExponentiation(op1, op2),
        strRatio(op1, op2),
    ]
    for i in range(len(operations)):
        print(operations[i])

#main_program

def main():
    num1 = int(input("Enter the first operand: "))
    num2 = int(input("Enter a second operand: "))
    showEquations(num1, num2)

main()
