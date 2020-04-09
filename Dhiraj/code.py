# --------------
# Code starts here

# Create the lists 
class_1= ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2= ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class= class_1+ class_2

print(str(new_class))


# Append the list

# print updated list
new_class.remove('Carla Gentry')
print(str(new_class))

# Remove the element from the list

# print the list



# Create the Dictionary
courses={'Math': 65,'English': 70,'History': 80,'French': 70,'Science': 60}

# Slice the dict and stores  the all subjects marks in variable
Maths= courses.get('Math')
Eng= courses.get('English')
His= courses.get('History')
Fre= courses.get('French')
Sci= courses.get('Science')

# Store the all the subject in one variable `Total`
total= Maths+Eng+His+Fre+Sci
# Print the total
print(total)
# Insert percentage formula
percentage= (total/500)*100
# Print the percentage
print(percentage)



# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

topper=max(mathematics,key=mathematics.get)
print(topper)

# Given string
topper= "Andrew Ng"
print(topper.split())

# Create variable first_name 
first_name= topper[:6]
print(first_name)
# Create variable Last_name and store last two element in the list
Last_name= topper[7:9]
print(Last_name)
# Concatenate the string
full_name= Last_name+' '+ first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name= full_name.upper()
print(certificate_name)
# Code ends here


