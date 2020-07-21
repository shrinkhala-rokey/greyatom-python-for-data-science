# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class=[]
for i in class_2 : 
    new_class=class_1+class_2
print(new_class)
# Append the list
new_class.append('peter Wasden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}



# Slice the dict and stores  the all subjects marks in variable
Math=courses.get('Math')
English=courses.get('English')
History=courses.get('History')
French=courses.get('French')
Science=courses.get('Science')

# Store the all the subject in one variable `Total`
total=Math+English+History+French+Science
# Print the total
print(total)
# Insert percentage formula
percentage=(total*100)/500
# Print the percentage
print(percentage)



# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

max_marks_scored = max(mathematics,key=mathematics.get)
print (max_marks_scored)

# Given string
key_list = list(mathematics.keys()) 
val_list = list(mathematics.values()) 
topper=key_list[val_list.index(95)]
print(topper)




# Create variable first_name 
first_name,last_name=topper.split()
# Create variable Last_name and store last two element in the list
print(first_name,last_name)
# Concatenate the string
full_name=last_name+' '+first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here


