# just call the log in function
def signUp(loggedIn):
    loggedIn = Login().getLoginInput(loggedin)

# display help center message
def helpCenter():
    print("We're here to help!")

# print about us message
def about():
    print("In College: Welcome to In College, the world's largest college student network with many users in many "
          "countries and territories worldwide")

# print press message
def press():
    print("In College Pressroom: Stay on top of the latest news, updates, and reports")

# print blog message
def blog():
    print("Currently under construction. Please check back soon!")

# prints careers message
def careers():
    print("Currently under construction. Please check back soon!")

# print developers message
def developers():
    print("Currently under construction. Please check back soon!")

# print browse message
def browse():
    print("Currently under construction. Please check back soon!")

# print business solutions message
def businessSolutions():
    print("Currently under construction. Please check back soon!")

# print directories message
def directories():
    print("Currently under construction. Please check back soon!")

def usefulLinks(loggedIn):
    while True:
        print("                         InCollege - Useful Links                          ")
        print("Please select one of the following options to view the associated document.")
        print("""
            1. Sign Up
            2. Help Center
            3. About
            4. Press
            5. Blog
            6. Careers
            7. Developers
            8. Browse InCollege
            9. Business Solutions
            10. Directories
            
            
            11. Return Home
        """)
        try:
            newOption = int(input("Choice: "))
            print()
            # Sign Up option
            if newOption == 1:
                signUp(loggedIn)
            # Help Center option
            elif newOption == 2:
                helpCenter()
            # About option
            elif newOption == 3:
                about()
            # Press option
            elif newOption == 4:
                press()
            # Blog option
            elif newOption == 5:
                blog()
            # Careers option
            elif newOption == 6:
                careers()
            # Brand Policy option
            elif newOption == 7:
                developers()
            # Browse option
            elif newOption == 8:
                browse()
            # Business Solutions option
            elif newOption == 9:
                businessSolutions()
            # Directories Option
            elif newOption == 10:
                directories()
            # Return home option
            elif newOption == 8:
                print("Returning to home page...")
                break
        except ValueError:
            print("You provided a non-integer value.")
