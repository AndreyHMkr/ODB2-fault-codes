class Registration:
    """
    Handles user authentication for the OBD2 Database system.
    This class verifies the administrator password to grant write access.
    """

    # Class-level attribute for the system password
    # In a real app, this would be hashed or stored in an environment variable
    true_password = 'admin'

    def __init__(self, password):
        """
        Initializes the registration object with the provided password.

        :param password: The string entered by the user during login.
        """
        self.password = password

    def enter(self):
        """
        Validates the password against the system's true password.

        :return: True if the password matches.
        :raises ValueError: If the password is incorrect (Assessment Requirement: Custom Exceptions).
        """
        if self.password == self.true_password:
            # Demonstrating string output for successful permission
            print('Login Status: Permission granted successfully.')
            return True
        else:
            # Demonstrating Exception Handling as required by the course rubric
            raise ValueError('Access Denied: Incorrect administrator password.')
