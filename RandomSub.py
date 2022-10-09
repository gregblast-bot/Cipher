# Import string and random libraries
import string
import random

# Initialize random subtitution table and cipher and deciphered text
random_table = ""
cipher = ""
decipher = ""

# Declare subtitution string in uppercase and create a corresponding list
sub_string = "PRTUF$&NCB!@#)(ZAQWSLH*^JK"
sub_list = list(sub_string)

# Declare alphabet string in uppercase and create a corresponding list
alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)

# Create a random array of numbers from 0-25
numbers = random.sample(range(26), 26)

# Generate a random substitution table by using our random number array
for i in range(len(alphabet_string)) :
	x = sub_string[numbers[i]]
	random_table += x

print("Our Pseudo-Random Substitution Table: ")
print(random_table)

plaintxt = raw_input("Enter Plaintext: ")

# Ensure input is all uppercase
for i in range(len(plaintxt)) :
	p = plaintxt[i]
	if (p.isupper() == False) :
		print "Plaintext needs to be all uppercase letters!"
		quit()

# Create ciphertext of the plaintext input
for i in range(len(plaintxt)):
	for j in range(len(alphabet_string)) :
		# Create variables to hold indices
		a = alphabet_string[j]
		p = plaintxt[i]

		if (p == a) :
			cipher += random_table[j]

print("Cipher Generatred: ")
print(cipher)

# Decrypt ciphertext
for i in range(len(cipher)):
	for j in range(len(alphabet_string)) :
		# Create variables to hold indices
		r = random_table[j]
		c = cipher[i]

		if (c == r) :
			decipher += alphabet_string[j]

print("Deciphered Text: ")
print(decipher)