import pandas as pd

class CreateAccount:
    def __init__(self):
        print("Loading Creating Account page...")
    # # adds account to .csv file
    # # returns: True if account add was successful; False if account could not be added
    def addAcc(self, username, name, surname, password):
        # read account info from file
        columns = ['Username', 'Password', 'First_Name', 'Last_Name']
        data = pd.read_csv('users.csv', names = columns)
        userList = data.Username.tolist()
        passList = data.Password.tolist()
        firstNames = data.First_Name.tolist()
        lastNames = data.Last_Name.tolist()
        # remove headers from lists so they are not read as an account combination
        userList.remove("Username")
        passList.remove("Password")
        firstNames.remove("First_Name")
        lastNames.remove("Last_Name")

        # check to see if max accounts has been reached
        if len(userList) >= 6:
            print("The maximum amount of accounts has already been made!")
            print("Returning to home page...")
            return False
        else:
            # append retrieved data to list
            userList.append(username)
            passList.append(password)
            firstNames.append(name)
            lastNames.append(surname)

            dictionary = {'Username':userList, 'Password':passList, 'First_Name':firstNames, 'Last_Name':lastNames}
            df = pd.DataFrame(dictionary)
            df.to_csv('users.csv', index=False)

            print("Account has successfully been created! Returning to home page...")
            return True
