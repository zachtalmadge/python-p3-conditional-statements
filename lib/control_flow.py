#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == 'admin' and password == '12345':
        return 'Access granted'
    return 'Access denied'

def hows_the_weather(temp):
    if temp < 40:
        return "It's brisk out there!"
    elif temp >= 40 and temp <= 60:
        return "It's a little chilly out there!"
    elif temp >= 85:
        return "It's too dang hot out there!"
    else: 
        return "It's perfect out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    
    return num

def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print('Invalid operation!')
        return None
