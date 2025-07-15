# Readability counts. So uncomment the import line if you want to have more output on your console,
# or you're not zen enough.

# import this

# Ex 1 : FizzBuzz
# Logic of my solution : 
# First step is to generate the numbers from 1 to 100.
# If the number is divisible by 3, print "Fizz".
# If the number is divisible by 5, print "Buzz".
# If the number is divisible by both 3 and 5, print "FizzBuzz".
# If the number is not divisible by either, print the number itself.
#so a range of numbers is created and then checked for divisibility via if statements.
# We check first if the number is divisible by both 3 and 5, then check for 3 and then for 5. 


def fizzbuzz():
    for num in range(1, 101): 
        if num %3 == 0 and num %5 == 0:
            print("FizzBuzz")
            next
        if num %3 == 0:
            print("Fizz")
            next
        if num %5 == 0:
            print("Buzz")
            next
        
        print(num)  

# - Bonus point: make your function accept a dict parameter containing multiple: word to
# output. So the program above would be
# yourfunction({
# '3': 'Fizz',
# '5':'Buzz',
# })
# But we could totally send you
# yourfunction({
# '4': 'Fizz',
# '9': 'Buzz',
# '12': 'Lazz'
# })

# Logic of my solution:
# So i accept a dict parameter and iterate through it to check the divisibility of the numbers.
# The keys of the dict are the divisors and the values are the words to output.
# i just have to iterate through the settings dictionary and then check if the number is divisible by the key.
# If it is, i append the value to the output string. that's how i can handle multiple words for different divisors.
def bonus_fizzbuzz(settings):
    for num in range(1, 101):
        output = ""
        for key, value in settings.items():
            if num % int(key) == 0: # Converting key to int for divisibility check
                output += value
        print(output if output else num)

# TESTING :
#fizzbuzz()
#bonus_fizzbuzz({'3': 'Fizz', '5': 'Buzz'})
bonus_fizzbuzz({'4': 'Fizz', '9': 'Buzz', '12': 'Lazz'})