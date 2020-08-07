from pprint import pprint

def get_favorite(favorite_contact):
    if favorite_contact == False:
        return 'Нет'
    else:
        return favorite_contact


class Phonebook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    # добавить контакт
    def __add__(self, other):
        self.contacts.append(other)

    # вывести все контакты из телефонной книги
    def all_contacts(self):
        for contact in self.contacts:
            print(contact)

    # удаление контакта
    def del_contact(self, phone_number):
        i = 0
        for contact in self.contacts:
            if contact.get_phone_number() == phone_number:
                del(self.contacts[i])
            i += 1

    # поиск контакта по имени
    def search_by_name_last_name(self, name, last_name):
        for contact in self.contacts:
            if (contact.get_name() == name) and (contact.get_last_name() == last_name):
                return contact

    # поиск контакта с избранным номером
    def search_favorite(self,favorite_contact):
        contacts_who_favorite_contact = []
        for contact in self.contacts:
            if contact.get_favorite() == favorite_contact:
                contacts_who_favorite_contact.append(contact)
        for contacts in contacts_who_favorite_contact:
            print(contacts)


class Contact:
    def __init__(self, name, last_name, phone_number, favorite_contact=False, **kwargs):
        self.dict_of_contact = {}
        self.dict_of_contact['Имя'] = name
        self.dict_of_contact['Фамилия'] = last_name
        self.dict_of_contact['Телефон'] = phone_number
        self.dict_of_contact['Избранный контакт'] = favorite_contact
        self.dict_of_contact['дополнительная информация'] = kwargs

    def get_favorite(self):
        return self.dict_of_contact['Избранный контакт']

    def get_phone_number(self):
        return self.dict_of_contact['Телефон']

    def get_name(self):
        return self.dict_of_contact['Имя']

    def get_last_name(self):
        return self.dict_of_contact['Фамилия']

    def __str__(self):
        for keys, values in self.dict_of_contact.items():
            print(f'{keys} : {values}')
        return ''

jhon = Contact('Jhon', 'Smith', '+71234567809', 'нет', telegram='@jhony', email='jhony@smith.com')
kate = Contact('Kate', 'Oldington', '+79301236574', '+71234567809', email='katasonic@gmail.com')

exmple_book = Phonebook('exmple_book')

exmple_book.__add__(jhon)
exmple_book.__add__(kate)

# exmple_book.del_contact('+71234567809')

exmple_book.all_contacts()

# print(exmple_book.search_by_name_last_name('Jhon', 'Smith'))

exmple_book.search_favorite('+79301236574')

