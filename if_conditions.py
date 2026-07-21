
# CONDITIONAL EXECUTION if-else statement

if sheep_counter >= 10:
    sleep_and_dream() # If the sheep counter is greater than or equal to 10, call the sleep_and_dream function
    make_bed()
    take_a_bath()
    feed_the_sheep_dogs()
    
if the_weather_is_good:
    go_for_a_walk() # If the weather is good, call the go_for_a_walk function
    take_photos()
    enjoy_the_scenery()
else:
    go_to_theater() # If the weather is not good, call the go_to_theater function
have_lunch() #have lunch regardless of the weather

# NESTED if-else statement
if the_weather_is_good:
    if the_sun_is_shining:
        go_for_a_walk() # If the weather is good and the sun is shining, call the go_for_a_walk function
        take_photos()
        enjoy_the_scenery()
    else:
        go_to_theater() # If the weather is good but the sun is not shining, call the go_to_theater function
else:
    if tickets_are_available:
        go_to_theater() # If the weather is not good but tickets are available, call the go_to_theater function
    else:
        go_shopping() # If the weather is not good and tickets are not available, call the go_shopping function
        
# elif statement

if the_weather_is_good:
    go_for_a_walk() # If the weather is good, call the go_for_a_walk function
    take_photos()
    enjoy_the_scenery()
    
elif tickets_are_available:
    go_to_theater()
    
elif table_available():
    go_for_lunch()
    
else:
    play_chess_at_home()
    
# Analyzing Code Samples

# Read Numbers
Number1 = int(input("First Number: "))
Number2 = int(input("Second Number: "))

# Choose the Largest Number
if Number1 > Number2:
    largest_number = Number1
else:
    largest_number = Number2
    
# Print result
print("The largest number is:", largest_number)

# Read two Numbers
Number1 = int(input("First Number: "))
Number2 = int(input("Second Number: ")) 

if Number1>Number2:
    largest_number = Number1
else:
    largest_number = Number2
    
print("The largest number is:", largest_number)

# Read three Numbers

Number1 = int(input("First Number: "))
Number2 = int(input("Second Number: "))
Number3 = int(input("Third Number: "))

largest_number = Number1

if Number2 > largest_number:
    largest_number = Number2
    
if Number3 > largest_number:
    largest_number = Number3

print("The largest number is:", largest_number)

x = "1"
 
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")
 
 
# while loop

#infinite loop
while True:
    print("This is an infinite loop, am stuck in it. Press Ctrl+C to stop it.")
    
while True:
    print("I am Don A Young Man Indeed")
    
# Calculates how many odd and even numbers are entered by the user until the user enters 0

odd_number = 0
even_number = 0

number = int(input("Enter a number: "))

while number != 0:
    if number % 2 == 0:
        odd_number += 1
    else:
        even_number += 1
        
    number = int(input("Enter a number: "))

print("Odd numbers:", odd_number)
print("Even numbers:", even_number)

# Counter variable to exit loop
counter = 70000
while counter != 32576:
    print("Finding a Match." ,counter)
    counter -= 1
print("Match Found." ,counter)

# Practice 
secret_number = 777

while True:
    guess = int(input("Enter an integer number: "))

    if guess == secret_number:
        print(secret_number)
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")
        
# For Loop
for i in range(100):
    # do something()
    pass

for i in range(100):
    print("These are the integers", i)