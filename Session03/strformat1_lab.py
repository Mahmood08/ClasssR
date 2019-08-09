
#Write a format string that will take four element tuple:
 #Task-1

print("Display tuple after formating ")
tuple=( 2, 123.4567, 10000, 12345.67)

print("file_{:03d}: {:.2f}, {:.2e}, {:.2e}'".format(*tuple))

#Task 2 
print("\nDisplay tuple") 

name = (2, 123.4567, 10000, 12345.67) 

print(f"file_{name[0]:03d}, {name[1]/1000:.2%}, {name[2]:b}, {name[3]:,}") 
print("") 




#Task 3 



print("Display tuple for arbitrary length") 
tuple =(2, 54, 13, 12, 5, 32)

def formatter(in_tuple): 
    if type(in_tuple) == int:

       print("The number is:",in_tuple) 
    else: 

        length = len(in_tuple) 
        form_string = ("{:d}, " * (length -1)) + "{:d}" 
        print("The",len(in_tuple)," numbers are:", form_string.format(*in_tuple)) 
formatter(tuple) 
print("") 


#Task-4
#Write a format string that will take five element tuple
# and print tuple using index number to specify position

print("\nDisplay tuple using index number ")
tuple=( 4, 30, 2017, 2, 27)

print("'{:02d},{:d},{:d},{:02d},{:d}'".format(tuple[3],tuple[4],tuple[2],tuple[0],tuple[1]))


#Task-5
# Take four element list and display it using f string
print("\nDisplay the list using fstring ")
list=['oranges', 1.3, 'lemons', 1.1]
list_1=(f'The weight of an {list[0].upper()} is {list[1]*(1.2)} and the weight of a {list[2].upper()} is {list[3]*(1.2)}\n')

print(list_1)

#Task-6

print("\nprint a table of several rows using Alignment specifiers \n ")
print('{:10}{:10}{:20}'.format('Name',   'Age', ' Cost'))

print('{:10}{:10}{:20}'.format('Michael', '45', '$90.04'))

print('{:10}{:10}{:20}'.format('Allen', '35', '$110.00'))
print('{:10}{:10}{:20}'.format('David', '40', '$1000.00'))

print('{:10}{:10}{:20}'.format('Jonaphen', '50', '$82.60'))
print('{:10}{:10}{:20}'.format('Kye', '55', '$1500.50'))


