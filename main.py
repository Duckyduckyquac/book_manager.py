import pandas as pd
import csv
#Initialization
try:
    df = pd.read_csv('test.csv')
except FileNotFoundError:
    print("\n\n\nNo CSV File Found. File being created...\n\n\n")
    df = pd.DataFrame(columns=['Title', 'Author', 'Rating'])
    df.to_csv('test.csv', index=False)

#Logic Blocks
def search_books():
    df = pd.read_csv('test.csv')
    to_search = input("Input the book to search: ").strip().title()
    actual_book = df[df['Title'] == to_search]
    print(f"\n\nHere is the book you searched for: \n\n{actual_book}")


def add_books():
    df = pd.read_csv('test.csv')
    title = input("Title of the book to add: ").strip().title()
    author = input("Author of the book to add: ").strip().title()
    while True:
        try: 
            rating = float(input("Rating of the book to add: "))
            if rating > 5 or rating <1:
                print("Input a number between 1 to 5")
            else:
                break
        except ValueError:
            print("Input a number, try again!")
    new_book = {
        'Title':[title],
        'Author':[author],
        'Rating':[rating]
                }
    df = pd.read_csv('test.csv')
    df = pd.concat([df, pd.DataFrame(new_book)], ignore_index = True)
    df.to_csv('test.csv', index=False)
    print("The book has been successfully added! ")


def delete_book():
    to_del = input("Title of the book to delete: ").strip().title()
    df = pd.read_csv('test.csv')

    if to_del in df['Title'].values:
        df = df[df['Title'] != to_del]
        df.to_csv('test.csv', index=False)
        print(f"{to_del} has been deleted.")
    else:
        print("The book is not found! ")

def view_books():
    df = pd.read_csv('test.csv')
    print(f"The books you have are the following: \n\n\n{df}\n\n\n")

def clean_data():
    df = pd.read_csv('test.csv')
    print(f"The number of values with"
          f"missing data are:{df.isnull().sum()}")
    confirmation = input("Confirm for deletion? Yes or No?").strip().lower()
    if confirmation == 'yes':
        df.dropna(inplace = True)
        df.to_csv('test.csv', index=False)
        print("The values with missing data have been deleted! ")
    else:
        print("Operation aborted... ")

def sort_data():
    df = pd.read_csv('test.csv')
    df = df.sort_values(by='Rating', ascending = False)
    df.to_csv('test.csv', index=False)

    print("\n\n\nThe data has now been successfully sorted. It looks like this:\n\n\n")
    view_books()

def get_userchoice():
    while True:
        try:
            x = int(input("What would you like to do?\n\n1. Search Books\n2. Add Books\n3. Delete Books\n4. View Books\n5. Clean Data\n6. Sort Data\n7. Exit: \n\n "))
            if x > 7 or x < 1:
                print("\n\n\nInput a number within 1 to 7, Try again!\n\n\n")
            else:
                return x
        except ValueError:
            print("\n\n\nInput a number, try again!\n\n\n")


#Main Code
print(f"\n\n---- Welcome to the Book List! ----\n\n")
choice = get_userchoice()

while True:
    if choice == 1:
        search_books()
    elif choice == 2:
        add_books()
    elif choice == 3:
        delete_book()
    elif choice == 4:
        view_books()
    elif choice == 5:
        clean_data()
    elif choice == 6:
        sort_data()
    elif choice == 7:
        break
    choice = get_userchoice()
