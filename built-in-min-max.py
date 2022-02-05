#Module 3 - Chapter 4: built-in-min-max 
#Ryan Smith

#Building a maximum function


def maximum(value1, value2, value3):
    """Return the maximum of three values:"""
    
    max_value = value1
    
    if value2 > max_value:
        max_value = value2
        
    if value3 > max_value:
        max_value = value3
        
    return max_value

print('Enter 3 numbers to find the maximum')

value1 = int(input('Enter value 1: '))
value2 = int(input('Enter value 2: '))
value3 = int(input('Enter value 3: '))

print('The maximum of your numbers is:', maximum(value1, value2, value3))


print('Here is same function picking out number from the set without user input.')

number_set = [12,36,27]

print('The number set is', number_set)

print(maximum(12,36,27))

print('Here is example of the built in max() function getting the max from a set.')

number_set2 = [15,35,42,22,17]

print('This number set is ', number_set2)

print(max(number_set2))

##Defining a minimum Function

def minimum(number1, number2, number3):
    """Return the minimum of the three numbers."""
    
    min_value = number1
    
    if number2 < min_value:
        min_value = number2
        
    if number3 < min_value:
        min_value = number3
    
    return min_value

print('Enter 3 numbers to determine the minimum using a built minimum fuction.')

number1 = int(input('Enter value 1: '))
number2 = int(input('Enter value 2: '))
number3 = int(input('Enter value 3: '))

print('The minimum number in your set is:', minimum(number1, number2, number3))

#using the built in min() function

number_set3 = [15, 9, 27, 14]

print('Here we are finding the minimum number using built in min() function: ', number_set3)

print('The minimum from the set above is: ', min(number_set3))
      