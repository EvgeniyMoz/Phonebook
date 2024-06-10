def ask_data():
    s_name = input("Введите Фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите Отчество: ")
    phone = input("Введите номер телефона: ")
    contact = {
        'second_name': s_name,
        'first_name': f_name,
        'middle_name': m_name,
        'phone_number': phone
    }
    return contact

def add_new_contact():
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        values = contact.values()
        file.write(';'.join(values) + '\n')
    return True

def open_phonebook():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip().split(";"), end="\t")

def modify_contact():
    name = input("Введите имя или фамилию контакта, которого вы хотите изменить: ")
    contacts = []
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for line in file:
            contact = line.strip().split(";")
            contacts.append(contact)
    
    for contact in contacts:
        if name in contact:
            new_contact = ask_data()
            index = contacts.index(contact)
            contacts[index] = list(new_contact.values())
            break
    
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        for contact in contacts:
            file.write(';'.join(contact) + '\n')

def delete_contact():
    name = input("Введите имя или фамилию контакта, которого вы хотите удалить: ")
    contacts = []
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for line in file:
            contact = line.strip().split(";")
            contacts.append(contact)
    
    for contact in contacts:
        if name in contact:
            contacts.remove(contact)
            break
    
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        for contact in contacts:
            file.write(';'.join(contact) + '\n')

def main():
    isStop = '1'
    while isStop != '0':
        print("Выберите что хотите сделать:\n1 - посмотреть\n2 - добавить\n3 - сохранить\n4 - открыть\n5 - изменить\n6 - удалить\n0 - выход")
        isStop = input(">")
        if isStop == '2':
            add_new_contact()
        elif isStop == '4':
            open_phonebook()
        elif isStop == '5':
            modify_contact()
        elif isStop == '6':
            delete_contact()
        input("Нажмите Enter чтобы продолжить")

main()
