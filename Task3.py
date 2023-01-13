import random
import sys

def generate_email(file, domain_name):
    """
    It takes a file name and a domain name and returns a list of email addresses.
    
    :param file: The name of the file that contains the list of names
    :param domain_name: The domain name of the email address
    """

    
    last_email = domain_name # Domain name for the email addresses

    try:
        with open(file,"r") as outline: #supposing it as outline
            for i in outline:
                student_id = i[:7]  # get student id
                tempor_surname =  i[9:].split(', ')[0]  # get last name
                first_name = i[9:].split(', ')[1].replace('\n', '') # get first name
                
                # Get only the capital letters from the last name
                last_name = ''.join([i.lower() for i in tempor_surname.upper() if i.isupper()])#convertiing upper letter  in small letter
                temporary = ''.join([i[0].lower() +'.' for i in first_name.split(" ")]) #get first letter of each word in first name

                random_number = random.randint(1000,9999)  
                email = temporary +  last_name +str(random_number) + last_email # generate email addresses

                with open("final_text.txt",'a+') as write_in_f: #a+ makes file
                     write_in_f.write(student_id + " " + email +"\n") #writes in file
    except FileNotFoundError:
        print(f'Cannot open "{file}". Sorry about that.')
        
try:
    file =  sys.argv[1] #if 1st item is not your file name then show message (2 item should bee there)
except IndexError:
    print("Missing command-line argument.")
    quit()

generate_email(file, "@poppleton.ac.uk")
