"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# Reference https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution/30450119




check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = find_solution(20)
    if solution is None:
        print ("No answer found")
    else:
        print ("found an answer:", solution)
print(find_solution)

for i in range (1,10):
    print(2520 / i)
      
# https://www.youtube.com/watch?v=Km36RkQToqo
# tell if  a number is divisible by 1 to 20
def isDivisible1to20(number):
    for i in range (2,21): #since all numbers are divisible by 1 we are going to start from 2
        if number % i != 0:
            return False 
    return True 

# starting number 1, check if it's divible by 1 to 20

number = 20 
#since all number are going to be divisble by 2 we are going to start with 2 
#since all numbers need to be divisble by 20 we can just start with 20

while True:
    if isDivisible1to20(number):
        break #if it is true, let break out of the loop
    number += 20 #if it is false, let increment number adding into it
# and also we are going to increment by 20 each time and we don't bother to check with the odd numbers
# we can also increment by 20 for each time until it is True and it break out of the loop

# if we have found the number, stop
print(number)