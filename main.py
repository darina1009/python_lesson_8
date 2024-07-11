def find_by_lastname(phone_book, last_name):
    result = []
    for record in phone_book:
        if record['Фамилия'] == last_name:
            result.append(record)
    return result

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
    return phone_book

def delete_by_lastname(phone_book, last_name):
    result = []
    for record in phone_book:
        if record['Фамилия'] != last_name:
            result.append(record)
    return result

def find_by_number(phone_book, number):
    result = []
    for record in phone_book:
        if record['Телефон'] == number:
            result.append(record)
    return result

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)
    return phone_book

def print_result(phone_book):
    for record in phone_book:
        print(','.join(record.values()))

def work_with_phonebook():
    choice = show_menu()
    phone_book=read_txt('phon.txt')
    while choice != 9:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new number ')
            change_number(phone_book, last_name, new_number)
        elif choice == 4:
            last_name = input('lastname ')
            phone_book = delete_by_lastname(phone_book, last_name)
        elif choice == 5:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ')
            add_user(phone_book, user_data)
        elif choice == 7:
            write_txt('phonebook.txt', phone_book)
        elif choice == 8:
            src_filename = input('source file name ')
            dest_filename = input('destination file name ')
            record_num = int(input('record number to copy '))
            copy_record(src_filename, dest_filename, record_num)

        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер телефона абонента\n"
          "4. Удалить абонента из справочника\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Добавить абонента в справочник\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Копировать запись из одного файла в другой\n"
          "9. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            phout.write(','.join(record.values()) + '\n')



def copy_record(src_filename, dest_filename, record_num):
    src_records = read_txt(src_filename)

    if record_num < 1 or record_num > len(src_records):
        print(f"Error: Record number {record_num} is out of range.")
        return

    record_to_copy = src_records[record_num - 1]

    dest_records = read_txt(dest_filename)

    dest_records.append(record_to_copy)

    write_txt(dest_filename, dest_records)

    print(f"Record {record_num} copied from {src_filename} to {dest_filename}.")            

work_with_phonebook()