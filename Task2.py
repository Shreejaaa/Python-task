print("Park Run Timer")
print("~~~~~~~~~~~~~~")
print("Let's go!")

total_runners = 0
total_time = 0
fastest_time = None # None is a variable to a value that is not a number
fastest_runner = None
slowest_time = None
records = [] #Making empty list
split_part = []

while True:                          
    datas = input()
    records.append(datas) #appending records in variable data
    if records[0].upper() == "END": #checking whether record's first element is "END" 
        print("Error Error!! No data.")
        break
    elif datas.upper()=="END":  # If the input  is "END" then it will break the loop.
        break
    
    for i in records:   
        a = i.split("::") #spliting the data in i 
        split_part.append(a) # Appending the value of a in split_part.
        
    # total_runners={int(i[0]):int(i[1]) for i in split_part[:-1]}  
        
        
  
    runner_number = a[0] #Taking first element from a and assigning it to runner_number
    time = a[1] #Taking second element from a and assigning it to runner_number
        
  
    if not time.isdigit(): #Error handling (whether time is digit or not)
        print("Error in data stream. Ignorning. Carry on.")
        continue
        
   
    time = int(time) # Converting the time into integer

    
    total_runners = total_runners + 1
    total_time = total_time + time
  
    if fastest_time is None or time < fastest_time: #Checking if fastest time is none or less than time
        fastest_time = time #If true then it will assign value of time to fastest_time
       
        fastest_runner = runner_number # Assigning the value of runner_number to fastest_runner.
        
    if slowest_time is None or time > slowest_time:
        slowest_time = time
        
average_time = total_time / total_runners

def to_minutes_seconds(time): #Convertes time in "seconds" to minutes and seconds
    minutes = time // 60
    seconds = time % 60
    return f"{minutes} minutes, {seconds} seconds"


fastest_time = to_minutes_seconds(fastest_time) # Converting the fastest time in "seconds" to minutes and seconds.
slowest_time = to_minutes_seconds(slowest_time)
average_time = to_minutes_seconds(average_time)


print(f"\nTotal Runners: {total_runners}") #Printing in f-string format
print(f"Average Time:  {average_time}")
print(f"Fastest Time:  {fastest_time}")
print(f"Slowest Time:  {slowest_time}")
print(f"\nBest Time Here: Runner #{fastest_runner}")






