import pandas as pd

# main function
# returns: string fullName = full name of found user; False if no user found
def main():
    while True:
        print("     Search-A-User Page      \n")
        firstName = input("Please enter the FIRST NAME of the user you would like to search for: ")
        lastName = input("Please enter the LAST NAME of the user you would like to search for: ")

        # read data from .csv file
        columns = ['Username', 'Password', 'First_Name', 'Last_Name']
        data = pd.read_csv('users.csv', names = columns)
        firstNames = data.First_Name.tolist()
        lastNames = data.Last_Name.tolist()
        # remove headers from lists so they are not read as an account combination
        firstNames.remove("First_Name")
        lastNames.remove("Last_Name")

        # search for the user in the list
        if firstName in firstNames and lastName == lastNames[firstNames.index(firstName)]:
            print("This person is a part of the InCollege system.")
            fullName = firstName + ' ' + lastName
            print("Returning to home page...")
            return fullName
        else:
            print("This person is not yet a part of the InCollege system.")
            print("Returning to home page...")
            return False