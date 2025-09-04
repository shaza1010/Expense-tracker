'''
# Expense Tracker
A program to track personal expenses. Every entry includes a description, amount, and date.
The user can add, edit, delete, and view all entries. It calculates and displays the total amount spend.
'''

## the libraries and files imported
from datetime import datetime, timedelta
import calendar

## The class for every entry
class Entry:
    def __init__(self, amount, date, description):
        '''make an entry with the amount(int), date(datetime)
        , description(non-empty) string'''
        self.amount = int(amount)
        self.date = datetime.strptime(date, "%d-%m-%Y")
        self.description = description

    def valid_description(self):
        '''check if the description is non-empty string'''
        return self.description != ""
    
    def display_entry(self, index):
        '''display the entry (id, amount, date)
        and it's description'''
        left_str = f"{index}# {self.amount} L.E"
        right_str = self.date.strftime("%d-%m-%Y")
        # .ljust(), .rjust() to align the text
        line = left_str.ljust(60) + right_str.rjust(15)
        print(line)
        print("  ", self.description)
        print("-" * len(line))

## The class to store the history
class Entries_history:
    def __init__(self):
        self.history = []
        self.data_file = ""

    def sort_history(self):
        self.history.sort(key=lambda entry: entry.date)

    def add_entry(self, entry):
        if entry.valid_description():
            self.history.append(entry)
            self.sort_data()
            return self.history.index(entry)
        else:
            raise Exception("The description can not be empty.")

    def sort_data(self):
        self.sort_history()
        with open(self.data_file, 'w') as f:
            f.write("amount,date,description\n")
            for entry in self.history:
                f.write(f"{entry.amount},{entry.date.strftime('%d-%m-%Y')},{entry.description}\n")

    def load_past_entries(self):
        with open(self.data_file, "r") as file:
            next(file) # skips the header
            for line in file:
                parameters = line.strip().split(',')
                if len(parameters) < 3:
                    # Skipping bad line
                    continue
                amount = parameters[0]
                date = parameters[1]
                # So it won't crash if the description has a ','
                description = ",".join(parameters[2:])
                entry = Entry(amount, date, description)
                self.add_entry(entry)
        self.sort_data()

    def edit_entry(self, index, new_amount, new_date, new_description):
        entry = self.history[index]
        if new_amount is not None:
            entry.amount = new_amount
        if new_date is not None:
            entry.date = datetime.strptime(new_date, "%d-%m-%Y")
        if new_description is not None:
            entry.description = new_description
        self.sort_data()

    def delete_entry(self, index):
        self.history.pop(index)
        self.sort_data()

    def show_history(self, start_date=None, end_date=None):
        total = 0
        count = 0
        for i, entry in enumerate(self.history):
            if start_date and end_date:
                if not (start_date <= entry.date.date() <= end_date):
                    continue
            entry.display_entry(i)
            total += entry.amount
            count += 1
        if count == 0: print("No entries in that date frame.")
        else: print(f"Total amount spent:   {total} L.E")
        
    def get_total(self):
        return sum(entry.amount for entry in self.history)


