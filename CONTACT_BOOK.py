class Contact:
    def __init__(self, name: str, phone: str, email: str, address: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name: str, phone: str, email: str, address: str):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact added: {new_contact}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term: str):
        results = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                print(contact)

    def update_contact(self, old_name: str, new_name: str = None, new_phone: str = None, new_email: str = None, new_address: str = None):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_name if new_name else contact.name
                contact.phone = new_phone if new_phone else contact.phone
                contact.email = new_email if new_email else contact.email
                contact.address = new_address if new_address else contact.address
                print(f"Contact updated: {contact}")
                return
        print("Contact not found.")

    def delete_contact(self, name: str):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact deleted: {contact}")
                return
        print("Contact not found.")


def user_interface():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        
        elif choice == "2":
            contact_book.view_contacts()
        
        elif choice == "3":
            search_term = input("Enter name or phone to search: ")
            contact_book.search_contact(search_term)
        
        elif choice == "4":
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name (or press Enter to skip): ")
            new_phone = input("Enter new phone (or press Enter to skip): ")
            new_email = input("Enter new email (or press Enter to skip): ")
            new_address = input("Enter new address (or press Enter to skip): ")
            contact_book.update_contact(old_name, new_name, new_phone, new_email, new_address)
        
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        
        else:
            print("Invalid option. Please try again."    )    

if __name__ == "__main__":
    user_interface()
