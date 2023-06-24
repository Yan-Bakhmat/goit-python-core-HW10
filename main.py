from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, Record):
        self.update({Record.Name.name: Record})


class Record:
    def __init__(self, Name, *Phones):
        self.Name = Name
        self.Phones = list(Phones)

    def add_phone(self, name_and_numbers):
        name_and_numbers = name_and_numbers.split(' ')
        self.Phones = list(set(self.Phones) | set(name_and_numbers[1:]))
        return "Done!"

    def change_phone(self, name_and_numbers):
        name_and_numbers = name_and_numbers.split(' ')
        self.Phones = name_and_numbers[1:]
        return "Done!"

    def delite_phone(self, name_and_numbers):
        name_and_numbers = name_and_numbers.split(' ')
        self.Phones = list(set(self.Phones) - set(name_and_numbers[1:]))
        return "Done!"


class Field:
    def __init__(self, name, phone=None, e_mail=None):
        self.name = name
        self.phone = phone
        self.e_mail = e_mail


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)


CONTACTS = AddressBook()


def hello():
    return 'How can I help you?'


def add_or_change_contact(name_and_number):
    name_and_number = name_and_number.split(' ')
    CONTACTS[name_and_number[0]] = name_and_number[1]
    return "Done!"


def show_number(name):
    return CONTACTS[name]


def show_all(contacts):
    for name, number in contacts.items():
        yield f'{name}: {number}'


def close():
    return "Good bye!"


def input_error(func):
    def inner():
        flag = True
        while flag:
            try:
                result = func()
                flag = False
            except IndexError:
                print('Enter the name and numbers separated by a space.')
            except ValueError:
                print('I have no idea how you did it, try again.')
            except KeyError:
                print("The contact is missing.")
        return result
    return inner


@ input_error
def main():
    bot_status = True
    while bot_status:
        command = input('Enter the command: ').lower()
        if command == 'hello':
            print(hello())
        elif 'add' in command:
            print(AddressBook.add_record(
                Record.add_phone(command.removeprefix('add '))))
#            print(add_or_change_contact(
#                command.removeprefix('add ')))
        elif "change" in command:
            print(add_or_change_contact(
                command.removeprefix('change ')))
        elif "phone" in command:
            print(show_number(command.removeprefix("phone ")))
        elif command == "show all":
            if CONTACTS:
                for contact in show_all(CONTACTS):
                    print(contact)
            else:
                print('The contact list is empty.')
        elif command in ("good bye", "bye", "close", "exit"):
            print(close())
            bot_status = False
        else:
            print("Enter correct command, please.")


if __name__ == '__main__':
    main()