def main():
    title = '''
╔───────────────────────────────────────────────────────────────────╗
│ ██████████                                                        │
│░░███░░░░░█                                                        │
│ ░███  █ ░█████ █████████████   ██████  ████████   █████   ██████  │
│ ░██████ ░░███ ░░███░░███░░███ ███░░███░░███░░███ ███░░   ███░░███ │
│ ░███░░█  ░░░█████░  ░███ ░███░███████  ░███ ░███░░█████ ░███████  │
│ ░███ ░   ████░░░███ ░███ ░███░███░░░   ░███ ░███ ░░░░███░███░░░   │
│ ██████████████ █████░███████ ░░██████  ████ ███████████ ░░██████  │
│░░░░░░░░░░░░░░ ░░░░░ ░███░░░   ░░░░░░  ░░░░ ░░░░░░░░░░░   ░░░░░░   │
│                     ░███                                          │
│ ███████████         █████            █████                        │
│░█░░░███░░░█        ░░░░░            ░░███                         │
│░   ░███  ░████████  ██████    ██████ ░███ █████  ██████  ████████ │
│    ░███  ░░███░░███░░░░░███  ███░░███░███░░███  ███░░███░░███░░███│
│    ░███   ░███ ░░░  ███████ ░███ ░░░ ░██████░  ░███████  ░███ ░░░ │
│    ░███   ░███     ███░░███ ░███  ███░███░░███ ░███░░░   ░███     │
│    █████  █████   ░░████████░░██████ ████ █████░░██████  █████    │
│   ░░░░░  ░░░░░     ░░░░░░░░  ░░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░     │
╚───────────────────────────────────────────────────────────────────╝
'''
    print(title)
    history = Entries_history()
    history.data_file = "history.txt"
    history.load_past_entries()

    print('''A program to track personal expenses. Every entry includes a description, amount, and date.
The user can add, edit, delete, and view all entries. It calculate and display the total amount spend.''')
    history.show_history()
    
    while True:
        print("\n(add - edit - delete - show entry - show all - show time - total spend - exit)")
        action = input("What would you like to do? ")
        
        if action == "add":
            amount = input("Enter amount: ")
            date = input("Enter date(dd-mm-yyyy): ")
            description = input("Enter description: ")
            
            try:
                entry = Entry(amount, date, description)
                index = history.add_entry(entry)
            except ValueError:
                print("Value Error: make sure you entered a valid number and date")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            else:
                print(f"Entry stored successfully. ID: {index}")

        elif action == "edit":
            try:
                index = int(input("entry's ID: "))
                print("press ENTER if you don't want to change")
                new_amount = input("New Amount: ")
                new_date = input("New Date(dd-mm-yyyy): ")
                new_description = input("New description: ")

                new_amount = int(new_amount) if new_amount.strip() else None
                new_date = new_date if new_date.strip() else None
                new_description = new_description if new_description.strip() else None

                history.edit_entry(index, new_amount, new_date, new_description)
            except ValueError:
                print("Value Error: make sure you entered a valid number and date")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            else: 
                print("Entry edited successfully")

        elif action == "delete":
            index = int(input("Entry ID: "))
            history.delete_entry(index)
            print("Entry deleted successfully")

        elif action == "show entry":
            index = int(input("Entry ID: "))
            entry = history.history[index]
            entry.display_entry(index)
        
        elif action == "show all":
            history.show_history()

        elif action == "show time":
            time = input("Show this (day - week - month - year - custom): ")
            today = datetime.today().date()
            if time == "day": 
                start_date = end_date = today
            elif time == "week":
                start_date = today - timedelta(days=today.weekday())
                end_date = start_date + timedelta(days=6)
            elif time == "month":
                start_date = today.replace(day=1)
                end_date = today.replace(day=calendar.monthrange(today.year, today.month)[1])
            elif time == "year":
                start_date = datetime(today.year, 1, 1).date()
                end_date = datetime(today.year, 12, 31).date()
            elif time == "custom":
                try:
                    start_date = input("Enter start date(dd-mm-yyyy): ")
                    end_date = input("Enter end date(dd-mm-yyyy): ")
                    start_date = datetime.strptime(start_date, "%d-%m-%Y").date()
                    end_date = datetime.strptime(end_date, "%d-%m-%Y").date()
                except ValueError:
                    print("Wrong format in date.")
            else:
                print("Not a known action. Please check your spelling.")
            
            history.show_history(start_date, end_date)

        elif action == "total spend":
            print(f"Total amount spent: {history.get_total()} L.E")

        elif action == "exit": break
        else:
            print("Not a known action. Please check your spelling.")

if __name__ == '__main__':
    main()
    print('\n')