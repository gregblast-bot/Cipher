# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:22:54 2021

@author: Chris "The Oil Rig" Christ
"""

plaintext = 'ABCD'

# convert to uppercase
plaintext = plaintext.upper()

# set shift
shift = 25;

# get ciphertext
ciphertext = ""
for p in plaintext:
    # get ascii val of new ciphertext character
    val = ord(p) + shift
    # subtract 65 from it
    val = val - 65
    # modulo 26
    val = val % 26
    # add back the 65
    val = val + 65
    # add to ciphertext
    ciphertext = ciphertext + chr( val )

print(ciphertext)

# same as above but done with more brevity
ciphertext = ""
for p in plaintext:
    val = chr( (ord(p) + shift - 65) % 26 + 65 )
    ciphertext = ciphertext + val

print(ciphertext)

#find shift
my_shift = 0
temp = ciphertext
for i in range(26): # run through possible shifts
    if (temp == plaintext): # if we found right shift, we done
        print(my_shift)
        break
    else:
        my_shift += 1 # add to shift
        temp = ""
        # shift each character of ciphertext by our shift; use algorithm from above;
        # save in temp
        for j in range(len(ciphertext)):
            val = chr( (ord(ciphertext[j]) - my_shift - 65) % 26 + 65 )
            temp = temp + val
    
