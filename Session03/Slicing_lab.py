
# Exchange first and last item

def Exchange_first_last(string_name):
    """Exchange first and last item in string"""
    
    if (len(string_name)==1):
        return string
    
    return string_name[-1]+string_name[1:-1]+string_name[0]

string_name= input("Enter the string name ")
print(Exchange_first_last(string_name))


#Remove every other element from the string

def remove():
    """Display a string with every other item removed"""
    
    print(" show list after removing")
    name= ['shirin', 'nasrin', 'irin','sarmin']
    for item in name:
        name.remove(item)
        
    return name

print(remove())

#Reversed the String

def reversed_string(string):
    """ display reverse string"""
    return string [-1::-1]

string = input("enter the input string ")
print(reversed_string(string))


