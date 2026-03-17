"""
    Main entry point for the OBD2 Database Application.
    Handles user authentication and the main interaction loop.
"""
import os

from create_js_file_with_errors import DatabaseManage
from registration import Registration

# Create database manager with default Ford error file
db = DatabaseManage('ford_error.json')

# Session dictionary to store user status
user_session = {'is_admin': False}


def display_header():
    """Displays the application header and current status."""
    print("\n" + "="*45)
    print("      OBD2 DIAGNOSTIC DATABASE (FORD)      ")
    print("="*45)
    # Extracting filename using slicing to show understanding
    current_file = os.path.basename(db.file_path)
    print(f"ACTIVE DATABASE: {current_file}")
    print(f"USER STATUS: {'ADMIN' if user_session['is_admin'] else 'GUEST'}")
    print("-" * 45)


# Main program loop
while True:
    display_header()
    print('\nChoice action:')

    # Display menu options depending on user role
    if not user_session['is_admin']:
        print('0 - Log-in')
        print('1 - Find a fault code')
        print('4 - Switch file')
        print('5 - Exit')
    else:
        print("1 - find a fault code")
        print("2 - add new fault")
        print("3 - Change the database file")
        print("4 - Switch file")
        print("5 - Exit")
    choice = input("Select option: ")
    if choice == '0':
        password = input('Enter password: ')
        try:
            register = Registration(password)
            if register.enter():
                user_session['is_admin'] = True
                print('Status changed to Admin')
        except ValueError as e:
            print(f'Wrong password - {e}')
    elif choice == '1':
        db.find()
    elif choice == '2':
        if user_session['is_admin']:
            db.add()
        else:
            print('You cant add, no access permission')
    elif choice == '3':
        new_filename = input('Enter a name for the new file (e.g. focus3_errors): ').strip()
        db.change_database(new_filename)
        print(f'Now all data will be saved in {new_filename}.json')
    elif choice == '4':
        files = db.show_all_json_files()
        if files:
            index = input('Select your choice number to switch: ')
            if index.isdigit() and 0 < int(index) <= len(files):
                new_name = files[int(index) - 1]
                db.change_database(new_name)
    elif choice == '5':
        print('Goodbye!')
        break
    else:
        print('Invalid choice, try again.')
