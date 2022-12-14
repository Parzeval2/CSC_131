##########################################################################
# author: Grant Cooper
# date:    12/12/2022
# desc:   counted the significant digits
#########################################################################
from random import randint, seed

SHOWLIST = False  # a boolean to determine whether to show the list
MIN = 0  # the smallest random number that can be created.
MAX = 1000  # the largest random number that can be created.


# A function that prompts the user for two pieces of information i.e.
# the size of the list they want to create, and the seed that will be
# used for the list creation. It then returns both pieces of information to the
# calling statement.
def userint():
    LIST_SIZE = int(input("Please enter an integer to determine the list size: "))
    SEED = int(input("Please enter a number to act as a seed: "))
    return LIST_SIZE, SEED


# A function that prints out a list. It receives two pieces of data. The
# first is a string representing the name of the list. The second is a
# list containing all the relevant data. It proceeds to print out the
# name, and then all the elements of the data separated using a tab
# space. Both the name and the entire list are printed on a single line.
def listprint(NAME, LIST):
    PRINTSTRING = (NAME + '\t')
    for i in range(len(LIST)):
        PRINTSTRING += (str(LIST[i]) + "\t")
    print(PRINTSTRING)


# A function that creates the list of random numbers. It receives two
# arguments: one for the size of list to be created, and another for the
# seed that will be used to create the list. The function creates the
# list using the global variables MIN and MAX to form a bound for the
# kinds of numbers that are added to the list. The list is then returned
# to the calling statement.
def listcreate(size, SEED):
    seed(SEED)
    RANDOMLIST = []
    for i in range(size):
        RANDOMLIST.append(randint(MIN, MAX))
    return RANDOMLIST


# A function that recieves a list of numbers and returns another list
# containing the frequency of the lists Most Significant Digits (MSD). The
# list created by the function has 10 elements with each value
# corresponding to a different possible MSD i.e. the value in index 0
# shows the number of values in the original number list that have 0 as
# their most significant digit; the value in index 1 shows the number of
# values with 1 as their MSD; and so on and so forth. This 10 element
# list is returned to the calling statemet.
def msd(LIST):
    MSD_LIST = [0] * 10
    for INT in LIST:
        msd_index = int(str(INT)[0])
        MSD_LIST[msd_index] += 1
    return MSD_LIST


# Similar to the function above, a function that recieves a list of
# numbers, and returns another list of 10 elements where each element
# represents the frequency of a specific Least Significant Digit in the
# original list.
def lsd(LIST):
    LSD_LIST = [0] * 10
    for INT in LIST:
        lsd_index = int(str(INT)[-1])
        LSD_LIST[lsd_index] += 1
    return LSD_LIST


# Header
def headermake():
    count = 0
    HEADER = '\t'
    while count < 10:
        HEADER += (str(count) + '\t')
        count += 1
    print(str(HEADER))
    line = ((len(HEADER) * 2) * '-')
    print(line)


# Showlist
def showlist(SHOWLIST):
    if SHOWLIST:
        print("Original list:")
        print(RANDOM_LIST)


###################################### MAIN ############################
# using the functions defined above:
#   prompt the user for the size of the list to be created as well as the seed.
LIST_SIZE, SEED = userint()
#   create the list of random numbers
RANDOM_LIST = listcreate(LIST_SIZE, SEED)
#   If SHOWLIST is selected, print out the list of numbers
showlist(SHOWLIST)
#   print the head of the table which just shows the numbers 0-9
headermake()
#   Calculate the MSD and LSD, and print out their statistics.
listprint("MSD", msd(RANDOM_LIST))
listprint("LSD", lsd(RANDOM_LIST))
