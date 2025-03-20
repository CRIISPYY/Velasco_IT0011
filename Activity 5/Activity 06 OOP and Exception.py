class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        try:
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            if not name.strip():
                raise ValueError("Name cannot be empty.")
            if price < 0:
                raise ValueError("Price cannot be negative.")
            self.items[item_id] = Item(item_id, name, description, price)
            print(f"Item '{name}' added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def read_item(self, item_id=None):
        if item_id:
            item = self.items.get(item_id)
            if item:
                print(item)
            else:
                print("Item not found.")
        else:
            item_list = [str(item) for item in self.items.values()]
            if item_list:
                for item in item_list:
                    print(item)
            else:
                print("No items available.")

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id in self.items:
            item = self.items[item_id]
            if name:
                if not name.strip():
                    print("Error: Name cannot be empty.")
                    return
                item.name = name
            if description:
                item.description = description
            if price is not None:
                if price < 0:
                    print("Error: Price cannot be negative.")
                    return
                item.price = price
            print(f"Item '{item_id}' updated successfully!")
        else:
            print("Item not found.")

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print(f"Item '{item_id}' deleted successfully!")
        else:
            print("Item not found.")


def main():
    manager = ItemManager()

    while True:
        print("===========================================")
        print("Please choose your choice")
        print("\n1. Create Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        print("===========================================")

        try:
            choice = int(input("type in your choice: "))

            if choice == 1:
                item_id = input("Enter Item ID: ").strip()
                name = input("Enter Item Name: ").strip()
                description = input("Enter Item Description: ").strip()
                price = float(input("Enter Item Price: "))
                manager.create_item(item_id, name, description, price)

            elif choice == 2:
                view_id = input("Enter Item ID to view (leave empty to view all): ").strip()
                manager.read_item(view_id if view_id else None)

            elif choice == 3:
                item_id = input("Enter Item ID to update: ").strip()
                name = input("Enter new name (leave empty to keep unchanged): ").strip()
                description = input("Enter new description (leave empty to keep unchanged): ").strip()
                price_input = input("Enter new price (leave empty to keep unchanged): ").strip()
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name or None, description or None, price)

            elif choice == 4:
                item_id = input("Enter Item ID to delete: ").strip()
                manager.delete_item(item_id)

            elif choice == 5:
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
