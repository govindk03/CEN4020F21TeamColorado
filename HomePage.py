# Home page file for team Colorado
# Implemented via python
from Error import Error
from CreateAccount import CreateAccount 
from Login import Login
from JobBoard import JobBoard
from SkillsPage import Skills
import re
# boolean to determine if logged in
loggedIn = False

# string to int
while True:

    # block of code for user who is not logged in
    if not loggedIn:
        print("\n              Home Page               ")
        print("Please select one of the following options")
        print("""
            1. Log-In
            2. Create an account
            3. Search for a job
            4. Find someone you know
            5. Learn a new skill
            6. Exit

            Student success story:
            My name is John Shephard and I graduated from college with a BCS degree. I stumbled
            upon InCollege when searching for jobs before graduating. Using this program, I
            was instantly connected with hundreds of employers who all met or exceeded my desired
            criteria. I now have been working with a company for 4 years and have already
            recieved multiple promotions! Thanks InCollege!\n
            7. Watch a video to see more of my story
        """)
    else:
        print("\n              Home Page               ")
        print("Please select one of the following options")
        print("""
            1. Log-Out (logged in as """ + loggedIn + """)
            2. Create an account
            3. Search for a job
            4. Find someone you know
            5. Learn a new skill
            6. Exit
        """)
    try:
        newOption = int(input("Choice: "))
        print()
        # Log-In option
        if newOption == 1:
            # Call the Log-In page function
            loggedIn = Login().getLoginInput(loggedIn)
        # Create an account option
        elif newOption == 2:
            # helper functions to get user input for parameters
            # username 
            def setUsername():
                name = input("Provide the username for the new account: ")
                return name
            # first name
            def setFirstName():
                name = input("Provide your first name: ")
                return name
            # last name
            def setLastName():
                name = input("Provide your last name: ")
                return name
            # password
            def setPassword():
                while True:
                    password = input("Provide password of the new account: ")
                    if (len(password) < 8 and len(password) > 12):
                        print("Your password should be between 8 and 12 characters")
                        continue
                    elif not re.search("[a-z]", password):
                        print("Your password should have a lower case letter")
                        continue
                    elif not re.search("[A-Z]", password):
                        print("Your password should have an upper case letter")
                        continue
                    elif not re.search("[0-9]", password):
                        print("Your password should have an integer")
                        continue
                    elif not re.search("[!-/]", password):
                        print("Your password should have a special character")
                        continue
                    elif re.search("\s", password):
                        print("Your password contains a forbidden character")
                        continue
                    else:
                        print("Valid Password")
                        return password
            # call functions to retrieve parameters
            username = setUsername()
            firstName = setFirstName()
            lastName = setLastName()
            password = setPassword()
            # instantiate CreateAccount object 
            x = CreateAccount()
            # call addAccount function to write into users.csv
            x.addAcc(username, firstName, lastName, password)

        # Search for a job option
        elif newOption == 3:
            # helper functions for parameters
            def setTitle():
                title = input("Job title: ")
                return title

            def setDesc():
                desc = input("Job description: ")
                return desc

            def setEmployer():
                employer = input("Employer: ")
                return employer

            def setLocation():
                location = input("Job location: ")
                return location

            def setSalary():
                salary = input("Salary: ")
                return salary
            # Call the JobBoard.py jobSelect function
            x = JobBoard()
            x.jobSelect(loggedIn, setTitle(), setDesc(), setEmployer(), setLocation(), setSalary())
        # Find someone you know option
        elif newOption == 4:
            x = Error()
            x.underConstruction()
        # Learn a new skill option
        elif newOption == 5:
            # Call the SkillsPage.py skillSelect function
            x = Skills()
            x.skillSelect()
        elif newOption == 6:
            # exit program
            exit()
        elif newOption == 7 and loggedIn:
            print("Video is now playing.")
    except ValueError:
        print("You provided a non-integer character.")