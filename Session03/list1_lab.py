



#Display all of the contents of the list
#Task-1
print("--------SERIES-1---------")

print("\nDisplay fruit list")

fruit_list=["Apples", "Pears", "Oranges","Peaches"]

for i in range(len(fruit_list)):
    
    print(fruit_list[i] + ", ", end=" ") 





#Add another fruit end of the list and display it
print("\n")
print("Add fruits to the end of list")
fruit_list.append("Grape")
print(fruit_list,"\n")




#ask user for a number and display the fruits correspond to that number
Number = int(input('Please enter a number between 0-4:')) 
print('Number '+ str(Number) +' corresponds to '+fruit_list[Number])
print("\n")

#Add another fruit to the first of the list and display it
print("Add fruits to the first of list")
list_1=["Melon"]
new_list = list_1 + fruit_list
print(new_list,"\n")


#Add another fruit to the first of the list using insert method

print("Add fruits begining of list using insert  ")
fruit_list.insert(0,"Melon")
print(fruit_list,"\n")


#Display all the fruits that begin with “P”, using a for loop.

fruit_list=["Apples", "Pears", "Oranges","Peaches"]

print("Display all the fruits that begin with “P”,\n")
        
for i in fruit_list:
    if "P" in i:
        print(i)
    
       
print("--------SERIES-2---------")



           
fruit_list=["Apples", "Pears", "Oranges","Peaches"]

print("\nDisplay fruit list")
for i in range(len(fruit_list)):
    
    print(fruit_list[i] + ", ", end=" ")

print("\n")    
    
print("Remove the last fruit from the list.")
fruit_list.pop()
print(fruit_list)
print("\n")

#Ask the user for a fruit to delete, find it and delete it

print("Ask the user for a fruit to delete, find it and delete it")

fruit_list=["Apples", "Pears", "Oranges","Peaches"]

string_Fruit = input("Please enter a fruit name:")

if string_Fruit not in fruit_list:
    
    
   print("That fruit is not in the list")
   
else:
    print("found fruit and delete it")
    fruit_list.remove(string_Fruit)
    print(fruit_list)
print("\n")    
    

"""........SERIES-3.....
Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)"""



print("--------SERIES-3---------")

print("\nDisplay fruit list")
fruit_list=["Apples", "Pears", "Oranges","Peaches"]
print(fruit_list)
print("\n")


print('Ask the user for input like “Do you like apples?” for each fruit in the list making the fruit all lowercase. ') 



for fruit in fruit_list: 

    while True:
        
        string_fruit = input("Do you like " + fruit.lower() + "? yes/no = ")
        
        if (string_fruit.lower() == 'yes'):
            
            print(fruit_list)
            
            Break          

        elif (string_fruit.lower() == 'no'):
            
            
             print(fruit)
             print("Remove it from list ")
             fruit_list.remove(fruit)   
             print("display the list\n ",fruit_list)
             break

        else:        
            print("Please enter yes or no:\n") 
     


print("--------SERIES-4---------")

           
print("\nDisplay the list") 
     
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"] 
print(fruit_list) 

print("\nDisplay new list in reverse order ") 
     
new_list = [] 
for items in fruit_list:
    reverse_item=items[::-1]
    new_list.append(reverse_item)
print(new_list)
print("\n")

print("Delete the last item from the list ")

new_list_copy = new_list[:-1]
print(new_list_copy) 
print("\n")








    
       
        
       



