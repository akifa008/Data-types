# Task 1: Using a for Loop
for num in range(1, 11):  
    print(num)

# Task 2: Using a while Loop
count = 1
while count <= 5:  
    print(count)
    count += 1  

# Task 3: Loop with a Condition
user_number = int(input("Enter a number: "))  

while user_number >= 1:  
    print(user_number)
    user_number -= 1     

# Task 4: Nested Loop 
for i in range(1, 4):       
    for j in range(1, 4):   
        print(f"{i} x {j} = {i*j}")

# Task 5: Using break
for i in range(11): 
    if i == 6:     
        break    
    print(i)

# Task 6: Using continue
for i in range(6):  
    if i == 3:      
        continue   
    print(i)
