import random
list1 = ["apple","ball","cat","dog","elephant","shreeja","shreeya","shreena","shreehenna"]
list2 =['aero', 'heather', 'camilo', 'dalaila', 'eliya', 'fencica', 'girwani', 'henna', 'inna', 'juhee', 'kuhee', 'luna', 'mayuu', 'nayuu', 'omnivorous', 'picasso', 'quinn', 'ruhii', 'srk', 'tina', 'upbihar', 'vincenzo', 'wuhuuu', 'xerophyte', 'yuhii', 'zymbiaa']
list3 =["appcar","bancar","catcar","doocar","shree","arch","neup","upr","sube","dhaka","mainal","kharel","adhi","sharm","ojh"]

 
while True: #It is used to run the program until the condition is true.
    while True: #only for  Exceptional handling 

         
            try: #exceptional handling (What if entered password is not int?)
                question = int(input("How many passwords are needed? :"))
               
                break #Is used to break the loop if the user inputs required value.

            except ValueError:
                print("Please enter a number(integer).") 



    if question == 0 or question >= 24 or question < 0: #condition 
        print("Please enter a value between 1 and 24.")

    else:
        print (f"\nPassword Generator \n------------------") 
        for i in range(question):#loop to generate password from list
            result1 = random.choice(list1)
            result2 = random.choice(list2)
            result3 = random.choice(list3)
            pwd = result1 + result2 + result3 #concatenating 
            print (f"{i+1} --> {pwd}") #output layout
        break 
