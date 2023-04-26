# Kenneth John Costa
# Assignment 4
# Even-Odd

# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; the first text file will be named even.txt 
# that will contains all even numbers extracted from the numbers.txt. 
# The second text file will be named odd.txt that will contains all odd numbers 
# extracted from the numbers.txt.

def process():
    # Open numbers.txt, even.txt, and odd.txt
    with open("numbers.txt","r") as input_text, open("even.txt","w") as output_even, open("odd.txt","w") as output_odd:
        # Read numbers.txt
        numbers = input_text.readlines()
        for line in numbers:
            integer = int(line.strip())
            # If the integers are even:
            if integer % 2 == 0:
               # Write to even.txt
               output_even.write(str(integer) + "\n")
            # If the integers are odd:     
            else:          
               # Write to odd.txt
               output_odd.write(str(integer) + "\n")
process()
