class Person:
    def __init__(self, fullname, mobile, email_id, residence):
        self.fullname = fullname
        self.mobile = mobile
        self.email_id = email_id
        self.residence = residence

class Directory:
    def __init__(self):
        self.entries = []

    def new_entry(self):
        fullname = input("Input full name: ")
        mobile = input("Input mobile number: ")
        email_id = input("Input email ID: ")
        residence = input("Input residence address: ")
        person = Person(fullname, mobile, email_id, residence)
        self.entries.append(person)
        print(f"Entry for {fullname} created successfully!")

    def list_entries(self):
        for person in self.entries:
            print(f"Full Name: {person.fullname}, Mobile: {person.mobile}")

    def find_entry(self):
        fullname = input("Input full name to find: ")
        for person in self.entries:
            if person.fullname == fullname:
                print(f"Full Name: {person.fullname}, Mobile: {person.mobile}, Email ID: {person.email_id}, Residence: {person.residence}")
                return
        print("Entry not found.")

    def modify_entry(self):
        fullname = input("Input full name to modify: ")
        mobile = input("Input new mobile number (leave blank to keep current): ")
        email_id = input("Input new email ID (leave blank to keep current): ")
        residence = input("Input new residence address (leave blank to keep current): ")
        for person in self.entries:
            if person.fullname == fullname:
                if mobile:
                    person.mobile = mobile
                if email_id:
                    person.email_id = email_id
                if residence:
                    person.residence = residence
                print(f"Entry for {fullname} modified successfully!")
                return
        print("Entry not found.")

    def remove_entry(self):
        fullname = input("Input full name to remove: ")
        for i, person in enumerate(self.entries):
            if person.fullname == fullname:
                del self.entries[i]
                print(f"Entry for {fullname} removed successfully!")
                return
        print("Entry not found.")

# Create a new directory
my_directory = Directory()

while True:
    print("\n1. New Entry\n2. List Entries\n3. Find Entry\n4. Modify Entry\n5. Remove Entry\n6. Quit")
    selection = input("Make your selection: ")
    if selection == '1':
        my_directory.new_entry()
    elif selection == '2':
        my_directory.list_entries()
    elif selection == '3':
        my_directory.find_entry()
    elif selection == '4':
        my_directory.modify_entry()
    elif selection == '5':
        my_directory.remove_entry()
    elif selection == '6':
        break
    else:
        print("Invalid selection. Please try again.")
