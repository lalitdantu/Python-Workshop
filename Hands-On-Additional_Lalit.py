# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.

def unique(numbers):
  if len(numbers) == len(set(numbers)):
    return True
  else:
    return False
print(unique([1,3,3,4]))
print(unique([1,2,3,4,1,5]))
print(unique([1,1,1,1]))
print(unique([1,2,3,4,5,6]))

#Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. 
#Continues this operation until the number is positive.



#Write a Python program to find the digits which are absent in a given mobile number



#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
import random
vowels = ['a','e','i','o','u']
random.shuffle(vowels)
print(''.join(vowels))

#Write a Python program to find common divisors between two numbers in a given pair.
