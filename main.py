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
