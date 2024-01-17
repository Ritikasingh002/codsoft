class ListItem:
    def __init__(self, item_name, progress="Not Started"):
        self.item_name = item_name
        self.progress = progress

class List:
    def __init__(self):
        self.items = []

    def add_item(self):
        item_name = input("Input item name: ")
        new_item = ListItem(item_name)
        self.items.append(new_item)
        print(f"Item '{item_name}' added successfully!")

    def view_items(self):
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item.item_name} - {item.progress}")

    def update_item(self):
        item_number = int(input("Input item number to update: "))
        progress = input("Enter new progress: ")
        if item_number > 0 and item_number <= len(self.items):
            self.items[item_number-1].progress = progress
            print(f"Item '{self.items[item_number-1].item_name}' updated successfully!")
        else:
            print("Invalid item number.")

    def delete_item(self):
        item_number = int(input("Input item number to delete: "))
        if item_number > 0 and item_number <= len(self.items):
            print(f"Item '{self.items[item_number-1].item_name}' deleted successfully!")
            del self.items[item_number-1]
        else:
            print("Invalid item number.")

def run():
    list = List()
    while True:
        print("\n1. Add Item\n2. View Items\n3. Update Item\n4. Delete Item\n5. Exit")
        selection = int(input("Choose an option: "))
        if selection == 1:
            list.add_item()
        elif selection == 2:
            list.view_items()
        elif selection == 3:
            list.update_item()
        elif selection == 4:
            list.delete_item()
        elif selection == 5:
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    run()
