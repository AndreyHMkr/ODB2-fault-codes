import json
import os


class DatabaseManage:
    """
        Handles all operations related to the fault code database.
        Responsible for saving, loading, and searching for codes in a JSON file.
    """
    def __init__(self, file_path):
        """
            Initializes the database manager with a specific file path.
            :param file_path: String representing the path to the JSON database.
        """
        self.file_path = file_path

    def save(self, fault_obj):
        """
               Adds a new fault code object to the database while preserving existing data.
               :param fault_obj: An instance of AddNewOBDCode class.
        """
        data = self._load_all()
        # Key: Fault Code (e.g., P0171), Value: Description
        data[fault_obj.code] = fault_obj.description

        with open(self.file_path, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add(self):
        """Admin interface for entering a new fault code via the console."""
        try:
            code = input('Enter fault code (e.g., P0171): ').upper().strip()
            first_char = code[:1]
            numeric = code[1:]
            if first_char not in ['P', 'C', 'B', 'U']:
                print(f'Warning: code should be start with {first_char}')
            if not numeric.isdigit() and len(code) > 3:
                print('Note: The numeric part of the code should usually contain only numbers.')
            description = input('Enter fault description: ').strip()

            new_fault = AddNewOBDCode(code, description)

            self.save(new_fault)
            print(f'New fault {code} successfully added!')

        except ValueError as e:
            print(f'Error - {e}')

    def _load_all(self):
        # Check if database file exists
        if not os.path.exists(self.file_path):
            return {}
        if os.path.getsize(self.file_path) == 0:
            return {}
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f'Warning: File {self.file_path} is corrupted. New dictionary created.')
            return {}

    def find(self):
        while True:
            code = input('Enter fault code for search description(or exit if you want to go out): ').upper()
            if code == 'exit'.upper():
                break
            data = self._load_all()
            result = data.get(code, f'Error, {code} not found in database.')
            print(f'Result: {result}')

    def change_database(self, new_path):
        if not new_path.endswith('.json'):
            new_path += '.json'
        self.file_path = new_path
        print(f'Path changed to {self.file_path}')

    def show_all_json_files(self):
        all_files = os.listdir('.')
        json_files = [file for file in all_files if file.endswith('.json')]
        if not json_files:
            print('Files not found.')
            return []
        print('\n --- Available files --- ')
        for index, file in enumerate(json_files, 1):
            mark = " (ACTIVE)" if file == os.path.basename(self.file_path) else ""
            print(f"{index}. {file}{mark}")

        return json_files


class AddNewOBDCode:
    def __init__(self, code, description):
        if not code or not description:
            raise ValueError('Code and description cant be empty.')
            self.code = code
            self.description = description
