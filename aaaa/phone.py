#1. UI (User interface)
#2. Создать файл 
#3. Читать файл
#4. Вывод данных на экран:
 #   -считать файл
 #  -вывести на экран
#5. Запись контакта:
#    -запросить данные
#    -сохранить в перменную
#    -записать в файл
#6. Поиск контакта:
#    -запросить данные поиска
#    -сохранить в переменную
#    -считать файл
#    -сохранить в переменную
#    -произвести поиск

#Добавление контакта

def name_data():
    return input('Ввведите имя: ')

def surname_data():
    return input('Введите фамилию: ')

def patronymic_data():
    return input('Введите отчество: ')

def phone_number_data():
    return input('Введите номер телефона: ')

def address_data():
    return input('Введите адрес: ')

def input_contact():
    name = name_data()
    surname = surname_data()
    patrnymic = patronymic_data()
    phone_number = phone_number_data()
    address = address_data()
    return f'{name} {surname} {patrnymic}\n{phone_number}\n{address}'

def add_contacts():
    contact = input_contact()
    with open('Phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(contact + '\n\n')

#Чтение файла

def read_file():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        return data.read()

#Печать контактов

def print_contacts():
    data = read_file()
    print(data)

#Поиск контакта

def search_contact():
    search = input ('Введите данные для поиска: ')
    data = read_file().rstrip()
    if search not in data:
        print('Информация отсутствует')
    else:
        print([data])
        data = data.split('\n\n')
        print(data)
        for el in data:
            if search in el:
                print(el)
                print()

#Удаление контакта

def delete_contact():
    print("Введите информацию про контакт, который хотите удалить. ")
    contact = input_contact()
    data = read_file()
    if contact in data:
        with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact, '')
            data2.write(data)
            print(data2)
    else:
        print("Нет такой позиции")

#Изменение контакта

def change_contact():
    print("Введите информацию про контакт, который хотите изменить. ")
    contact = input_contact()
    data = read_file()
    if contact in data:
        print("Введите новый контакт")
        new_contact = input_contact()
        with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact, new_contact)
            data2.write(data)
            print(data2)
    else:
        print("Нет такой позиции")



def user_interface():
    with open('Phonebook.txt', 'a', encoding='utf-8'):
        pass
    cmd = None
    while cmd!= '4':
        print('1. Запись контакта\n'
        '2. Вывести данные на экран\n'
        '3. Поиск контакта\n'
        '4. Выход\n'
        '5. Удалить контакт\n'
        '6. Изменить контакт')

        cmd = input("Введите номер операции: ")
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        match cmd:
            case '1':
                add_contacts()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                print("До свидания!")
            case '5':
                delete_contact()
            case '6':
                change_contact()

user_interface()