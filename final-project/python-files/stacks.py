# This is just a solution with a test case embedded.
# Don't pay attention to every detail here. 
# The most important part is the logic behind the function adding_student()
#======================= Global Variables ===================

max_seats = 2 # how many students are allowed per course
subscribers = [] # list of all students who have subscribed
waiting_list = [] # list of all students who are on the waiting list

#======================= Set up for the test cases ==========
# pip instal faker
from faker import Faker

to_enroll = [] # list of fake generated emails that will be populated to fill out the other 2 lists above
test_cases = 3 # how many emails we will generate to test case our program

#======================= Functions ==========================
def adding_students(email):
    """This function gets an email address and add it to the subscriber or to the waiting list
       depending on how many seats are available 
    """
    if len(subscribers) < max_seats:
        # Checking if there are already people in the waiting list
        if len(waiting_list) > 0:
            subscribers.append(waiting_list[0])
            waiting_list.pop(0)
        # If not, add new subscribers
        else:
            subscribers.append(email)

    # Adding future students to the waiting list since they can't enroll this time
    else:
        waiting_list.append(email)

def display():
    """This function only displays the subscribers and the waiting list"""
    print(f"The subscribers list now is \n {subscribers}")
    print('------------------------------')
    print(f"The waiting list now is \n {waiting_list}")
    print('------------------------------')

def email_generator():
    """This function generates fake emails to populate the lists"""
    fake = Faker()
    for n in range(0, test_cases):
        to_enroll.append(fake.email())

    for email in to_enroll:
        adding_students(email)
    
    for n in range(0, len(to_enroll)):
        to_enroll.pop(0)


def tester():
    """This function populates the lists again and display them to the end-user"""
    email_generator()
    display()

#------------------- Test Cases ------------------------------
print("================= Test Cases =================")

#First row
tester()

#Removing the first student from the subscriber list
print("Now, let's remove the first student from the subscribers list and see what happens when more students try to enroll...")
print("------------------------------")
subscribers.pop(0)
tester()
print("Notice how the first student in the waiting list was added to the end of the subscriber list when there were spots available")
print("------------------------------")

#Removing all students
print("Now let's remove all the students in the waiting list and see what happens...")
print("------------------------------")
subscribers = []
tester()

    



