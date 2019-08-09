import sys

donors_name = {'william gates':[3, 3000.45],
               'Jeff Bezos': [2, 3452.00], 
               'Paul Allen': [2, 9970.65], 
               'Mark Zuckerberg': [5,5000.75 ], 
               'David': [3, 2500.17], 
               'Michael': [4, 1500.00], 
               'Allen': [1, 2400.35]}



prompt = "\n".join(("Please select a menu option below:",

                    "1 - Send a Thank You to an individual",

                    "2 - Create a Report",

                    "3 - Send letters to all donors",

                    "4 - Quit",

                    ">>> "))


def create_report(): 

    """Create a detailed report of donors and their history of the amounts they have donated"""
    
    donor_report = []
    for name in donors_name: 
        total_donation = (donors_name[name][1]) 
 
        donation_times = (donors_name[name][0]) 
        avg_donate = round((total_donation / donation_times), 2) 
        donor_report.append((name, total_donation, donation_times, avg_donate)) 
        donor_report.sort(key=lambda x: x[1] , reverse=True) 

    print("\n\n") 
    print("{:16} {:20} {:25} {:25}\n".format( "Name", "Total Donation", "Number of Gifts", "Average Gifts")) 
    for i in donor_report: 
        print("{:16} {:<20} {:<25} {:<25}".format( i[0], i[1], i[2], i[3])) 

    print("\n\n\n")


def donor_list():
    """ Updated by Comprehensions"""
    
    name_list = [name for name in DONORS_NAME]    
    return '\n'.join(name_list)

def get_donation():
    """ updated this function using Error handling.
        It gets donation from the donor"""
    while True:       
        donation = input("\nPlease Enter a Valid Amount.""\n$")
                               
        try:
            donation = float(donation)
            return donation
        except ValueError:
             print("\nError.It is not valid amount.")
             
def send_thank_you_letter(name, donation_amount):
    """ Create a thank you message """
    message = f"{name},Thank you for your most recent donation of ${DONORS_NAME[name][1]}."
    return message

def file_name(name):
    'Return a txt file name based on the donor name and using underscores instead of spaces'
    return name.replace(' ', '_') + '.txt'

def send_letter_for_all():
    """ Send a thank you message to all donors"""
    print("***\nloading letters for all donors\n***")
    for name in list(DONORS_NAME.keys()):
        amount = DONORS_NAME[name][0] * DONORS_NAME[name][1]
        message = send_thank_you_letter(name, amount) 
        save_letter_disk(message, name, str(amount))
