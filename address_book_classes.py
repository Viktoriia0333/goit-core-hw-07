from datetime import datetime, timedelta
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Birthday(Field):
    def __init__(self, value: str):
        super().__init__(self)
        try:
            datetime.strptime(value, '%d.%m.%Y')
            self.value = value
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        super().__str__()


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if phone not in [p.value for p in self.phones]:
            self.phones.append(Phone(phone))
        else:
            return 'Contact already has this number'

    def edit_phone(self, old, new):
        if len(new) == 10:
            for i in self.phones:
                if i.value == old:
                    index = self.phones.index(i)
                    self.phones[index] = Phone(new)
        else:
            raise ValueError

    def find_phone(self, phone):
        for i in self.phones:
            if phone == i.value:
                return i

    def remove_phone(self, phone):
        for i in self.phones:
            if phone == i.value:
                self.phones.remove(i)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        birthday = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"

    def __repr__(self):
        return str(self)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name] if name in self.data else None

    def delete(self, name):
        self.data.pop(name) if name in self.data else None

    @staticmethod
    def find_next_monday(date, weekday=0):
        time_delta = timedelta(days=weekday - date.weekday())
        monday = date + time_delta + timedelta(days=7)
        return monday

    def get_upcoming_birthdays(self):
        current_date = datetime.now().date()
        birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, '%d.%m.%Y').date()
                birthday_date = birthday_date.replace(year=current_date.year)
                if (birthday_date - current_date) <= timedelta(days=7):
                    if birthday_date.weekday() >= 5:
                        birthday_date = self.find_next_monday(birthday_date)
                    birthdays.append({'name': record.name.value, 'to congratulate': str(birthday_date)})
        return birthdays

    def __str__(self):
        result = []
        for name, record in self.data.items():
            result.append(str(record))
        return "\n".join(result)
