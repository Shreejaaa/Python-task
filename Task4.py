import sys
def caesar_cracker(file_name):# Define a function to crack the Caesar Cipher
    try:
        with open(file_name, "r") as f:# Read the contents of the file and store it as an encrypted message
            encrypted_message = f.read()
    except IOError:
        print("Cannot open '{}'. Sorry about that.".format(file_name))  # Print an error message if the file cannot be opened
        sys.exit(1) # Exit the program with an error code


    shift = 12 #for shift in range(26):
    decrypted_message = "" # Initialize an empty decrypted message
    for ch in encrypted_message: # Iterate over each character in the encrypted message
            if ch.isalpha():
                if ch.isupper(): # If the character is a letter, decrypt it using the current shift value
                    decrypted_message += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
                else:
                    decrypted_message += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
            else:
                decrypted_message += ch # If the character is not a letter, add it to the decrypted message as is   
    print("Shift {}: {}".format(shift, decrypted_message))


if len(sys.argv) < 2: # Check if the correct number of command line arguments were provided
    print("Usage: caesar_cracker.py <encrypted_message_file>")
    sys.exit(1)

file_name = sys.argv[4] #(Sample1,4=shift 12),(Sample1,2=shift 15),(Sample3,2=shift 5)

caesar_cracker(file_name)# Run the Caesar Cipher cracking function using the specified file name

