from address_book_classes import *
from contats_handler import *
a = Record("a")
a.add_phone('0365986565')
a.add_birthday('10.01.2000')
book = AddressBook()
book.add_record(a)
print(type(a.birthday))
print(book)
print(book.get_upcoming_birthdays())


def parse_command(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print('Hi, i am a bot-helper! How can i help you?')
    contacts = AddressBook()

    while True:
        user_input = input('Enter the command: ')
        command, *args = parse_command(user_input)

        if command in ['exit', 'close']:
            print('Good bye!')
            break

        elif command in ['hello', 'hi']:
            print('Hi!')

        else:
            match command:
                case 'add':
                    print(add_contact(args, contacts))
                case 'change':
                    print(change_contact(args, contacts))
                case 'phone':
                    print(show_phone(args, contacts))
                case 'all':
                    print(show_all_contacts(contacts))
                case 'add-birthday':
                    print(add_birthday(args, contacts))
                case 'show-birthday':
                    print(show_birthday(args, contacts))
                case 'birthdays':
                    print(birthdays(contacts))
                case _:
                    print('Sorry, i don`t know command like that yet.')


if __name__ == '__main__':
    main()

