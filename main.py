from collections import UserDict

import re

class Field: # Базовий клас для полів запису.
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): # Клас для зберігання імені контакту. Обов'язкове поле
    def __init__(self, value):
        self.value = value

class Phone(Field): # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    # Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
    # Наслідує клас Field. Значення зберігaється в полі value .
    
    def __init__(self, value):

        assert len(re.findall(r"\d", value)) == 10, f"Phone number {value} doest't have correct format: it must have 10 digits only"
        self.value = value
    
class Record: # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    
    # Реалізовано зберігання об'єкта Name в атрибуті name.
    # Реалізовано зберігання списку об'єктів Phone в атрибуті phones.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    # Реалізовано метод для додавання - add_phone. 
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
        #print(f'Phone {phone} added to the contact of {self.name}')

    # Реалізовано метод для видалення - remove_phone.
    def remove_phone(self, phone: str):
        if phone in [p.value for p in self.phones]:
            for p in self.phones:
                if p.value == phone:
                    self.phones.remove(p) 
                    #print(f'Phone number {phone} for the contact of {self.name} successfully removed')   
        else:
            print(f'Phone number {phone} for the contact of {self.name} not identified')   
    
    # Реалізовано метод для редагування - edit_phone.
    def edit_phone(self, phone: str, new_phone: str):
        if phone in [p.value for p in self.phones]:
            for p in self.phones:
                if p.value == phone:
                    p.value = new_phone
                    #print(f'Phone number {phone} for the contact of {self.name} changed into {new_phone}')
        else:
            raise ValueError            

    # Реалізовано метод для пошуку об'єктів Phone - find_phone. 
    def find_phone(self, phone: str):
        if phone in [p.value for p in self.phones]:
            for p in self.phones:
                if p.value == phone:
                    return p
                    #print(f'Phone number {phone} found in the Contact of {self.name}')    

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



class AddressBook(UserDict): # Клас для зберігання та управління записами. 
    
    # Реалізовано метод add_record, який додає запис до self.data. 
    def add_record(self, record):
        self.data[record.name.value] = record 
        
    # Реалізовано метод find, який знаходить запис за ім'ям.
    def find(self, name: str):
        return self.data.get(name)
        
    # Реалізовано метод delete, який видаляє запис за ім'ям.
    def delete(self, name: str):
        del self.data[name]
    
    # Реалізовано магічний метод __str__ для красивого виводу об’єкту класу AddressBook .
    def __str__(self):
        string = "AdressBook:"
        for i in self.data:
            string += "\n"
            string += str(self.data[i])
        return string
        #return "\n".join(str(record) for record in self.data.values()) как альтернатива

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1111111111")
john_record.add_phone("2222222222")
#print(john_record)

# Додавання запису John до адресної книги
book.add_record(john_record)

#Редагування запису John
#john_record.remove_phone("2222222222")
#print(john_record)

#john_record.edit_phone("1111111111", "333333333")
#print(john_record)

#john_record.remove_phone("2222222222")
#print(john_record)

# Пошук конкретного телефону у записі John 
#print(john_record.find_phone("333333333"))


# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("4444444444")
jane_record.add_phone("5555555555")
#print(jane_record)

# Додавання запису Jane до адресної книги
book.add_record(jane_record)

#Редагування запису Jane
#jane_record.remove_phone("5555555555")
#print(jane_record)

#jane_record.edit_phone("4444444444", "666666666")
#print(jane_record)

# Пошук конкретного телефону у записі Jane 
#print(jane_record.find_phone("5555555555"))

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1111111111", "666666666")

print(john)  # Виведення: Contact name: John, phones: ........

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("666666666")
print(f"{john.name}: {found_phone}")  # Виведення: John: ........

# Видалення запису Jane
book.delete("Jane")
print(book)


