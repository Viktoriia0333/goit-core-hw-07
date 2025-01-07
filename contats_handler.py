from address_book_classes import *


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please. Phone must include 10 numbers"
        except KeyError:
            return 'There is no this contact in your contacts list'
        except IndexError:
            return 'Enter the arguments'
        except AttributeError:
            return 'Contact not found'

    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        message = 'Contact added'
        book.add_record(record)
    else:
        message = 'Contact updated'

    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return 'Contact changed'


@input_error
def show_phone(args: str,  book: AddressBook):
    name = args[0]
    record = book.find(name)
    phones = []
    for phone in record.phones:
        phones.append(phone.value)
    return phones


@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    record.add_birthday(birthday)
    return 'birthday added'


@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    return record.birthday.value


@input_error
def birthdays(book: AddressBook):
    return book.get_upcoming_birthdays()


@input_error
def show_all_contacts(book: AddressBook):
    return book
