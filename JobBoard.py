import Error
import pandas as pd

class JobBoard: 
    def __init__(self):
        print("Loading Job Board...")

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

    # function to create a job listing
    # returns: True if listing creation successful, False if unsuccessful
    def createJobListing(self, fullName, title, description, employer, location, salary):
        # read file to check job listings
        columns = ['Title','Description','Employer','Location','Salary','created_by']
        data = pd.read_csv('jobs.csv', names = columns)
        titleList = data.Title.tolist()
        descList = data.Description.tolist()
        employerList = data.Employer.tolist()
        locationList = data.Location.tolist()
        salaryList = data.Salary.tolist()
        namesList = data.created_by.tolist()
        # remove headers 
        titleList.remove("Title")
        descList.remove("Description")
        employerList.remove("Employer")
        locationList.remove("Location")
        salaryList.remove("Salary")
        namesList.remove("created_by")

        # check to see if max amount of jobs posted
        if len(titleList) >= 5:
            print("Maximum amount of jobs listings has already been posted. Please come back later!")
            return False
        else:
            print("Please enter the following fields.")
            # append retrieved data to list
            titleList.append(title)
            descList.append(description)
            employerList.append(employer)
            locationList.append(location)
            salaryList.append(salary)
            namesList.append(fullName)

            dictionary = {'Title':titleList, 'Description':descList, 'Employer':employerList, 'Location':locationList, 'Salary':salaryList, 'created_by':namesList}
            df = pd.DataFrame(dictionary)
            df.to_csv('jobs.csv', index=False)

            print("Job listing has successfully been created!")
            return True

    # main function
    # input: loggedIn = string containing logged-in user's name, or False if empty (nobody logged in)
    def jobSelect(self, loggedIn):
        while True:
            print("             Job Board             ")
            print("Please select one of the following options")
            print("""
            1. Find a job listing
            2. Create a job listing (must be logged in)
            3. Back to home page
            """)
            try:
                newOption = int(input("Choice: "))
                print('\n')
                # Find a job listing option
                if newOption == 1:
                    Error.underConstruction()
                # Create a job listing option
                elif newOption == 2 and loggedIn:
                    self.createJobListing(loggedIn, self.setTitle(), self.setDesc(), self.setEmployer(), self.setLocation(), self.setSalary())
                # Deny job creation if not logged in
                elif newOption == 2 and not loggedIn:
                    print("You must be logged in to post a job listing!\n")
                # Back to home page option
                elif newOption == 3:
                    print("Returning to home page...")
                    break
            except ValueError:
                print("You provided a non-integer character.")
