
import sys

#Write a mailroom program where it should have a data structure that holds
#a list donors and a history of the amounts they have donated.
#This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
#It should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.

#If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
#If the user types list show them a list of the donor names and re-prompt.
#If the user types a name not in the list, add that name to the data structure and use it.
#If the user types a name in the list, use it.
#Once a name has been selected, prompt for a donation amount.
#Convert the amount into a number 
#Add that amount to the donation history of the selected user.
#Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.




Donors = {'william gates':[3, 3000.45], 
               'Jeff Bezos': [2, 3452.00], 
               'Paul Allen': [2, 9970.65], 
               'Mark Zuckerberg': [5,5000.75 ], 
               'David': [3, 2500.17], 
               'Michael': [4, 1500.00], 
               'Allen': [1, 2400.35]}


def Create_report(): 

    """Create a report of donors and their history of the amounts they have donated"""
    
    donor_report = []
    for name in Donors: 
        total_donation = (Donors[name][1]) 
 
        donation_times = (Donors[name][0]) 
        avg_donate = round((total_donation / donation_times), 2) 
        donor_report.append((name, total_donation, donation_times, avg_donate)) 
        donor_report.sort(key=lambda x: x[1] , reverse=True) 

    print("\n\n") 
    print("{:16} {:20} {:25} {:25}\n".format( "Name", "Total Donation", "Number of Gifts", "Average Gifts")) 
    for i in donor_report: 
        print("{:16} {:<20} {:<25} {:<25}".format( i[0], i[1], i[2], i[3])) 

    print("\n\n\n")



def Add_donor():
    
    """ prompt for a Full Name.if user types 'list' show donor names,if types 'quit'
        return to the main menu ,if types a name not in the list add that to the list,
        if types a name in the list use it and prompt for donation amount,Add that amount
        to the donation history """

    while True: 

        print("\nEnter 'list' to see list of names.") 

        print("Enter 'quit' to go back.")
        print("Enter 'name' to add new donor.")
        
        name = input("Please enter a name: ")
        
        if (name == 'list'):
 
            Show_list()
            
        elif (name == 'quit'): 
            break
        
        else: 

            donation_amount = get_donation() 

            if (donation_amount == 'quit'):
 
                break
            
            if (name not in Donors):
                
                Donors[name] = [1, donation_amount]
                
            else:
                
                Donors[name][0] = Donors[name][0] + 1 
 
                Donors[name][1] = Donors[name][1] + donation_amount
 
            Send_Thank_you_letter(name, donation_amount)
 
            break
        
        
def Show_list():
    
    print("\nDonor Names:") 
    print("-" *15 ) 
    for name in Donors:
 
        print(name)       


def get_donation():
    """ Take donation from the donor"""

    while True: 
        print("\nPlease enter donation amount. " 

             " Or Enter 'quit' to return to main menu.")
 
        donation = input("$")
        
        if (donation == 'quit'): 
            return donation
        
        else: 
            donation = float(donation)
 
            return donation 
        
            
              

def Send_Thank_you_letter(name, donation_amount): 
    message = ("\nDear {},\n\nThank you for your most recent donation of ${}. " 

               " You have donated\na total of ${} to the " 
               "BEYOND VISION MUSIC FOUNDATION.  Our company greatly appreciates the continued " 

               "generosity from individiuals like you.")
               

    message = (message.format(name, donation_amount, Donors[name][1])) 
#    print(message) 
    return message


def exit_program():
    
    print("Bye!")
    sys.exit()
              


if (__name__ == '__main__'):
    
    while True: 
        print("\nPlease choose a menu option below:") 

        print("1- Send a Thank you") 

        print("2- Create a Report") 
        
        print("3- quit") 

        menu_option = input(">>> ")
        
        if (menu_option == "1"): 
            Add_donor()
 
        if (menu_option == "2"):
            Create_report()
 
        
        elif (menu_option == "3"):
            
             exit_program()

        
        else: 
            print("Sorry. '%s' is not a valid menu option." % menu_option) 
              
