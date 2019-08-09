





print("--------seriesSERIES-1---------")

print("\nDisplay fruit list")

fruit_list=["Apples", "Pears", "Oranges","Peaches"]

for i in range(len(fruit_list)):
    
    print(fruit_list[i] + ", ", end=" ") 




#Add another fruit end of the list and display it
print("\n")
print("Add fruits to the end of list")
fruit_list.append("Grape")
print(fruit_list,"\n")


#Add another fruit to the first of the list and display it
print("Add fruits to the first of list")
list_1=["Melon"]
new_list = list_1 + fruit_list
print(new_list,"\n")


#Add another fruit to the first of the list using insert method

print("Add fruits begining of list ")
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

#Ask the user for a fruit to delete, find it and delete it

print("Ask the user for a fruit to delete, find it and delete it")

fruit_list=["Apples", "Pears", "Oranges","Peaches"]

string_Fruit = input("Please enter a fruit name:")

if string_Fruit not in fruit_list:
    
    
   print("That fruit is not in the list")
   
else:
    
    fruit_list.remove(string_Fruit)
    print(fruit_list)

"""........SERIES-3.....
Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)"""



print("--------SERIES-3---------")

fruit_list=["Apples", "Pears", "Oranges","Peaches"]
print(fruit_list)



print('Ask the user for input like “Do you like apples?” for each fruit in the list making the fruit all lowercase. ') 



for i in fruit_list: 

    string_fruit = input("Do you like " + i.lower() + "? yes/no = ")

    x = True

    while x is True:
        
        if (string_fruit.lower() == 'yes'):
            
            x = True 
            print(fruit_list)
            
            break 

        elif (string_fruit.lower() == 'no'):
            
             x= True
             print(i)
             print("Remove it from list ")
             fruit_list.remove(i)   
             print("display the list\n ",fruit_list)
             break

        else:
            x= False
            print("Please enter yes or no") 
     


print("--------SERIES-4---------")

           
print("Display the list") 
     
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"] 
print(fruit_list) 

print("\nDisplay new list in reverse order ") 
     
newList = [] 
for items in fruit_list:
    reverse_item=items[::-1]
    newList.append(reverse_item)
print(newList)
print("\n")

print("Delete the last item from the list ")

newListCopy = newList[:-1]
print(newListCopy)









    
       
        
       



