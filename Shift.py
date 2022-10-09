# Import string library
import string

# Collect input for plaintext
plaintxt = raw_input("Enter Plaintext: ")
cipher = ""
c0 = ""
c1 = ""
c2 = ""
c3 = ""
c4 = ""
c5 = ""
c6 = ""
c7 = ""
c8 = ""
c9 = ""
c10 = ""
c11 = ""
c12 = ""
c13 = ""
c14 = ""
c15 = ""
c16 = ""
c17 = ""
c18 = ""
c19 = ""
c20 = ""
c21 = ""
c22 = ""
c23 = ""
c24 = ""
c25 = ""
c26 = ""

# Ensure input is all uppercase
for i in range(len(plaintxt)) :
	p = plaintxt[i]
	if (p.isupper() == False) :
		print "Plaintext needs to be all uppercase letters!"
		quit()

# Print plaintext, sanity check
print "Plaintext reads: ", plaintxt

# Collect input for shift and typecast to an integer
k = raw_input("Enter shift: ")
k = int(k)

# Ensure input is an integer
if(isinstance(k,int) == False) :
	print "The shift needs to be an integer."
	quit()

# Print shift, sanity check
print "Shift = ", k

# Declare alphabet string in uppercase and create a list/array
alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)

# Make the plaintext the outer loop
for i in range(len(plaintxt)) :
	# Make the alphabet the inner loop
	for j in range(len(alphabet_string)) :
		# Create variables to hold indices
		a = alphabet_string[j]
		p = plaintxt[i]

		# Compare plaintext to the alphabet 
		# If the shift goes out of bounds we have to loop around
		if (p == a and j+k >= 26) :
			cipher += alphabet_string[(j+k)%26]
		elif (p == a and j+k <= 26) :
			cipher += alphabet_string[j+k]

print(cipher)

ciphertxt = raw_input("Enter Ciphertext: ")

# Ensure input is all uppercase
for i in range(len(ciphertxt)) :
	c = ciphertxt[i]
	if (c.isupper() == False) :
		print "Ciphertext needs to be all uppercase letters!"
		quit()

# Make the ciphertext the outer loop
for i in range(len(ciphertxt)) :
	# Make the alphabet the inner loop
	for j in range(len(alphabet_string)) :
		a = alphabet_string[j]
		C = ciphertxt[i]
		if (C == a) :
			# Create variables to hold indices
			c0 += alphabet_string[(j-0)%26]
			c1 += alphabet_string[(j-1)%26]
			c2 += alphabet_string[(j-2)%26]
			c3 += alphabet_string[(j-3)%26]
			c4 += alphabet_string[(j-4)%26]
			c5 += alphabet_string[(j-5)%26]
			c6 += alphabet_string[(j-6)%26]
			c7 += alphabet_string[(j-7)%26]
			c8 += alphabet_string[(j-8)%26]
			c9 += alphabet_string[(j-9)%26]
			c10 += alphabet_string[(j-10)%26]
			c11 += alphabet_string[(j-11)%26]
			c12 += alphabet_string[(j-12)%26]
			c13 += alphabet_string[(j-13)%26]
			c14 += alphabet_string[(j-14)%26]
			c15 += alphabet_string[(j-15)%26]
			c16 += alphabet_string[(j-16)%26]
			c17 += alphabet_string[(j-17)%26]
			c18 += alphabet_string[(j-18)%26]
			c19 += alphabet_string[(j-19)%26]
			c20 += alphabet_string[(j-20)%26]
			c21 += alphabet_string[(j-21)%26]
			c22 += alphabet_string[(j-22)%26]
			c23 += alphabet_string[(j-23)%26]
			c24 += alphabet_string[(j-24)%26]
			c25 += alphabet_string[(j-25)%26]
			c26 += alphabet_string[(j-26)%26]

print(c0)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
print(c9)
print(c10)
print(c11)
print(c12)
print(c13)
print(c14)
print(c15)
print(c16)
print(c17)
print(c18)
print(c19)
print(c20)
print(c21)
print(c22)
print(c23)
print(c24)
print(c25)
print(c26)

#This finds the key with more brevity, above lists all possible keys
#find shift
my_shift = 0
temp = c0
for i in range(26): # run through possible shifts
    if (temp == plaintxt): # if we found right shift, we done
        print(my_shift)
        break
    else:
        my_shift += 1 # add to shift
        temp = ""
        # shift each character of ciphertext by our shift; use algorithm from above;
        # save in temp
        for j in range(len(c0)):
            val = chr( (ord(c0[j]) - my_shift - 65) % 26 + 65 )
            temp = temp + val
