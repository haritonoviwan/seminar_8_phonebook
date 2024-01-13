# Задача №49.
# Создать телефонный справочник с возможностью импорта и экспорта данных 
# в формате .txt. Фамилия, имя, отчество, номер телефона - данные, 
# которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи (например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

('phonebook.txt', 'a')

def file_read():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        return file.read()
    
def file_append(text=''):
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(text)

def input_surname():
    return input('Введите фамилию: ')

def input_name():
    return input('Введите имя: ')

def input_patronymic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите телефон: ')

def input_adress():
    return input('Введите адрес: ')

def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    print()

    contact_str = f"{surname} {name} {patronymic} {phone}\n{adress}\n\n"
    file_append(contact_str)

def print_data():
    print(file_read())

def search_contact():
    print("Возможные варианты поиска\n"
          "1. По фамилии \n"
          "2. По имени\n"
          "3. По отчеству\n"
          "4. По телефону\n"
          "5. По адресу\n")
    command = input("Выберите вариат поиска: ")

    while command not in ("1", "2", '3', '4', "5"):
        print("Некорректный ввод. Повторите попытку\n")
        command = input("Выберите вариат поиска: ")

    i_var = int(command) - 1
    search = input('Введите данные для поиска: ')
    print()
    contacts_list = file_read().rstrip().split("\n\n")
    # print(contacts_list)

    for contact_str in contacts_list:
        cont_list = contact_str.replace("\n", " ").split()
        if search in cont_list[i_var]:
            print(contact_str)
        print()

def copy_entry(source_file, destination_file, entry_number):
    with open(source_file, 'r', encoding='UTF-8') as source:
        entries = source.read().rstrip().split("\n\n")

        if 0 < entry_number <= len(entries):
            entry_to_copy = entries[entry_number - 1]
            
            with open(destination_file, 'a', encoding='UTF-8') as dest:
                dest.write(entry_to_copy + '\n\n')
            print(f"Запись номер {entry_number} успешно скопирована.")
        else:
            print(f"Ошибка: записи с номером {entry_number} не существует.")

def u_interface():
    file_append()
    command = ""
    while command != "5":
        print("Меню: \n"
              "1. Добавить контакт \n"
              "2. Найти контакт\n"
              "3. Вывести все контакты\n"
              "4. Копировать запись\n"
              "5. Выход\n")
        command = input("Выберите пункт меню: ")

        while command not in ("1", "2", '3', '4', '5'):
            print("Некорректный ввод. Повторите попытку\n")
            command = input("Выберите пункт меню: ")            
        print()
        match command:
            case "1":
                input_data()
            case "2":
                search_contact()
            case "3":
                print_data()
            case "4":
                entry_number = int(input("Введите номер записи для копирования: "))
                copy_entry('phonebook.txt', 'copied_phonebook.txt', entry_number)
            case "5":
                print("Пока 👋")

# input_data()
# print_data()
# search_contact()
u_interface()