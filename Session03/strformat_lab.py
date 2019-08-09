
#Write a format string that will take four element tuple:

tuple=( 2, 123.4567, 10000, 12345.67)

print("'First item: {:03d}, second item: {:.2f}\n,third item :{:.2e} and fourth item: {:.2e}'".format(*tuple))




#Task-3

def formatter(in_tuple):
    width= 4
    tuple_m =(4,)*in_tuple
    
#   format_string="'{:d},{:d},{:d},{:d}'"

    format_template = '%%%ds : %%%ds'
# later:
    width = 20
    format_string = format_template % (width, width)

    
    return format_string.format(*tuple_m)


print(formatter(4))


#Task-4
#Write a format string that will take five element tuple
# and print tuple using index number to specify position


tuple=( 4, 30, 2017, 2, 27)

print("'{:02d},{:d},{:d},{:02d},{:d}'".format(tuple[3],tuple[4],tuple[2],tuple[0],tuple[1]))


#Task-5
# Take four element list and display it using f string

list=['oranges', 1.3, 'lemons', 1.1]
list_1=(f' The weight of an {list[0].upper()} is {list[1]*(1.2)} and the weight of a {list[2].upper()} is {list[3]*(1.2)}')

print(list_1)

#Task-6




